# 問題

>Description<br>
>We found a brand new type of encryption, can you break the secret code? (Wrap with picoCTF{})<br>
>fegdeogdgecoeocgcgchcfcffccfca new_caesar.py

説明<br>
全く新しいタイプの暗号化を発見しました。秘密のコードを解読できますか？（picoCTF{}で囲んでください）<br>
fegdeogdgecoeocgcgchcfcffccfca new_caesar.py

# 解法要約
bit的なシーザー暗号、key が1文字、全探索、勝ち

# 解法

配布ファイルは 1つの pythonファイル、インスタンスサーバーはなし<br>
配布ファイルを見ると 16文字版のヴィジュネル暗号みたいなことをしていた (そう聞くと弱そう)

さて、注目すべき場所は以下
```python
ALPHABET = string.ascii_lowercase[:16]

...

flag = "redacted"
key = "redacted"
assert all([k in ALPHABET for k in key])
assert len(key) == 1
```

assert関数はその後の条件文を満たさない場合エラーを返し、プログラムを止める<br>
要するにこの暗号化の前提条件として

* key を構成するの全ての文字は [a-p] であること
* key は 1文字であること

が存在する

そう、key は 1文字であるのだ<br>
ということで key が [a-p] である場合を全探索で見てフラグゲット

※因みに key = 'p'

### 反省
1文字であることには気づいたが、flag が アルファベット以外あることを考慮に入れずにスクリプトが間違っていると疑ってしまった<br>
結局、{1-9_?} などの記号・数字であった......気づけたものだった

# 解答
picoCTF{et_tu?_77866c61}
