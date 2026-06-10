# 問題

>Description<br>
>Can you break into this super secure portal?

説明<br>
この非常に安全なポータルを突破できますか？

# 解法要約
デベロッパーツール、勝ち

# 解法
ベリファイしてくれるだけのサイト<br>
移動もできないし、クッキーもない

ソースコード見てみると、少し難読化されてるだけで認証が実装されてた

```js
  function verify() {
    checkpass = document.getElementById("pass").value;
    split = 4;
    if (checkpass.substring(0, split) == 'pico') {
      if (checkpass.substring(split*6, split*7) == 'eb02') {
        if (checkpass.substring(split, split*2) == 'CTF{') {
         if (checkpass.substring(split*4, split*5) == 'ts_p') {
          if (checkpass.substring(split*3, split*4) == 'lien') {
            if (checkpass.substring(split*5, split*6) == 'lz_2') {
              if (checkpass.substring(split*2, split*3) == 'no_c') {
                if (checkpass.substring(split*7, split*8) == 'b45}') {
                  alert("Password Verified")
                  }
                }
              }
      
            }
          }
        }
      }
    }
    else {
      alert("Incorrect password");
    }
  }
```
があった

順番に読んでフラグゲット

# 解答
picoCTF{no_clients_plz_2eb02b45}