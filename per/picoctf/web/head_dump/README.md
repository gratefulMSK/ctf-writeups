# 問題

>Description<br>
>Welcome to the challenge! In this challenge, you will explore a web application and find an endpoint that exposes a file containing a hidden flag.<br>
>The application is a simple blog website where you can read articles about various topics, including an article about API Documentation. Your goal is to explore the application and find the endpoint that generates files holding the server’s memory, where a secret flag is hidden.

説明<br>
チャレンジへようこそ！このチャレンジでは、Webアプリケーションを探索し、隠されたフラグを含むファイルを公開するエンドポイントを見つけ出します。<br>
このアプリケーションは、APIドキュメントに関する記事など、さまざまなトピックの記事を読むことができるシンプルなブログサイトです。あなたの目標は、アプリケーションを探索し、サーバーのメモリに格納されたファイルを生成するエンドポイントを見つけることです。そのファイルには、秘密のフラグが隠されています。

# 解法要約
api-docs、/heapdump、直書き、勝ち

# 解法

ページみていろいろいじると1つ怪しいページに遷移した<br>
`/api-docs/` という場所で swagger というツールセットを使っていると出てくるデフォルトページ、詳しくは最後に<br>
普通に情報漏洩のページなので設定で非公開にすべきページ

問題文に従うとメモリに関する何かをしているエンドポイントを見つけて、その中を見ればいい<br>
`/api-docs/` を見ていると下に `/heapdump` でダウンロードできるものが存在しそうとわかる<br>
この `/heapdump` についても最後に

url を `/heapdump` にすると勝手にダウンロードされ、その中を見ると json形式で長い文章が書かれている

"picoCTF{" で検索すると直書きされていてフラグゲット

### "/api-docs/" について
swagger というツールセットを使ったりするとできてしまうパス<br>
ここには何というパスで何メソッドで行けばなにができるか、というパスの説明書みたいなのが書いている

本来デバッグ用でしかないし、公開損だが、デフォルトが公開設定になっている場合があるらしい

### "/heapdump" について
`/heapdump` ではサーバー側のプログラムが今使っているメモリを json形式にして出力する<br>
デバックとしてはサーバーのメモリ管理をするときなどに使う

vue などで spa (single page application) を作るときなどは画面遷移が起こらないため、メモリの使い過ぎによるクラッシュなどの防止にメモリ管理をしなければいけない

apiキーなどの環境変数も含んでいるため、絶対に公開してはいけない<br>
デフォルトでは非公開設定のはず

因みに、デベロッパーツールのメモリタブからヒープスナップショットをダウンロードできるが、<br>
こいつはブラウザのこのサイトで使ってるメモリの情報である

### wappalyzer から推測できるパス
gem 君が作ってくれたから載せておく
| 検出された技術 | 推測されるライブラリ | 期待できるパス（例） |
| :--- | :--- | :--- |
| Java (Spring Boot) | SpringDoc / SpringFox | `/v3/api-docs`, `/swagger-ui.html` |
| Python (FastAPI) | (標準機能) | `/docs`, `/redoc`, `/openapi.json` |
| Python (Flask) | Flasgger | `/apidocs/` |
| Node.js (Express) | swagger-ui-express | `/api-docs`, `/swagger` |
| PHP (Laravel) | L5-Swagger | `/api/documentation` |
| Go (Gin/Echo) | swaggo | `/swagger/index.html` |


# 解答
picoCTF{Pat!3nt_15_Th3_K3y_546786ba}