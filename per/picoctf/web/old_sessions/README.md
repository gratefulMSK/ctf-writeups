# 問題

> Description<br>
> Proper session timeout controls are critical for securing user accounts. If a user logs in on a public or shared computer but doesn’t explicitly log out (instead simply closing the browser tab), and session expiration dates are misconfigured, the session may remain active indefinitely.<br>
> This then allows an attacker using the same browser later to access the user’s account without needing credentials, exploiting the fact that sessions never expire and remain authenticated.

説明<br>
適切なセッションタイムアウト制御は、ユーザーアカウントのセキュリティを確保する上で非常に重要です。ユーザーが公共のコンピュータや共有コンピュータにログインした後、明示的にログアウトせず（単にブラウザのタブを閉じるだけの場合）、セッションの有効期限が正しく設定されていない場合、セッションは無期限にアクティブなままになる可能性があります。<br>
これにより、攻撃者は同じブラウザを後から使用する際に、認証情報なしでユーザーのアカウントにアクセスできてしまいます。これは、セッションが期限切れにならず、認証状態が維持されるという脆弱性を悪用したものです。

# 解法要約

アクセス、登録、ログイン、/sessionsにいく、クッキー変更

# 解法
とりあえずアクセス

登録とログインができるのでログインすると掲示板があった<br>
そのなかで怪しいメッセージが...

``` Text
mary_jones_8992
2024-2-20 14:50
Hey I found a strange page at /sessions
```

urlに/sessionsをついかしてみると

``` js
1) session:X3icQ88KQnFsouhc2MhKEjOxg5vZP6EYgG5Sv9gehG4, {'_permanent': True, 'key': 'admin'}

2) session:NANzyWlE-wfg7ogBj189-VK-tagSaDNAk8f_19ciw0I, {'_permanent': True, 'key': 'a'}
```

なぜかセッション情報があった<br>
因みにaというユーザーは自分<br>
セッション情報については最後に<br>

adminに行けば何かありそうだからデベロッパーツール > Application > クッキーからsessionを変更

``` Text
Welcome admin
picoCTF{s3t_s3ss10n_3xp1rat10n5_ed8964c2}
```

※セッションについて<br>
セッション情報は公開しないが存在することはある<br>
サーバー側で保存していてそれを表示するページは意図的に作らない限り存在しない

# 解答
picoCTF{s3t_s3ss10n_3xp1rat10n5_ed8964c2}