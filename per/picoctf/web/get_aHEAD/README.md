# 問題

>Description<br>
>Find the flag being held on this server to get ahead of the competition

説明<br>
このサーバーで保持されている旗を見つけて、競争相手より優位に立ちましょう。

# 解法要約
HEAD メソッド、勝ち

# 解法
くそ問、嘘、反省

タイトルを見ると aHEAD とあり不自然<br>
中を見ると背景色を赤と青にするか行き来するだけ

デベロッパーツールで中を見ると、 GET メソッドで赤、 POST メソッドで青色になる

ということで HEAD メソッドを送りましょう<br>
フラグゲット

因みに `curl -I http://...` は自動で HEAD メソッドを送る仕様

### HEAD メソッドとは
HEAD メソッドとは GET メソッドからボディを抜いてヘッダーのみにしたもの<br>
普通は...

今回の場合 HEAD メソッドが来たら違うものを送るようになっている<br>
だから GET メソッドのヘッダーを見るだけだといつまでもたどり着けなかった

# 解答
picoCTF{r3j3ct_th3_du4l1ty_8b13f07}