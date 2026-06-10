# 問題

>Description<br>
>Kishor Balan tipped us off that the following code may need inspection:

説明<br>
キショール・バラン氏から、以下のコードに検査が必要になる可能性があるとの情報が寄せられました。

# 解法要約
デベロッパーツール、ソースタブ、勝ち

# 解法
タイトル的にはデベロッパーツールを使いそう<br>
サイトを見ると

```Text
I used these to make this site:
HTML
CSS
JS (JavaScript)
```

サイト作ったよとしか言ってないからデベロッパーツールを見てみる<br>
domで `<!-- Html is neat. Anyways have 1/3 of the flag: picoCTF{tru3_d3 -->` を発見<br>
他の二つはCSS, JSっぽいぞ

cssより
```css
/* You need CSS to make pretty pages. Here's part 2/3 of the flag: t3ct1ve_0r_ju5t */
```

jsより
```js
/* Javascript sure is neat. Anyways part 3/3 of the flag: _lucky?302945a7} */
```

よってフラグは結合して `picoCTF{tru3_d3t3ct1ve_0r_ju5t_lucky?302945a7}`

# 解答
picoCTF{tru3_d3t3ct1ve_0r_ju5t_lucky?302945a7}