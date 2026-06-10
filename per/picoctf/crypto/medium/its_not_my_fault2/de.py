import hashlib
import time

def solve_md5_quiz(input_preffix, target_hash_suffix):
    counter = 0
    start_time = time.time()
    
    print( "探索を開始します...")
    
    while True:
        # 1. 可変部分（今回は数字のカウント） + 固定の5文字 で入力文字列を作成
        input_str = f"{input_preffix}{counter}"
        
        # 2. MD5を計算（文字列は一旦 bytes にエンコードする必要がある）
        hash_result = hashlib.md5(input_str.encode('utf-8')).hexdigest()
        
        # 3. ハッシュ値の末尾6文字が一致するかチェック
        if hash_result.endswith(target_hash_suffix):
            elapsed_time = time.time() - start_time
            print("\n=== 条件達成 ===")
            print(f"見つかった入力値: {input_str}")
            print(f"MD5ハッシュ値   : {hash_result}")
            print(f"総試行回数      : {counter:,} 回")
            print(f"かかった時間    : {elapsed_time:.2f} 秒")
            return input_str
        
        counter += 1
        
        # 進捗確認用（1,000万回ごとに表示）
        if counter % 10000000 == 0:
            print(f"現在 {counter:,} 回試行中...")

# --- 条件の設定 ---
INPUT_SUFFIX = "39174"       # 元のデータの最後の5文字
TARGET_HASH_SUFFIX = "f37a2a" # 狙いたいMD5の末尾6文字（16進数）

solve_md5_quiz(INPUT_SUFFIX, TARGET_HASH_SUFFIX)