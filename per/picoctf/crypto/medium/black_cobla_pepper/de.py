from pwn import xor

# --- chall.py の関数定義 ---
def split(full_key):
    k = full_key
    k1 = ''
    k2 = ''
    k3 = ''
    k4 = ''
    sub_keys = [k1, k2, k3, k4]
    for i in range(len(k)):
        sub_keys[i%4] = str(sub_keys[i%4]) + str(k[0])
        k = k[1:]
    return sub_keys

def glue(parts):
    k = ''
    for i in range(32):
        k = str(k) + str(parts[i%4][0])
        parts[i%4] = str(parts[i%4][1:])
    return k

def rot_word(word):
    return str(word[2:]) + str(word[0:2])

def sub_word(word):
    return word

def rcon(word):
    return word

def gen_keys(master_key):
    keys = []
    rounds = 0
    k = master_key
    while (rounds < 11):
        keys.append(k)
        sub_keys = split(k)
        sub_keys[-1] = rot_word(sub_keys[-1])
        sub_keys[-1] = sub_word(sub_keys[-1])
        sub_keys[-1] = rcon(sub_keys[-1])
        sub_keys[0] = xor(bytes.fromhex(sub_keys[0]), bytes.fromhex(sub_keys[-1])).hex()
        sub_keys[1] = xor(bytes.fromhex(sub_keys[1]), bytes.fromhex(sub_keys[0])).hex()
        sub_keys[2] = xor(bytes.fromhex(sub_keys[2]), bytes.fromhex(sub_keys[1])).hex()
        sub_keys[3] = xor(bytes.fromhex(sub_keys[3]), bytes.fromhex(sub_keys[2])).hex()
        k = glue(sub_keys)
        rounds += 1
    return keys

def to_matrix(key):
    bytes_list = [int(key[i:i+2], 16) for i in range(0, 32, 2)]
    array = [[0] * 4 for _ in range(4)]
    for i in range(16):
        row = i % 4
        col = i // 4
        array[row][col] = hex(bytes_list[i])[2:].zfill(2)
    return array

def from_matrix(matrix):
    reconstructed = ''
    for col in range(4):
        for row in range(4):
            reconstructed += matrix[row][col].zfill(2)
    return reconstructed

def sub_bytes(state):
    return state

def shift_rows(state):
    placeholder = state[1][0]
    state[1][0], state[1][1], state[1][2], state[1][3] = state[1][1], state[1][2], state[1][3], state[1][0]
    state[2][0], state[2][1], state[2][2], state[2][3] = state[2][2], state[2][3], state[2][0], state[2][1]
    state[3][0], state[3][1], state[3][2], state[3][3] = state[3][3], state[3][0], state[3][1], state[3][2]
    return state

def gmul(a, b):
    b = int(b, 16)
    p = 0
    for c in range(8):
        if b & 1:
            p ^= a
        a <<= 1
        if a & 0x100:
            a ^= 0x11b
        b>>=1
    return p

def mix_columns(s):
    ss = [[0] * 4 for _ in range(4)]
    for c in range(4):
        ss[0][c] = hex(gmul(0x02, s[0][c]) ^ gmul(0x03, s[1][c]) ^ int(s[2][c], 16) ^ int(s[3][c], 16))[2:].zfill(2)
        ss[1][c] = hex(int(s[0][c], 16) ^ gmul(0x02, s[1][c]) ^ gmul(0x03, s[2][c]) ^ int(s[3][c], 16))[2:].zfill(2)
        ss[2][c] = hex(int(s[0][c], 16) ^ int(s[1][c], 16) ^ gmul(0x02, s[2][c]) ^ gmul(0x03, s[3][c]))[2:].zfill(2)
        ss[3][c] = hex(gmul(0x03, s[0][c]) ^ int(s[1][c], 16) ^ int(s[2][c], 16) ^ gmul(0x02, s[3][c]))[2:].zfill(2)
    for i in range(4):
        for j in range(4):
            s[i][j] = ss[i][j]
    return s

def AES(plaintext, key):
    ciphertext = plaintext
    round_keys = gen_keys(key)
    ciphertext = xor(bytes.fromhex(round_keys[0]), bytes.fromhex(ciphertext)).hex()
    for i in range(1,10):
        ciphertext = to_matrix(ciphertext)
        sub_bytes(ciphertext)
        shift_rows(ciphertext)
        mix_columns(ciphertext)
        ciphertext = from_matrix(ciphertext)
        ciphertext = xor(bytes.fromhex(round_keys[i]), bytes.fromhex(ciphertext)).hex()
    ciphertext = to_matrix(ciphertext)
    sub_bytes(ciphertext)
    shift_rows(ciphertext)
    ciphertext = from_matrix(ciphertext)
    ciphertext = xor(bytes.fromhex(round_keys[10]), bytes.fromhex(ciphertext)).hex()
    return ciphertext

# --- ガウスの消去法 ---
def solve_linear_system(A, b):
    n = 128
    mat = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(A[j][i])
        row.append(b[i])
        mat.append(row)
    for i in range(n):
        pivot = i
        while pivot < n and mat[pivot][i] == 0:
            pivot += 1
        if pivot == n: continue
        mat[i], mat[pivot] = mat[pivot], mat[i]
        for j in range(n):
            if i != j and mat[j][i] == 1:
                for k in range(n + 1):
                    mat[j][k] ^= mat[i][k]
    res = [0] * n
    for i in range(n):
        if mat[i][i] == 1:
            res[i] = mat[i][n]
    return res

# --- メイン処理 ---
pt = '72616e646f6d64617461313131313131'
ct = bytes.fromhex('d7481d89f1aaf5a857f56edd2ae8994c')

# 鍵の特定
B = bytes.fromhex(AES(pt, '00'*32))
B_bits = [ (b >> i) & 1 for b in B for i in range(8) ]
A_bits = []
for i in range(128):
    key_bits = [0]*128; key_bits[i] = 1
    key_hex = ''.join([hex(key_bits[j]|key_bits[j+1]<<1|key_bits[j+2]<<2|key_bits[j+3]<<3)[2:] for j in range(0,128,4)])
    ct_res = bytes.fromhex(AES(pt, key_hex))
    ct_bits = [ (b >> j) & 1 for b in ct_res for j in range(8) ]
    A_bits.append([c ^ b for c, b in zip(ct_bits, B_bits)])

ct_bits = [ (b >> j) & 1 for b in ct for j in range(8) ]
key_bits = solve_linear_system(A_bits, [c ^ b for c, b in zip(ct_bits, B_bits)])
key_hex = ''.join([hex(key_bits[i]|key_bits[i+1]<<1|key_bits[i+2]<<2|key_bits[i+3]<<3)[2:] for i in range(0,128,4)])

# フラグの復号
ct_flag = bytes.fromhex('8c7d66558130eb5796d131beb43c9934')
C_key = bytes.fromhex(AES('00'*32, key_hex))
C_key_bits = [ (b >> i) & 1 for b in C_key for i in range(8) ]
M_key_bits = []
for i in range(128):
    flag_bits = [0]*128; flag_bits[i] = 1
    flag_hex = ''.join([hex(flag_bits[j]|flag_bits[j+1]<<1|flag_bits[j+2]<<2|flag_bits[j+3]<<3)[2:] for j in range(0,128,4)])
    ct_res = bytes.fromhex(AES(flag_hex, key_hex))
    ct_bits = [ (b >> j) & 1 for b in ct_res for j in range(8) ]
    M_key_bits.append([c ^ b for c, b in zip(ct_bits, C_key_bits)])

ct_bits = [ (b >> j) & 1 for b in ct_flag for j in range(8) ]
flag_bits = solve_linear_system(M_key_bits, [c ^ b for c, b in zip(ct_bits, C_key_bits)])
flag_hex = ''.join([hex(flag_bits[i]|flag_bits[i+1]<<1|flag_bits[i+2]<<2|flag_bits[i+3]<<3)[2:] for i in range(0,128,4)])
print(f'Flag: {bytes.fromhex(flag_hex).decode()}')
