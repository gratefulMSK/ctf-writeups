# 問題

>Description<br>
>What if d is too small?

説明<br>
dが小さすぎる場合はどうなる？

# 解法要約
wiener's attack、勝ち

# 解法

配布ファイルはなし、インスタンスサーバーのみ<br>
インスタンスサーバーに通信すると N, e, c が渡される

さてここで注目しないといけないことが e がいつもの 65537 ではなく、N と同じくらいでかいということである

今回の問題は wiener's attack の典型的な問題である<br>
wiener's attack の説明は下記に記した

wiener's attack より、 $ \frac{e}{N} $ の主近似分数を列挙して 各分母を d と仮定し復号を行う探索を行えばフラグゲット

※因みに問題名はダックスフントの攻撃であるが、英語圏でダックスフントは wiener dog ともよばれるそう

### 連分数
※ここから数学の話になりますが、詳しくはやりませんし、用語が定義に則っていない場合があります<br>
wiener's attack を説明するためです

wiener's attack の前にまず連分数の話をする

連分数とは以下の形である

```math
a_0 + \frac{1}{a_1 + \frac{1}{\cdots + \frac{1}{a_n}}}
```

連分数の性質として、任意の有理数は連分数で表すことができるという性質がある<br>
また、$ \{a_0, a_1, ..., a_n\} $ に対してこれの k 番目までの数列 $ \{a_0, a_1, ..., a_k\} (k < n) $ で表した連分数をもとの有理数の主近似分数という


```math
a_0 + \frac{1}{a_1 + \frac{1}{\cdots + \frac{1}{a_k}}}
```

wiener's attack ではこの主近似分数の性質を用いて d を特定する

### wiener's attack とは

wiener's attack とは

```math
d < \frac{1}{3} \sqrt[4]{N}
```

これを満たすときに d を抽出する攻撃である

wiener's attack では連分数におけるルジャンドルの定理から出発する<br>
ルジャンドルの定理は以下である

ある実数 x に対して、
```math
\bigg\vert x - \frac{a}{b} \bigg\vert < \frac{1}{2b^2}
```
を満たす有理数 a/b は x の主近似分数である

ここで RSA における d の関係式を見る

```math
\begin{align}
ed &\equiv 1 \quad (mod \; \phi(N) \,) \\
ed &= k \cdot \phi(N) + 1 \\
\frac{e}{\phi(N)} &= \frac{k}{d} \bigg(1 + \frac{1}{k \cdot \phi(N)}\bigg) \\
\frac{e}{N} &= \frac{k}{d} \bigg(\frac{\phi(N) + \frac{1}{k}}{N}\bigg) \\
&= \frac{k}{d} \bigg(\frac{(p - 1)(q - 1) + \frac{1}{k}}{N}\bigg) \\
&= \frac{k}{d} \bigg(\frac{N - p - q + 1 + \frac{1}{k}}{N}\bigg) \\
\frac{e}{N} &= \frac{k}{d} \bigg(1 - \frac{p + q - 1 - \frac{1}{k}}{N}\bigg) \\
\end{align}
```

RSA の原理を知っていればこの式変形は追えるはず

(7)式の左辺は公開鍵 n, e の二つから計算できる<br>
右辺の括弧の中の第二項は p, q が大体 $ \sqrt{N} $ の大きさである<br>
このことから (7)式は k / d を公開鍵のみからなる e / N で近似できることを示している

さて、これを先ほどのルジャンドルの定理の条件式に当てはめる<br>
x = e / N, a / b = k / d を代入すると

```math
\begin{align}
\bigg\vert \frac{e}{N} - \frac{k}{d} \bigg\vert &< \frac{1}{2d^2}\\
\frac{k}{d} \cdot \frac{p + q - 1 - \frac{1}{k}}{N} &< \frac{1}{2d^2}
\end{align}
```

つまり、(9)式が条件を満たすとき、ルジャンドルの定理より k / d は e / N の主近似分数であり、主近似分数を全探索すれば必ず k / d が現れることをさす

さて、(9)式をもう少しについてもう少し式変形を行う

まず、一般的な RSA では p, q の MSB (most significant bit : 最上位ビット) は同じであり、p + q が最大となるのは p = 2q に限りなく近い時である<br>
$ p = 2q $ とすると、
```math
\begin{align}
N &= p \cdot q = 2q^2 \\
q &= \sqrt{\frac{N}{2}} \\
p &= 2q = \sqrt{2N} \\
p + q &= \sqrt{\frac{N}{2}} + \sqrt{2N} = \frac{3}{\sqrt{2}} \sqrt{N}
\end{align}
```

つまり、$ p + q < \frac{3}{\sqrt{2}} \sqrt{N} $

そして、一般的な RSA は以下を満たす

```math
e, d < \phi(N) < ed = k \cdot \phi(N) + 1
```

$ e < \phi(N) $ と $ ed = k \cdot \phi(N) + 1 $ より $ k < d $ が導き出せる

最後に自明に $ 0 < \frac{1}{k} $ である

この三つの条件式より (9)式を変形すると

```math
\begin{align}
\frac{k}{d} \cdot \frac{p + q - 1 - \frac{1}{k}}{N} &< \frac{d}{d} \cdot \frac{\frac{3}{\sqrt{2}} \sqrt{N}}{\sqrt{N} \cdot \sqrt{N}} = \frac{3}{\sqrt{2}\sqrt{N}} \\
\frac{3}{\sqrt{2} \sqrt{N}} &< \frac{1}{2d^2} \\
d^2 &< \frac{1}{3\sqrt{2}} \sqrt{N} \\
d &< \frac{1}{\sqrt{3\sqrt{2}}} \sqrt[4]{N} \, \fallingdotseq 0.485 \sqrt[4]{N}
\end{align}
```

これを満たすときルジャンドルの定理の条件を満たし、d を主近似分数を列挙することにより求めることができることが証明できた<br>

また、一般的に wiener's attack は以下の条件式でよく表される

```math
d < \frac{1}{3} \sqrt[4]{N}
```

※因みにこの wiener's attack は RSA の通信システムがしっかりと普及する前に数学的に見つかっているためこれによる事件はほとんどない<br>
※対策は以下が効く
* e を小さくすること : $ \phi(N) < ed $ より e が小さければ d は小さくなれない
* crt-rsa を使う : 元々 d を小さくする理由は復号処理を軽くすることだったが crt-rsa は d を小さくせずにそれを叶える
* $e + t \cdot \phi(N)$ を公開鍵 e とする : $\phi(N)$ の整数倍を e に足しても $ ed = 1 \quad (mod \; \phi(N))$ は変わらないため d の値は変わらないが、$e < \phi(N)$ の前提が崩れるため wiener's attack はできなくなる

# 解答
picoCTF{proving_wiener_2ab2814}
