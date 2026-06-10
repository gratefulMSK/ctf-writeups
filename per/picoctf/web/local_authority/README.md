# 問題

>Description<br>
>Can you get the flag?

説明<br>
旗を入手できますか？

# 解法要約
ネットワーク、secure.js、勝ち

# 解法
認証はできるけど適当なアカウントでログインすらできない<br>
クッキーも存在しない<br>
ソースにもヒントはなさそう

認証方法を知りたいからデベロッパーツールのネットワークからログイン時の様子を見る<br>
`/secure.js` が走っていたので見ると

```js
function checkPassword(username, password)
{
  if( username === 'admin' && password === 'strongPassword098765' )
  {
    return true;
  }
  else
  {
    return false;
  }
}
```

ログイン情報を記入してフラグゲット


# 解答
picoCTF{j5_15_7r4n5p4r3n7_b0c2c9cb}
