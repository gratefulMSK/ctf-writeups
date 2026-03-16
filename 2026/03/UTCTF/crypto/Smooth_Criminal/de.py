from Crypto.Util.number import long_to_bytes
from sympy import discrete_log, factorint

p = 1363402168895933073124331075716158793413739602475544713040662303260999503992311247861095036060712607168809958344896622485452229880797791800555191761456659256252204001928525518751268009081850267001
g = 223
h = 1009660566883490917987475170194560289062628664411983200474597006489640893063715494610197294704009188265361176318190659133132869144519884282668828418392494875096149757008157476595873791868761173517

# 1. p-1 の因数分解
factors = factorint(p - 1)

# 中国剰余定理を「逐次代入」で実現する関数
def manual_crt(remainders, moduli):
    """
    x ≡ r1 (mod m1), x ≡ r2 (mod m2) ... を逐次的に解く
    """
    x = remainders[0]
    m = moduli[0]
    for i in range(1, len(remainders)):
        r_i = remainders[i]
        m_i = moduli[i]
        # x + k * m ≡ r_i (mod m_i) を満たす k を求める
        # k * m ≡ r_i - x (mod m_i)
        inv_m = pow(m, -1, m_i)
        k = ((r_i - x) * inv_m) % m_i
        x = x + k * m
        m = m * m_i
    return x

remainders = []
moduli = []

# 2. 各素因数について解く
for q, e in factors.items():
    qe = q**e
    # 提示された Lifting 法、あるいは discrete_log を使用
    # gi = g^((p-1)/qe), hi = h^((p-1)/qe)
    gi = pow(g, (p - 1) // qe, p)
    hi = pow(h, (p - 1) // qe, p)
    
    xi = discrete_log(p, hi, gi)
    remainders.append(xi)
    moduli.append(qe)
    print(f"Solved for {q}^{e}: {xi}")

# 3. 独自のCRT合成
x = manual_crt(remainders, moduli)

print(f"\nFinal x: {x}")
try:
    print(f"Flag: {long_to_bytes(int(x)).decode()}")
except:
    print("Decoding failed. Check the integer value.")