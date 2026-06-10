import collections

# 暗号化されたstudy.txtの内容
with open('given/study.txt', 'r') as f:
    study_text = f.read().replace('\n', '')

# 暗号化されたflag.txtの内容
with open('given/flag.txt', 'r') as f:
    flag_text = f.read().replace('\n', '')

# 頻度分析
counts = collections.Counter(study_text)
cipher_freq = [c for c, count in counts.most_common()]
english_freq = list('etaoinshrdlcumfygwbpvkxjqz')

# マッピングを作成
mapping = dict(zip(cipher_freq, english_freq))

# 復号関数
def decrypt(text, mapping):
    return ''.join([mapping.get(c, c) for c in text])

# 復号してみる
decrypted_study = decrypt(study_text, mapping)
print("復号されたstudy.txtの冒頭:")
print(decrypted_study[:100])

# flagを復号してみる
decrypted_flag = decrypt(flag_text, mapping)
print("\n復号されたflag.txt:")
print(decrypted_flag)
