# 問題

>Description<br>
>A message was encrypted using a shared secret... but it looks like one side of the exchange leaked something. Can you piece together the secret and get the flag?

説明<br>
メッセージが共有秘密鍵を使って暗号化されましたが、どうやら通信の一方の側で何かが漏洩したようです。秘密鍵を解読してフラグを入手できますか？

# 解法要約
ディッフィー・ヘルマンの鍵共有、勝ち

# 解法

ソースを見るとどう考えても Diffie-Hellmanの鍵共有<br>
でメッセージを見ると初期に決める秘密鍵 b を出力してしまっている

そして A も出力しているため共有鍵もわかるし xor するだけ<br>
同封した de.py を実行してフラグゲット

因みに最終的に共有鍵が mod 256 されることを利用して、 256通り全て試す de2.py でもフラグは得られる




### Diffie-Hellmanの鍵共有 (DH法)
二人の通信がどんなに公開されていても共有鍵を作ることができる方法<br>
二人は秘密鍵である指数 a, b をそれぞれ作る<br>
二人は公開してもよい底となる g と 素数 p を作って共有する

$A := (g)^a \pmod{p}$<br>
$B := (g)^b \pmod{p}$

二人は公開してもよい A, B を共有する

$K := (A)^b \pmod{p} = (B)^a \pmod{p}$

計算すると同じ値 K がでる<br>
これを共有鍵とする

これは公開された情報だけでは理論上解くことが難しいとされている


# 解答
picoCTF{dh_s3cr3t_1bcf19a9}