import hashlib
import socket
import re

# チーズリストの読み込み
with open("cheese_list.txt", "r") as f:
    cheeses = [line.strip() for line in f.readlines()]

def find_cheese(target_hash):
    for cheese in cheeses:
        c_variants = [cheese, cheese.lower(), cheese.replace(" ", ""), cheese.lower().replace(" ", "")]
        for c in c_variants:
            for i in range(256):
                salt = f"{i:02x}"
                # パターン: c + salt (bytes)
                if hashlib.sha256(c.encode() + bytes.fromhex(salt)).hexdigest() == target_hash:
                    return cheese, salt
    return None, None

def solve():
    host = "verbal-sleep.picoctf.net"
    port = 55026
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    
    # 受信
    data = s.recv(4096).decode()
    print(data)
    
    match = re.search(r"guess it:  ([a-f0-9]{64})", data)
    if not match:
        print("Hash not found")
        return
    
    target_hash = match.group(1)
    print(f"Target Hash: {target_hash}")
    
    print("Searching...")
    cheese, salt = find_cheese(target_hash)
    print(f"Found: {cheese} with salt {salt}")
    
    if cheese:
        # サーバーの指示に従って入力
        # "What would you like to do?" -> "g"
        s.send(b"g\n")
        print(s.recv(4096).decode()) # "What is the name of the cheese?"
        s.send((cheese + "\n").encode())
        print(s.recv(4096).decode()) # "What is the salt?"
        s.send((salt + "\n").encode())
        print(s.recv(4096).decode()) # 結果

if __name__ == "__main__":
    solve()
