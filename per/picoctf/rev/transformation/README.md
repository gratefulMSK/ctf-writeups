# 問題

>Description<br>
>I wonder what this really is...
>enc ''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])

説明<br>
これは一体何なんだろう…<br>
enc ''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])

# 解法要約
utf-16BE、その逆、勝ち

# 解法

問題文のエンコードは UTF-16 にしているコードである<br>
ちなみに UTF-16 は Unicode を 2バイトで表す方法で、リトルエンディアン（LE）、ビッグエンディアン（BE）の二通りがあり、今回は BE であった<br>

ならば enc に書いてあるものが UTF-16 だ...と思うと実は違う<br>
実は enc ファイルに書き出すとき（おそらく作者が）、UTF-8 として書き出している<br>
そのため、これはビットから求めることはできない

python の文字列型は Unicode なのでそこを始点とすればよい
それを de.py に書いた、実行してフラグゲット

## 他の解法

解法 append - 1

以下をターミナルで実行
``` bash
python3 -c "print('灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸形㝦㘲捡㕽'.encode('utf-16-be').decode('utf-8'))"
```

解法 append - 2

cyberchef にて "Encode Text" の "UTF-16BE(1201)" を入れる

# 解答
picoCTF{16_bits_inst34d_of_8_b7f62ca5}
