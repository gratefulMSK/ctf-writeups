
# 問題

>Description<br>
>Can you get the flag?

説明<br>
フラグを取得できますか？

# 解法要約
css、js、勝ち

# 解法
見ると長い文章
>On Includes<br>
>Many programming languages and other computer files have a directive, often called include (sometimes copy or import), that causes the contents of a second file to be inserted into the original file. These included files are called copybooks or header files. They are often used to define the physical layout of program data, pieces of procedural code and/or forward declarations while promoting encapsulation and the reuse of code.<br>
>Source: Wikipedia on Include directive

インクルードについて<br>
多くのプログラミング言語やその他のコンピュータファイルには、インクルード（コピーまたはインポートと呼ばれることもあります）と呼ばれるディレクティブがあり、これによって別のファイルの内容を元のファイルに挿入します。これらのインクルードされたファイルは、コピーブックまたはヘッダーファイルと呼ばれます。これらは、プログラムデータ、手続き型コード、および/または前方宣言の物理的なレイアウトを定義するためによく使用され、カプセル化とコードの再利用を促進します。

出典：Wikipediaのインクルードディレクティブに関する記事

以上Google翻訳より

この長い文章の下に say hello と書かれたボタンがあって押すとアラートが出てきたのでソースを見てみる

html には js の参照が書かれていたので js の方をみると
```js
function greetings()
{
  alert("This code is in a separate file!");
}

//  f7w_2of2_6edef411}
```

ということで、 css をみると
```css
body {
  background-color: lightblue;
}

/*  picoCTF{1nclu51v17y_1of2_  */
```
ということでフラグゲット


# 解答
picoCTF{1nclu51v17y_1of2_f7w_2of2_6edef411}