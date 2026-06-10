# 問題

>Description<br>
>I have these 2 images, can you make a flag out of them?<br>
>scrambled1.png scrambled2.png

説明<br>
この2枚の画像から国旗を作ってもらえますか？<br>
scrambled1.png scrambled2.png

# 解法要約
画像のadd、勝ち

# 解法

scramble1.png, scramble2.png の二つが配布される<br>
名前が scramble であることから add とかの合成の類とは予想できる

de.py が pixel ごとに足してくれるコード

※因みに画像分析ツールの "うさ耳ハリケーン" の "あおぞらしろねこ" とか使うとコードも必要ない

### 失敗
自分は画像を読み込むとき以下のようにして失敗した

```
# 画像を読み込む
img1 = Image.open('scrambled1.png').convert('L')
img2 = Image.open('scrambled2.png').convert('L')
```

正解は `convert('RGB')` であり、RGB として使うべきが L (Luminance = 輝度) として扱った

# 解答
picoCTF{bcdf93c3}
