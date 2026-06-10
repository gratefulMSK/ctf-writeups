c = "rgnoDVD{O0NU_WQ3_G1G3O3T3_A1AH3S_cc82272b}"
key = "CYLAB"


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



# 復号

decrypted = vigenere_decrypt(c, key)
print(f"復号後    : {decrypted}")