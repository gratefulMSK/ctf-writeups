# 問題

>Description<br>
>Do you know how to use the web inspector?


説明<br>
ウェブインスペクターの使い方をご存知ですか？

# 解法要約
html、base64、勝ち

# 解法

ページは3つ
* index.html
* about.html
* contact.html

問題文でインスペクターを言及してるからデベロッパーツールを見ると about.html に以下

``` html
<section class="about" notify_true="cGljb0NURnt3ZWJfc3VjYzNzc2Z1bGx5X2QzYzBkZWRfMWY4MzI2MTV9">
   <h1>
    Try inspecting the page!! You might find it there
   </h1>
   <!-- .about-container -->
</section>
```

とにかく `notify_true="cGljb0NURnt3ZWJfc3VjYzNzc2Z1bGx5X2QzYzBkZWRfMWY4MzI2MTV9"` があやしい上に、base64っぽいのでデコードする<br>
フラグゲット


# 解答
picoCTF{web_succ3ssfully_d3c0ded_1f832615}