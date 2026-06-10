# 問題

>Description<br>
>This service provides you an encrypted flag. Can you decrypt it with just N & e?

説明<br>
このサービスは暗号化されたフラグを提供します。Nとeだけでそれを復号できますか？

# 解法要約
p = 2、勝ち

# 解法
RSA は理解している前提で話を進める

通信してみる<br>
普通に e と N と暗号文だけもらった<br>
さてどうするか...

python の暗号化のコードも配られてるから見てみる<br>
 ↓ 以下一部
``` python
from setup import get_primes

e = 65537

def gen_key(k):
    """
    Generates RSA key with k bits
    """
    p,q = get_primes(k//2)
    N = p*q
    d = inverse(e, (p-1)*(q-1))

    return ((N,e), d)
```

get_primes とかいう知らない関数が使われている<br>
それ以外は安全な RSA っぽい

from setup は自作ライブラリから持ってくるという意味だから、 get_primes 関数がなんなのかは予測するしかない

もう一度通信を見てみると N が必ず偶数になっていた<br>
片方の素数 p = 2 が確定なので q も計算可能<br>
よってフラグゲット

デクリプトファイル (de.py) は添付済み

# 解答
picoCTF{tw0_1$_pr!m341c6ed35}