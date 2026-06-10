# 問題

>Description<br>
>I found this cipher in an old book.

説明<br>
この暗号は古い本で見つけました。

# 解法要約
既知平文攻撃、ヴィジュネル暗号、勝ち

# 解法

通信すると暗号文がもらえる、ちなみに問題からヴィジュネルあたりの古典的な暗号は考えとくとよさそう<br>
暗号文は最後に貼った

流石に読めないので、暗号化されていなさそうな年号で調べる<br>
"1553 1467 1508 暗号" とかで検索するとヴィジュネル暗号が出てきたので確定とする<br>
因みにこういう特定の平文から暗号を読み解く攻撃を既知平文攻撃という

ただし key が分からないので、探す必要がある<br>
人の名前っぽいものを探すと、ヴィジュネル暗号の原型を考えた "Leon Battista Alberti" と同じ文字数の場所を見つけた<br>
"Rjzn Hfetoxea Gqmexyt" である

差を見ると 0, 6, 5, 11 の 4つを繰り返していた<br>
つまり、 key は "flag" であった

あとはどう考えてもフラグの場所である "pohzCZK{m311a50_0x_a1rn3x3_h1ah3xfL83Bg7G}" を復号してフラグゲット

※ちなみに flag とタイトルの意味は復号した文を読めばわかる

### 暗号文と元の文
解読コードは "de.py"
```
Encrypted message:
﻿Ne iy nytkwpsznyg nth it mtsztcy vjzprj zfzjy rkhpibj nrkitt ltc tnnygy ysee itd tte cxjltk

Ifrosr tnj noawde uk siyyzre, yse Bnretèwp Cousex mls hjpn xjtnbjytki xatd eisjd

Iz bls lfwskqj azycihzeej yz Brftsk ip Volpnèxj ls oy hay tcimnyarqj dkxnrogpd os 1553 my Mnzvgs Mazytszf Merqlsu ny hox moup Wa inqrg ipl. Ynr. Gotgat Gltzndtg Gplrfdo

Ltc tnj tmvqpmkseaznzn uk ehox nivmpr g ylbrj ts ltcmki my yqtdosr tnj wocjc hgqq ol fy oxitngwj arusahje fuw ln guaaxjytrd catizm tzxbkw zf vqlckx hizm ceyupcz yz tnj fpvjc hgqqpohzCZK{m311a50_0x_a1rn3x3_h1ah3xfL83Bg7G}

Ehk ktryy herq-ooizxetypd jjdcxnatoty ol f aordllvmlbkytc inahkw socjgex, bls sfoe gwzuti 1467 my Rjzn Hfetoxea Gqmexyt.

Tnj Gimjyèrk Htpnjc iy ysexjqoxj dosjeisjd cgqwej yse Gqmexyt Doxn ox Fwbkwei Inahkw.

Tn 1508, Ptsatsps Zwttnjxiax tnbjytki ehk xz-cgqwej ylbaql rkhea (g rltxni ol xsilypd gqahggpty) ysaz bzuri wazjc bk f nroytcgq nosuznkse ol yse Bnretèwp Cousex.

Gplrfdo’y xpcuso butvlky lpvjlrki tn 1555 gx l cuseitzltoty ol yse lncsz. Yse rthex mllbjd ol yse gqahggpty fce tth snnqtki cemzwaxqj, bay ehk fwpnfmezx lnj yse osoed qptzjcs gwp mocpd hd xegsd ol f xnkrznoh vee usrgxp, wnnnh ify bk itfljcety hizm paim noxwpsvtydkse.
```

```
It is interesting how in history people often receive credit for things they did not create

# During the course of history, the Vigenère Cipher has been reinvented many times

# It was falsely attributed to Blaise de Vigenère as it was originally described in 1553 by Giovan Battista Bellaso in his book La cifra del. Sig. Giovan Battista Bellaso

# For the implementation of this cipher a table is formed by sliding the lower half of an ordinary alphabet for an apparently random number of places with respect to the upper halfpicoCTF{b311a50_0r_v1gn3r3_c1ph3raA83Ba7B}

# The first well-documented description of a polyalphabetic cipher however, was made around 1467 by Leon Battista Alberti.

# The Vigenère Cipher is therefore sometimes called the Alberti Disc or Alberti Cipher.

# In 1508, Johannes Trithemius invented the so-called tabula recta (a matrix of shifted alphabets) that would later be a critical component of the Vigenère Cipher.

# Bellaso’s second booklet appeared in 1555 as a continuation of the first. The lower halves of the alphabets are now shifted regularly, but the alphabets and the index letters are mixed by means of a mnemonic key phrase, which can be different with each correspondent.
```

# 解答
picoCTF{b311a50_0r_v1gn3r3_c1ph3raA83Ba7B}
