# 概要 (Summary)
<img src="images/sum.png" width=300>
<br><br><br>

# 観察・解析 (Analysis)
### 配布

- lcg.txt 

### 考えたこと
lcg.txtの中身は
- 式が一つ
- $m$ の値
- $x_1$ ~ $x_4$ の値
- $x_5$ をkeyとしてflagとxorした後の値

式は以下、

$$
x_{n+1} = (a \cdot x_n + c) \pmod m
$$

式を見ると線形のなんちゃらっぽい<br>
$`m`$ が $`10^9`$ だったら全通り試せば行けるか？<br>
やってみると2時間かかりそうで断念

# 解法 (Exploit)
<br>

$$
\begin{aligned}
x_{n+1} = (a \cdot x_n + c) \pmod m \\
A, B, M \in \text{constants} \quad (M > A > 0, \ M > B \ge 0)
\end{aligned}
$$

<br>

これで表されたような式を用いた疑似乱数生成方法を線形合同法という。

線形合同法はいくつかの要素が分かれば予測することが可能となる。
今回の場合では以下の方法で $`a, c`$ が分かる。

$$
\begin{aligned}
x_2 &\equiv (a \cdot x_1 + c) \pmod m &&&& \text{(1)} \\
x_3 &\equiv (a \cdot x_2 + c) \pmod m &&&& \text{(2)}
\end{aligned}
$$

(2) - (1) すると

$$
\begin{aligned}
x_3 - x_2 &\equiv a(x_2 - x_1) \pmod m
\end{aligned}
$$

ここで、 $`\Delta x_n = x_{n + 1} - x_n`$ とすると

$$
\begin{aligned}
\Delta x_2 &\equiv a \cdot \Delta x_1 \pmod m \\
a &\equiv \Delta x_2 \cdot (\Delta x_1)^{-1} \pmod m
\end{aligned}
$$

また、(1)より

$$
\begin{aligned}
c &\equiv x_2 - a \cdot x_1 \pmod m
\end{aligned}
$$


つまり、 $`\Delta x_1`$ の逆元を求まれば $`a, c`$ が求まる。

今回、 $`m`$ の値は $`2^{32}`$ であり、$`\Delta x_1`$ は奇数であった。これより、二つの値が互いに素なため逆元が求まることが分かる。逆元はPythonのpow関数で求まり、上記の式にそれぞれの値を当てはめ、Flagを求めたコードがsolve.pyである。

# 旗 (Flag)
utflag{pr3d1ct_th3_futur3_lcg}

# 関連用語
LCG Parameter Reconstruction (LCGパラメータ復元)
- 既知の出力から $`a`$ と $`c`$ を特定する攻撃の総称