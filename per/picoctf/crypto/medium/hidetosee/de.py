def atbash_cipher(text):
    """アトバッシュ暗号の処理（暗号化・復号共通）"""
    result = []
    
    for char in text:
        if char.isalpha():
            if char.isupper():
                # 大文字の場合: 'A' と 'Z' を反転
                # アルゴリズム: 'Z' から '現在の文字とAの距離' を引く
                flipped_char = chr(ord('Z') - (ord(char) - ord('A')))
                result.append(flipped_char)
            else:
                # 小文字の場合: 'a' と 'z' を反転
                flipped_char = chr(ord('z') - (ord(char) - ord('a')))
                result.append(flipped_char)
        else:
            # 記号やスペースはそのまま
            result.append(char)
            
    return "".join(result)


c = "krxlXGU{zgyzhs_xizxp_1u84w779}"

# 暗号化
decrypted = atbash_cipher(c)
print(f"復号後    : {decrypted}")