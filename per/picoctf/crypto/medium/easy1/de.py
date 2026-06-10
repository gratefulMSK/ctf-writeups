def vigenere_encrypt(plain_text, key):
    """ヴィジュネル暗号で暗号化する関数"""
    cipher_text = []
    key = key.upper()
    key_index = 0

    for char in plain_text:
        if char.isalpha():
            # 大文字か小文字かで基準となるアスキーコードを決める
            start = ord('A') if char.isupper() else ord('a')
            
            # 鍵の文字のシフト量を計算 (A=0, B=1, ... Z=25)
            shift = ord(key[key_index % len(key)]) - ord('A')
            
            # 暗号化アルゴリズム: (文字 + シフト量) % 26
            encrypted_char = chr((ord(char) - start + shift) % 26 + start)
            cipher_text.append(encrypted_char)
            
            # 鍵のインデックスを進める（アルファベットのときのみ）
            key_index += 1
        else:
            # 記号やスペースはそのまま
            cipher_text.append(char)
            
    return "".join(cipher_text)


def vigenere_decrypt(cipher_text, key):
    """ヴィジュネル暗号を復号する関数"""
    plain_text = []
    key = key.upper()
    key_index = 0

    for char in cipher_text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            
            # 鍵の文字のシフト量を計算
            shift = ord(key[key_index % len(key)]) - ord('A')
            
            # 復号アルゴリズム: (文字 - シフト量 + 26) % 26
            decrypted_char = chr((ord(char) - start - shift + 26) % 26 + start)
            plain_text.append(decrypted_char)
            
            key_index += 1
        else:
            plain_text.append(char)
            
    return "".join(plain_text)


s = "UFJKXQZQUNB"
key = "SOLVECRYPTO"


print(f"復号後    : {vigenere_decrypt(s, key)}")