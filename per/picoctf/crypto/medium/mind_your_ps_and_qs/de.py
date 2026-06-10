import gmpy2
from Crypto.Util.number import long_to_bytes
import sys

# --- 既知の値をここに入力してください ---

p = 1891771437429478964908181306574287207137
q = 501332739776173570344039681219489434626477
e = 65537
c = 15341890103764929939105506004034128738090325640037083301857608662849501626260517

# ---------------------------------------------
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
        print(f"m (UTF-8)  = '{m_bytes[::-1].decode('utf-8')}'")
    except UnicodeDecodeError:
        print("（m は有効な UTF-8 文字列ではありません）")

except Exception as e:
    print(f"バイト列への変換中にエラーが発生しました: {e}", file=sys.stderr)