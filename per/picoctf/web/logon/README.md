# 問題

>Description<br>
>The factory is hiding things from all of its users.<br>
>Can you login as Joe and find what they've been looking at?

説明<br>
工場は全ユーザーから情報を隠している。<br>
ジョーとしてログインして、彼らが何を見ているのか突き止めてくれないか？

# 解法要約
ログイン、クッキー、勝ち

# 解法
問題より、Joeでログインすればいい<br>
適当にログインできるがflagは見せてくれない

ソースコードに怪しいものはない<br>
クッキー見てみると

* username
* password
* admin (bool値)

があった

username を 'Joe' に、 admin を True にしてリロード<br>
フラグゲット

因みに admin = True にするだけで行けた

# 解答
picoCTF{th3_c0nsp1r4cy_l1v3s_4d184b0d}