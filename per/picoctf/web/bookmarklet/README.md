# 問題

>Description<br>
>Why search for the flag when I can make a bookmarklet to print it for me?

説明<br>
国旗を探す手間を省いて、印刷用のブックマークレットを作ってみませんか？

# 解法要約
ブックマーク、勝ち

# 解法

ページに行くと

>Welcome to my flag distribution website!<br>
>If you're reading this, your browser has succesfully received the flag.<br>
>Here's a bookmarklet for you to try:

私の国旗配布ウェブサイトへようこそ！<br>
この文章が表示されているということは、ブラウザが国旗を正常に受信したということです。<br>
ぜひお試しください。

と一緒に以下の js のコードがあった

```js
javascript:(function() {
    var encryptedFlag = "àÒÆÞ¦È¬ëÙ£ÖÓÚåÛÑ¢ÕÓÔÅÐÙí";
    var key = "picoctf";
    var decryptedFlag = "";
    for (var i = 0; i < encryptedFlag.length; i++) {
        decryptedFlag += String.fromCharCode((encryptedFlag.charCodeAt(i) - key.charCodeAt(i % key.length) + 256) % 256);
    }
    alert(decryptedFlag);
})();
```

タイトルから察するにこれをブックマークに追加しろとのこと<br>
ブックマークにこの jacascript: から始まるコードを追加しクリックするとalertでフラグゲット

### ブックマークレットについて
ブックマークになぜ js コードが登録できるかというと、ブラウザが `http:`, `https:`, `javascript:`, `mailto` といった uriスキームを設定しているからである<br>
それぞれの uriスキームには役割が決まっており、 `http:`, `https:` は後ろのドメインに飛び、  `file:` はローカルの pdf ファイルをブラウザで開くときなどに使う<br>
`javascript:` はうしろの js のコードを実行する

さらに、この実行はその時開いているサイトの内部として実行される<br>
すると、そのサイトの DOM やクッキーにアクセスすることもできる<br>
つまり XSS が可能となる

このように被害者に XSS を登録させて実行させるものを self-XSS という

ちなみにブラウザの上の url を変更することとブックマークをクリックすることは同じであり、上の url を `javascript:` にして実行してもフラグが得られる

さらに因みに、ブラウザの場所によっては `javascript:` uriスキームが使えなくなることがある<br>
どういうことかというと、グーグルの検索画面はクロスサイトスクリプティングなど意図しないコードから守る機能 CSP (Content Security Policy) をしっかりつけている<br>
そういう時は about:blank という url を検索し、そのページからは CSP がかかっていない

# 解答
picoCTF{p@g3_turn3r_1d1ba7e0}
