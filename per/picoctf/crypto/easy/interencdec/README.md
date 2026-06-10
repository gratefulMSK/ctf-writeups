# 問題

>Description<br>
>Can you get the real meaning from this file.

説明<br>
このファイルから本当の意味を読み取ることができますか？

# 解法要約
base64、シーザー、勝ち

# 解法
ファイルに書いてあるのは以下<br>
"cvpbPGSYidkM0JxZGtwQlRYdHFhR3g2YUhsZmF6TnFlVGwzWVROclgyMHdNakV5TnpVNGZRPT0nCg=="

見ると明らかに base64 であるため cyberchef でデコード<br>
するとそれも明らかに base64 であるためデコード<br>
すると見たらシーザーっぽいから回して 19番目でフラグゲット

シーザーしてフラグゲット


# 解答
picoCTF{caesar_d3cr9pt3d_f0212758}
