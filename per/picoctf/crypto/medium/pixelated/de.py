from PIL import Image
import numpy as np

# 画像を読み込む
img1 = Image.open('scrambled1.png').convert('RGB')
img2 = Image.open('scrambled2.png').convert('RGB')

arr1 = np.array(img1)
arr2 = np.array(img2)

# 2. 256で割った余りを取る（これが通常の加算ロジック）
added_arr = arr1.astype(np.int32) + arr2.astype(np.int32)
wrap_arr = (added_arr % 256).astype(np.uint8)

# 画像として出力
result_img = Image.fromarray(wrap_arr)

# 拡大した状態で保存
result_img.save('result_final.png')