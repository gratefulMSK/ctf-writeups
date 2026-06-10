# アフィン暗号の総当たり＆復号スクリプト
import string

# aの候補（26と互いに素な数字）
a_candidates = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]
b_candidates = range(26)

def encrypt_affine(text, a, b):
    result = ""
    for c in text:
        if c.isalpha():
            base = ord('A') if c.isupper() else ord('a')
            idx = ord(c) - base
            new_idx = (a * idx + b) % 26
            result += chr(base + new_idx)
        else:
            result += c
    return result

def decrypt_affine(text, a, b):
    # aのモジュラ逆元を求める
    a_inv = pow(a, -1, 26)
    result = ""
    for c in text:
        if c.isalpha():
            base = ord('A') if c.isupper() else ord('a')
            idx = ord(c) - base
            new_idx = (a_inv * (idx - b)) % 26
            result += chr(base + new_idx)
        else:
            result += c
    return result

# ==========================================
# 👇 ここにサーバーから取得した情報を入れます 👇
# ==========================================
known_plain = "cheddar"
known_cipher = "MFEVVUR"           # サーバーが返してきた cheddar の暗号文を入れてください
secret_cipher = "DQSCAAQSUPF" # 最初に出題された Secret Cheese を入れてください

found_a, found_b = None, None

# 鍵(a, b)の探索
for a in a_candidates:
    for b in b_candidates:
        if encrypt_affine(known_plain, a, b).lower() == known_cipher.lower():
            found_a, found_b = a, b
            break
    if found_a is not None:
        break

if found_a is not None:
    print(f"[+] 鍵を発見！ a={found_a}, b={found_b}")
    plain_secret = decrypt_affine(secret_cipher, found_a, found_b)
    print(f"[+] 🎯 Secret Cheese の正解は: {plain_secret}")
else:
    print("[-] 鍵が見つかりませんでした。入力値を確認してください。")