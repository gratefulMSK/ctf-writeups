from pwn import *
import gmpy2

# ターゲット情報
host = "titan.picoctf.net"
port = 51335

# 通信の生ログ（サーバーとの生のやり取り）を全部見たい場合はここを 'debug' に変更してください。
# 普段は 'info' にしておくと画面がスッキリします。
context.log_level = 'info' 

def get_decrypted_value(io, payload):
    """オラクルにペイロードを送り、暗号文を数値として取得する"""
    io.recvuntil(b"E --> encrypt D --> decrypt. \n")
    io.sendline(b"D")
    
    io.recvuntil(b"Enter text to decrypt: ")
    # ペイロードを送信
    io.sendline(payload)
    
    # サーバーからの暗号文を抽出
    io.recvuntil(b"decrypted ciphertext as hex (c ^ d mod n): ")
    ciphertext_str = io.recvline().strip().decode()
    
    return int(ciphertext_str, 16)

def main():
    # サーバーに接続
    io = remote(host, port)
    
    # 取得したい数値 (Nを求めるための GCD 計算に使う組み合わせ)
    targets = [2, 3, 4, 6]
    N = 110151969047128444515103880417617529051769270868919904525750949580191323035735285236027363804380859577676696188702919080567430333135052874868670346505559420
    c = 2575135950983117315234568522857995277662113128076071837763492069763989760018604733813265929772245292223046288098298720343542517375538185662305577375746934
    c2 = 5067313465613043651275429665315895824157755779222372979446076012356324498190828210335763979330272318657269048435311897896433721115606764442199497891219230


    # ファイルへの書き込みと画面出力
    with open("output2.txt", "w") as f:
        log.info("オラクルへの問い合わせを開始します...")
        
        payload = str((c * c2) % N).encode()
        
        log.info(f"送信中: rc ...")
        
        # 暗号文の取得
        rc = get_decrypted_value(io, payload)
        
        # 画面に見やすく出力 (pwntools の機能)
        log.success(f"E(rc) 取得完了")

        m = (rc * gmpy2.invert(2, N)) % N
        
        # ファイルには計算に使いやすい形で保存
        f.write(f"c{m} = {c}\n")
            
    io.close()
    log.info("すべてのデータを output.txt に保存しました！")

if __name__ == "__main__":
    main()