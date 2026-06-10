from pwn import *

# ターゲット情報
host = "titan.picoctf.net"
port = 59015

# 通信の生ログ（サーバーとの生のやり取り）を全部見たい場合はここを 'debug' に変更してください。
# 普段は 'info' にしておくと画面がスッキリします。
context.log_level = 'info' 

def get_encrypted_value(io, payload):
    """オラクルにペイロードを送り、暗号文を数値として取得する"""
    io.recvuntil(b"E --> encrypt D --> decrypt. \n")
    io.sendline(b"E")
    
    io.recvuntil(b"enter text to encrypt (encoded length must be less than keysize): ")
    # ペイロードを送信
    io.sendline(payload)
    
    # サーバーからの暗号文を抽出
    io.recvuntil(b"ciphertext (m ^ e mod n) ")
    ciphertext_str = io.recvline().strip().decode()
    
    return int(ciphertext_str)

def main():
    # サーバーに接続
    io = remote(host, port)
    
    # 取得したい数値 (Nを求めるための GCD 計算に使う組み合わせ)
    targets = [2, 3, 4, 6]
    
    # ファイルへの書き込みと画面出力
    with open("output.txt", "w") as f:
        log.info("オラクルへの問い合わせを開始します...")
        
        for num in targets:
            # 数値を1バイトのバイナリデータに変換 (例: 2 -> b'\x02')
            # サーバー側でHexエンコードされ '02' として処理されることを期待
            payload = bytes([num])
            
            log.info(f"送信中: {num} ...")
            
            # 暗号文の取得
            c = get_encrypted_value(io, payload)
            
            # 画面に見やすく出力 (pwntools の機能)
            log.success(f"E({num}) 取得完了")
            
            # ファイルには計算に使いやすい形で保存
            f.write(f"c{num} = {c}\n")
            
    io.close()
    log.info("すべてのデータを output.txt に保存しました！")

if __name__ == "__main__":
    main()