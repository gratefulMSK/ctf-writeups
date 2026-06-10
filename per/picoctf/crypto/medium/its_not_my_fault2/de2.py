import math
import multiprocessing
import time
import sys

def search_worker(args):
    start_dp, step, max_dp, n, e = args
    
    # g = 2^e mod n
    g = pow(2, e, n)
    
    # 初期値: V = g^(start_dp) mod n
    V = pow(g, start_dp, n)
    
    # ステップごとの乗数: g_step = g^step mod n
    g_step = pow(g, step, n)
    
    dp = start_dp
    # 割り当てられた奇数のみをスキップしながら探索
    while dp <= max_dp:
        # V = 2^(e * d_p) mod n
        # pの倍数であれば gcd(V - 2, n) > 1 になる
        p = math.gcd(V - 2, n)
        if 1 < p < n:
            q = n // p
            return (dp, p, q)
        
        # 次のステップへ (乗算1回のみで高速化)
        V = (V * g_step) % n
        dp += step
        
    return None

def solve(n, e):
    max_dp = 1 << 36
    num_cores = multiprocessing.cpu_count()
    print(f"[+] CPU Cores detected: {num_cores}")
    print("[+] Starting parallel search for odd d_p...")
    
    # d_p は奇数なので、1つのプロセスが進むステップ幅は 2 * コア数
    global_step = 2 * num_cores
    
    tasks = []
    for i in range(num_cores):
        # 各コアの開始位置を 1, 3, 5, 7... にずらす
        start_dp = 1 + (2 * i)
        tasks.append((start_dp, global_step, max_dp, n, e))
        
    start_time = time.time()
    
    # プロセスプールで並列実行
    with multiprocessing.Pool(num_cores) as pool:
        # imap_unordered で終わったものから順次結果を受け取る
        for result in pool.imap_unordered(search_worker, tasks):
            if result:
                dp, p, q = result
                print("\n[+] BINGO!")
                print(f"[+] d_p = {dp}")
                print(f"[+] p = {p}")
                print(f"[+] q = {q}")
                print(f"[+] Answer (p + q) = {p + q}")
                print(f"[+] Time elapsed: {time.time() - start_time:.2f} seconds")
                
                # 見つかったら他のプロセスを強制終了
                pool.terminate() 
                return p + q
                
    print("[-] Could not find p and q.")
    return None

if __name__ == "__main__":
    # TODO: サーバーから取得した n と e を入力してください
    n = 61141246976969681381836064501741688188914671173443958910838492997038936176967727621195570151517530246869107840082582738257907396975707129348981003314625265159126388664443028757274078247947555897804308412866445391420028899321835504001649713702183245410983524405435833400801144683564950269412152034033665553287
    e = 40783983083253469339147263866496974167296117580835667102759553202449414365224338116493702790012045897957302232558082672399002735177757299683133955571926463976970386027681816027714493032856290556408171670105946094832519917533240127583893529465491296156082005969610835392219441394682267329509163545294331159483

    solve(n, e)