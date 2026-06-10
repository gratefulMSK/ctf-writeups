# 問題

>Description<br>
>A company stored a secret message on a server which got breached due to the admin using weakly hashed passwords. Can you gain access to the secret stored within the server?

説明<br>
ある企業がサーバーに秘密メッセージを保存していましたが、管理者が脆弱なハッシュ化パスワードを使用していたためにサーバーが侵害されました。サーバーに保存されている秘密情報にアクセスできますか？

# 解法要約
hashcat、勝ち

# 解法
ハッシュ化をしているらしいので hashcat を試す<br>
nc で通信すると hash化されたコードが渡されるので以下を行う

※ 因みに 3行目の hashcat の最後 --force は僕の環境依存で本来必要ない
``` shell
$ hashid -m 482c811da5d5b4bc6d497ffa98491e38
$ echo "482c811da5d5b4bc6d497ffa98491e38" > target.txt
$ hashcat -a 0 -m ハッシュ関数の番号 target.txt SecLists/Passwords/Leaked-Databases/rockyou.txt --force
```
関数の説明は後で<br>
これを 3回やると

* 482c811da5d5b4bc6d497ffa98491e38 : password123 (MD5)
* b7a875fc1ea228b9061041b7cec4bd3c52ab3ce3 : letmein (SHA-1)
* 916e8c4f79b25028c9e467f1eb8eee6d6bbdff965f9928310ad30a8d88697745 : qwerty098 (SHA-256)

が分かるのでフラグゲット

### 辞書型攻撃について
要するにブルートフォース (総当たり攻撃) である<br>
hash関数は一方向性があるため、 hash値から平文を予測はできない<br>
しかし hash関数は中身が公開されているため、あらかじめパスワードになりそうな平文を全部試しておいて一致するものを探せばよいというのが辞書型攻撃

それを計算してくれるのが hashcat というツール<br>
それの元のワードリストが seclists<br>
各自、 rockyou.txt などをダウンロードしてみるとよい

### 関数の説明
```
hashid -m hash値
```
これをすると hash値 が何のハッシュ関数を使われているかが分かる<br>
-m をつけると hashcat -m の後に書く数字もわかる<br>
MD5 は 0, SHA-1 は 100, SHA-256 は 1400

```
echo "hash値" > ファイル名1.txt
```
テキストファイルに hash値 を保存

```
hashcat -a 0 -m ハッシュ関数の番号 ファイル名1.txt ファイル名2.txt
```
ファイル名2.txt はワードリスト<br>
なんか GPU が使えなかったので私は --force を使って CPU を使った<br>
もし既に探索済みのワードは --show を最後につけると表示してくれる


# 解答
picoCTF{UseStr0nG_h@shEs_&PaSswDs!_4c95d69f}