# 問題

>Description<br>
>We made a lot of substitutions to encrypt this. Can you decrypt it?

説明<br>
これを暗号化するために、多くの置換を行いました。解読できますか？

# 解法要約
単一換字式暗号、勝ち

# 解法

配布ファイルはなく、通信だけ<br>
通信すると...

```
-------------------------------------------------------------------------------
uvxrbzit gmbm et svpb cazr - cbmjpmxus_et_u_vhmb_azfoqz_m4903514
-------------------------------------------------------------------------------
dm dmbm xvi fpug fvbm igzx z jpzbimb vc zx gvpb vpi vc vpb tgek ieaa dm tzd gmb texw, zxq igmx e pxqmbtivvq cvb igm cebti iefm dgzi dzt fmzxi os z tgek cvpxqmbexr ex igm tmz.  e fpti zuwxvdamqrm e gzq gzbqas msmt iv avvw pk dgmx igm tmzfmx ivaq fm tgm dzt texwexr; cvb cbvf igm fvfmxi igzi igms bzigmb kpi fm exiv igm ovzi igzx igzi e fergi om tzeq iv rv ex, fs gmzbi dzt, zt ei dmbm, qmzq deigex fm, kzbias deig cbergi, kzbias deig gvbbvb vc fexq, zxq igm igvprgit vc dgzi dzt smi omcvbm fm.
```

読めないが、何かが何かに置換されていそう

頑張る（下記説明）とフラグゲット

※因みにヒントにあるがこれは `picoCTF{}` がフォーマットではない<br>
そのまま送ればよい

### 頑張るとは

頑張ることである...

まあ具体的にはまず<br>
こういう文章を置換するときに使えることとして

* 一文字で意味がなるのは i (私) と a (冠詞) だけである
* 全ての単語には母音 (a, i, u, e, o) と y のいずれかがある
* 2文字は前置詞、and は頻出
* flag という単語が恐らくどこかにある
* 根気よく

を原則にやるとうまくいく

### 楽な解法
なんと自動でやってくれるサイトがあるらしい<br>
https://quipqiup.com/

あと頻度解析も効果的と考えられる<br>
実際、flag の frequency 頻度という意味である

※因みに flag の frequency is c over lambda は光の公式の
* frequency (周波数) = c (光速) / lambda (波長)

の英文である

### 復元後の平文

```
-------------------------------------------------------------------------------
congrats here is your flag - frequency_is_c_over_lambda_e4903514
-------------------------------------------------------------------------------
we were not much more than a quarter of an hour out of our ship till we saw her sink, and then i understood for the first time what was meant by a ship foundering in the sea.  i must acknowledge i had hardly eyes to look up when the seamen told me she was sinking; for from the moment that they rather put me into the boat than that i might be said to go in, my heart was, as it were, dead within me, partly with fright, partly with horror of mind, and the thoughts of what was yet before me.
```


# 解答
frequency_is_c_over_lambda_e4903514
