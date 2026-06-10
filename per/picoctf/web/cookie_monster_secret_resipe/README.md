# 問題

>Description<br>
>Cookie Monster has hidden his top-secret cookie recipe somewhere on his website. As an aspiring cookie detective, your mission is to uncover this delectable secret. Can you outsmart Cookie Monster and find the hidden recipe?

説明<br>
クッキーモンスターは、極秘のクッキーレシピをウェブサイトのどこかに隠しました。駆け出しのクッキー探偵であるあなたの使命は、このとびきり美味しい秘密を解き明かすことです。クッキーモンスターを出し抜いて、隠されたレシピを見つけることができるでしょうか？

# 解法要約
クッキー、base64、勝ち

# 解法

適当にログインしたら以下の文章

```Text
Access Denied
Cookie Monster says: 'Me no need password. Me just need cookies!'

Hint: Have you checked your cookies lately?

Go back
```

まあタイトル通りクッキーを見ると
```Text
cGljb0NURntjMDBrMWVfbTBuc3Rlcl9sMHZlc19jMDBraWVzXzczMTEwRUQxfQ%3D%3D
```

とりあえず base64 使うとフラグゲット

# 解答
picoCTF{c00k1e_m0nster_l0ves_c00kies_73110ED1}
