# 問題

>Description<br>
>Sometimes RSA certificates are breakable

説明<br>
RSA証明書は時として破られることがある

# 解法要約
openssl で証明書見る、n 小さい、素因数分解、勝ち

# 解法

くそかも

いや、、、、、、くそかも

配布は cert というファイル<br>
問題文・ファイル名から証明書と予想できるため openssl で中身を見る

``` bash
openssl x509 -text -noout -in cert
```

中を見ると

``` Text
Data:
    Version: 1 (0x0)
    Serial Number: 12345 (0x3039)
    Signature Algorithm: md2WithRSAEncryption
    Issuer: CN=PicoCTF
    Validity
        Not Before: Jul  8 07:21:18 2019 GMT
        Not After : Jun 26 17:34:38 2019 GMT
    Subject: OU=PicoCTF, O=PicoCTF, L=PicoCTF, ST=PicoCTF, C=US, CN=PicoCTF
    Subject Public Key Info:
        Public Key Algorithm: rsaEncryption
            Public-Key: (53 bit)
            Modulus: 4966306421059967 (0x11a4d45212b17f)
            Exponent: 65537 (0x10001)
Signature Algorithm: md2WithRSAEncryption
```

**で？**

n (Modulus) は明らかに小さいが、公開鍵だけで暗号文がなければ復号もできない

詰み...ヒントを見なければ......

まず前提としてこの問題はヒントを見る必要がある<br>
すると

```
ヒント1 :
The flag is in the format picoCTF{p,q}
ヒント2 :
Try swapping p and q if it does not work
```

ということで n を factorint なりで素因数分解してフラグゲット

# 解答
picoCTF{73176001,67867967}
