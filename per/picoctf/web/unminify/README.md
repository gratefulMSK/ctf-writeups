# 問題

>Description<br>
>I don't like scrolling down to read the code of my website, so I've squished it. As a bonus, my pages load faster!

説明<br>
ウェブサイトのコードを読むためにスクロールダウンするのが嫌だったので、コードを圧縮しました。おまけに、ページの読み込み速度も速くなりました！

# 解法要約
デベロッパーツール、html、勝ち

# 解法
ページを踏むとある文章

>Welcome to my flag distribution website!<br>
>If you're reading this, your browser has succesfully received the flag.<br>
>I just deliver flags, I don't know how to read them...

私の旗配布ウェブサイトへようこそ！<br>
この文章が読めているということは、あなたのブラウザは旗を正常に受信しました。<br>
私は旗を配布するだけで、読み方は知りません…。

ということで html を見ると以下を発見

```html
<div class="picoctf{}" style="width:70%">
  <p class="picoctf{}">If you're reading this, your browser has succesfully received the flag.</p>
  <p class="picoCTF{pr3tty_c0d3_d9c45a0b}"></p>
  <p class="picoctf{}">I just deliver flags, I don't know how to read them...</p>
</div>
```

フラグゲット


# 解答
picoCTF{pr3tty_c0d3_d9c45a0b}