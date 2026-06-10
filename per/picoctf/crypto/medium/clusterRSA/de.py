from sympy import factorint

n = 8749002899132047699790752490331099938058737706735201354674975134719667510377522805717156720453193651
e = 65537
ct = 2630159242114455882250729812770100011736485763047361297871782218963814793905003742546116295910618429


import gmpy2
from Crypto.Util.number import long_to_bytes
import sys

# --- 既知の値をここに入力してください ---
p = 9671406556917033397931773
q = 9671406556917033398314601
r = 9671406556917033398439721
s = 9671406556917033398454847
e = 65537
c = ct

n = p * q * r * s
phi_n = (p - 1) * (q - 1) * (r - 1) * (s - 1)
try:
    d = gmpy2.invert(e, phi_n)
    if d == 0:
        raise ValueError("d が 0 になりました。e と phi_n が互いに素ではありません。")
except ValueError as err:
    print(f"エラー: 秘密鍵 d を計算できません。{err}", file=sys.stderr)
    sys.exit(1)

m = pow(c, d, n)

print("--- RSA復号結果 ---")
print(f"n = {n}")
print(f"d = {d}")
print(f"m (数値) = {m}")

# 5. 平文 (数値) をバイト列に変換
try:
    m_bytes = long_to_bytes(m)
    print(f"m (バイト列) = {m_bytes}")
    
    try:
        print(f"m (UTF-8)  = '{m_bytes.decode('utf-8')}'")
    except UnicodeDecodeError:
        print("（m は有効な UTF-8 文字列ではありません）")

except Exception as e:
    print(f"バイト列への変換中にエラーが発生しました: {e}", file=sys.stderr)