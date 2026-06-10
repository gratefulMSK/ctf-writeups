# 問題

None

なし

# 解法要約
burp、ボディのotp消す、勝ち

# 解法
タイトルが burp への導入だからburpで見てみる<br>
登録 -> otp (ワンタイムパスワード) 入力 -> invalid<br>
ヘッダーにもソースにも違和感は存在しない

burp で見ると POST メソッドのボディで `opt=1234` と書いている<br>
これを消して送るとフラグゲット

※このときヘッドとボディの間に1行空行を挟まないとプロトコルとして成り立たず送れない

因みに otp を消して攻撃が通る例を gem 君が作った

```python 
otp = request.form.get('otp')

if otp is not None:
    # 項目がある時だけチェックする（親切設計のつもり）
    if otp == "12345":
        return "SUCCESS"
    else:
        return "Invalid OTP"

# 項目がない（None）ときは、チェックを「スルー」して下に進んじゃう
# その先に Flag を表示する処理があったら...
return render_template("flag.html")
```

本来 otp に None が入るとクラッシュを起こすため例外処理するが、その例外処理だけ書かずにクラッシュも起こさないコードになっていたと推測

因みに burp を使わずとも
``` bash
$ curl -X POST http://titan.picoctf.net:52590/dashboard -H "Cookie: session=.eJw......0dg"

Welcome, a you sucessfully bypassed the OTP request.
Your Flag: picoCTF{#0TP_Bypvss_SuCc3$S_3e3ddc76}
```
curl はセッション付けて POSTメソッドで行けば、ボディのないリクエストを送りフラグを得れる<br>
つまり、一応 cli でも理論上行ける

# 解答
picoCTF{#0TP_Bypvss_SuCc3$S_3e3ddc76}