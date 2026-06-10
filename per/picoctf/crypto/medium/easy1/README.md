# 問題

>Description<br>
>The one time pad can be cryptographically secure, but not when you know the key. Can you solve this?<br>
>We've given you the encrypted flag, key, and a table to help UFJKXQZQUNB with the key of SOLVECRYPTO. Can you use this table to solve it?.

説明<br>
ワンタイムパッドは暗号学的に安全ですが、鍵を知っていればそうではありません。これを解けますか？<br>
暗号化されたフラグ、鍵、そしてSOLVECRYPTOの鍵を解くための表をUFJKXQZQUNBに提供します。この表を使って解けますか？

# 解法要約
ヴィジュネル暗号、勝ち

# 解法

配布ファイルは 1つのテキストファイル<br>
見るとヴィジュネル暗号のテーブルである

では、ヴィジュネル暗号をするとして暗号文と鍵が欲しいがどこであろうか<br>
問題文を見るとこれ見よがしに大文字の `UFJKXQZQUNB`, `SOLVECRYPTO` があった

よってフラグゲット

# 解答
picoCTF{CRYPTOISFUN}
