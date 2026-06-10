# 問題

>Description<br>
>A message has been encrypted using RSA. The public key is gone… but someone might have been careless with the private key. Can you recover it and decrypt the message?

説明<br>
RSA暗号で暗号化されたメッセージがあります。公開鍵は失われてしまいましたが、秘密鍵は誰かが不注意で保管していた可能性があります。秘密鍵を復元してメッセージを復号化できますか？

# 解法要約
exiftoolコマンド、echo、openssl、勝ち

# 解法

くそ問<br>
というより知らないと解けない問題<br>
考えるだけ無駄だから答え見て褒められるレベル

二つのコードが配られる
* flag.enc
* image.jpg

flag.enc はよくわからない bin ファイル<br>
image.jpg は鍵の写真であった<br>
image.jpg に何の情報もないわけがない、かつ、タイトルが steganography からきているため exiftool で見てみる

``` shell
exiftool image.jpg
```

するとコメントに激なが文章、しかも hex っぽい<br>
どんなのか見たいから txtファイルに保存
```
echo "hex をコピペ" | xxd -r -p > word.txt
```
xxd はバイナリを 16進数で出力するもので、 `-r`オプションは逆に 16進数からバイナリに、 `-p`オプションは余計な ascii や座標などを除いたプレーンテキストで出力

すると pem形式のデータが出力された<br>
このファイルの拡張子を .pem に変更し、
``` shell
openssl pkeyutl -decrypt -inkey private.pem -in flag.enc
```
でフラグゲット

### 戒め
絶対に pemファイルから愚直に p, q　をだそうとか思わないこと<br>
なぜならめんどくさいし、それで時間をかけるのが馬鹿みたいだから<br>
それを望む人なら良し

### pemファイルについて
rsa はそもそも現代の通信システムでも使われている<br>
特に TLS/SSLプロトコルではその暗号化・復号を行うため、フォーマットが存在する<br>
その一つが pem形式・ pemファイルである<br>

pemファイルには秘密鍵・公開鍵などの情報が含まれ、このファイルと暗号化・復号したいデータを opensslツールにぶち込めば勝手に計算してくれる

# 解答
picoCTF{rs4_k3y_1n_1mg_ce170c3d}