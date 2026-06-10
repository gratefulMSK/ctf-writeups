from pwn import *
from binascii import unhexlify

# 接続先設定
host = "wily-courier.picoctf.net"
port = 49892

# 50,000文字のペイロード
payload = b"a" * 50000

print("[*] サーバーに接続しています...")
io = remote(host, port)

# 1. 起動直後に表示される「フラグの暗号文」を取得
io.recvuntil(b"This is the encrypted flag!\n")
enc_flag_hex = io.recvline().decode().strip()
enc_flag = unhexlify(enc_flag_hex)
L = len(enc_flag)  # フラグの本来の文字数(バイト数)

print(f"[*] 暗号化されたフラグを取得 (長さ: {L} bytes)")

# 2. 1回目の50,000文字送信
print("\n[*] 1回目の50,000文字( 'a'*50000 )を送信します...")
io.recvuntil(b"encrypt? ")
io.sendline(payload)
io.recvuntil(b"go!\n")
resp1_hex = io.recvline().decode().strip()
resp1 = unhexlify(resp1_hex)
print(f"[+] 1回目のレスポンス取得 (長さ: {len(resp1)} bytes)")

# 3. 2回目の50,000文字送信（循環の証明）
print("\n[*] 2回目の50,000文字を送信します...")
io.recvuntil(b"encrypt? ")
io.sendline(payload)
io.recvuntil(b"go!\n")
resp2_hex = io.recvline().decode().strip()
resp2 = unhexlify(resp2_hex)
print(f"[+] 2回目のレスポンス取得 (長さ: {len(resp2)} bytes)")

# 比較
if resp1 == resp2:
    print("[!] 1回目と2回目のレスポンスが完全に一致しました！（キー長50,000でのループを証明）\n")

# --- ここからフラグの復号（数学的な巻き戻し） ---
print("[*] 取得したデータからフラグを逆算します...")

# 1回目の50,000文字を送信した時、キーのスタート位置は「L（フラグの長さ）」でした。
# 50,000文字使い切ってちょうど1周したということは、
# 1回目のレスポンスの「末尾 L バイト」には、キーの「先頭 0〜L バイト」が使われています。

# キーの先頭部分を抽出 (レスポンスの末尾Lバイトと 'a' をXORしてキーを丸裸にする)
key_0_to_L = bytearray()
for b in resp1[-L:]:
    key_0_to_L.append(b ^ ord('a'))

# 抽出したキーを使って、最初のフラグ暗号文を復号する
flag = bytearray()
for i in range(L):
    flag.append(enc_flag[i] ^ key_0_to_L[i])

print("\n========================================")
print(f"[★] フラグ復元成功: {flag.decode(errors='ignore')}")
print("========================================")

io.close()