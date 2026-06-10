from sympy import factorint
import gmpy2
from Crypto.Util.number import long_to_bytes
import sys

# --- ここに素因数分解したい数を入れます ---
number_to_factor = 22366073089673907719644404341576291365593038129576775942560772083569587067702333298036452518159706889705186586629027498544826957890722013652785580904741942

# 素因数分解を実行
factors = factorint(number_to_factor)
print(f"{number_to_factor} の素因数分解:")
fac = [k for k, v in factors.items() if k != 2][0]
print(fac)


# --- 既知の値をここに入力してください ---
p = 2
q = fac
e = 65537
c = 14433795599863609365289902093732003552144010054860756834397594777952564550726737208210433649675522898923241945115846832587899356072387806436426375658470485

n = p * q
phi_n = (p - 1) * (q - 1)
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

