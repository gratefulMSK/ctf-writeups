# 問題

>Description<br>
>There is some interesting information hidden around this site. Can you find it?

説明<br>
このサイトには興味深い情報がいくつか隠されています。見つけられますか？

# 解法要約
HTML、CSS、JS、robots.txt、.htaccess、.DS_Store、勝ち

# 解法
静的サイトだからソース見て、 HTML に一つ目のフラグ<br>
```html
<!-- Here's the first part of the flag: picoCTF{t -->
```

CSS 見ると二つ目、三つめは js と期待した<br>
```css
/* CSS makes the page look nice, and yes, it also has part of the flag. Here's part 2: h4ts_4_l0 */
```

js にはよくわからない文章があった<br>
```js
/* How can I keep Google from indexing my website? */
```
「google が私のサイトを検索しないようにするにはどうすればいい？」と書いてある<br>
そんなの robots.txt に決まってる

```Text
# Part 3: t_0f_pl4c
# I think this is an apache server... can you Access the next flag?
```

次のヒントはこのサーバーが apache サーバーであること<br>
apache サーバーは各ディレクトリに `/.htaccess` があるらしい
```Text
# Part 4: 3s_2_lO0k
# I love making websites on my Mac, I can Store a lot of information there.
```

次のヒントは Mac、そしていっぱい情報がそこにあるとのこと<br>
Mac はディレクトリを開くと `/.DS_Store` というファイルができて、そこにディレクトリの情報が書き込まれる (バイナリ)
```Text
Congrats! You've completed the scavenger hunt! Part 5: _9588550}
```

フラグゲット

因みに、 `/.htaccess` はディレクトリのリクエスト制限やリダイレクト、エラーメッセージなどをかけるもの<br>
物によればここで好きなコマンドを実行できるが、基本はテキストで意味はない

`/.DS_Store` は本来そこにあるべきでなく、間違えてアップロードした、gitignoreし忘れた、などをしないと存在しない<br>
アップロードする必要が一切ないもの

# 解答
picoCTF{th4ts_4_l0t_0f_pl4c3s_2_lO0k_9588550}