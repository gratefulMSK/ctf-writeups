import math
import gmpy2
from pwn import *

host = "titan.picoctf.net"
port = 51335
context.log_level = 'debug'

def get_encrypted_value(io, payload):
    io.recvuntil(b"decrypt. \n")
    io.sendline(b"E")
    io.recvuntil(b"keysize):")
    io.sendline(payload)
    io.recvuntil(b"mod n)")
    return int(io.recvline().strip().decode())

def get_decrypted_value(io, c):
    io.recvuntil(b"decrypt. \n")
    io.sendline(b"D")
    io.recvuntil(b"Enter text to decrypt: ")
    io.sendline(str(c).encode())
    io.recvuntil(b"decrypted ciphertext as hex (c ^ d mod n): ")
    return int(io.recvline().strip().decode(), 16)

def main():
    io = remote(host, port)
    
    # -----------------------------------------
    # STEP 1: 正しいバイナリで暗号文を取得し、Nを暴く
    # -----------------------------------------
    log.info("Nを計算するためのデータを取得中...")
    c2 = get_encrypted_value(io, b'\x02')
    c3 = get_encrypted_value(io, b'\x03')
    c4 = get_encrypted_value(io, b'\x04')
    c6 = get_encrypted_value(io, b'\x06')
    
    X = (c2 * c3) - c6
    Y = (c2 * c2) - c4
    N = math.gcd(X, Y)

    # Nが偶数である限り、2で割って余分な成分を削ぎ落とす
    while N % 2 == 0:
        N //= 2
    
    log.success(f"N の特定に成功: {N}")
    
    if N <= 1:
        log.error("Nの計算に失敗しました（Nが1以下です）。")
        return

    # -----------------------------------------
    # STEP 2: ターゲット暗号文を偽装して復号させる
    # -----------------------------------------
    # ※※ ここに、本来解読したい暗号文（フラグなど）をint型で入れてください ※※
    C_flag = 2575135950983117315234568522857995277662113128076071837763492069763989760018604733813265929772245292223046288098298720343542517375538185662305577375746934 # ← 実際の値に書き換える
    
    log.info("ターゲット暗号文に 2^e を掛けて偽装します...")
    # c2 は 2^e mod N そのものなので、そのまま掛ければOK
    C_new = (C_flag * c2) % N 
    
    log.info("オラクルに偽装暗号文を復号させています...")
    M_new = get_decrypted_value(io, C_new)
    
    # -----------------------------------------
    # STEP 3: Nと2の逆元を使って、正しい平文を取り出す
    # -----------------------------------------
    log.info("2の逆元を掛けて本来のデータに戻します...")
    inv_2 = gmpy2.invert(2, N)
    M_flag = (M_new * inv_2) % N
    
    # 16進数文字列に戻し、さらにASCII文字列（フラグ）に変換
    hex_flag = hex(M_flag)[2:] # 先頭の '0x' を取り除く
    if len(hex_flag) % 2 != 0:
        hex_flag = '0' + hex_flag # バイト列変換のため偶数桁に揃える
        
    flag_bytes = bytes.fromhex(hex_flag)
    log.success(f"🎉 復号成功!: {flag_bytes.decode(errors='ignore')}")
    
    io.close()

if __name__ == "__main__":
    main()