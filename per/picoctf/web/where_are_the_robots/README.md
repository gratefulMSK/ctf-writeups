# 問題

>Description<br>
>Can you find the robots?

説明<br>
ロボットを見つけられますか？

# 解法要約
robots.txt見る、勝ち

# 解法
タイトルから `/robots.txt` に何かあるのは分かる<br>
見てみると

```Text
User-agent: *
Disallow: /cc6b1.html
```

なので `/cc6b1.html` 見ると flag ゲット

# 解答
picoCTF{ca1cu1at1ng_Mach1n3s_cc6b1}