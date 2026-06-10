def decrypt_rail_fence(cipher, rails):
    fence = [['\n' for i in range(len(cipher))] for j in range(rails)]
    
    rail = 0
    direction = 1
    for i in range(len(cipher)):
        fence[rail][i] = '*'
        rail += direction
        if rail == rails - 1 or rail == 0:
            direction = -direction
            
    index = 0
    for i in range(rails):
        for j in range(len(cipher)):
            if fence[i][j] == '*' and index < len(cipher):
                fence[i][j] = cipher[index]
                index += 1
                
    result = []
    rail = 0
    direction = 1
    for i in range(len(cipher)):
        result.append(fence[rail][i])
        rail += direction
        if rail == rails - 1 or rail == 0:
            direction = -direction
            
    return "".join(result)

cipher_text = "Ta _7N6DDDhlg:W3D_H3C31N__0D3ef sHR053F38N43D0F i33___NA"
for r in range(2, 6):
    print(f"Rails {r}: {decrypt_rail_fence(cipher_text, r)}")
