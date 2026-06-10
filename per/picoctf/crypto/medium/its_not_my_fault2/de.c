#include <stdio.h>
#include <stdlib.h>
#include <gmp.h>
#include <omp.h>

#define BATCH_SIZE 10000

int main() {
    // TODO: サーバーから取得した n と e を入力してください
    const char *n_str = "61141246976969681381836064501741688188914671173443958910838492997038936176967727621195570151517530246869107840082582738257907396975707129348981003314625265159126388664443028757274078247947555897804308412866445391420028899321835504001649713702183245410983524405435833400801144683564950269412152034033665553287";
    const char *e_str = "40783983083253469339147263866496974167296117580835667102759553202449414365224338116493702790012045897957302232558082672399002735177757299683133955571926463976970386027681816027714493032856290556408171670105946094832519917533240127583893529465491296156082005969610835392219441394682267329509163545294331159483";

    mpz_t n, e, base, g;
    mpz_inits(n, e, base, g, NULL);
    mpz_set_str(n, n_str, 0);
    mpz_set_str(e, e_str, 0);
    mpz_set_ui(base, 2);
    
    // g = 2^e mod n
    mpz_powm(g, base, e, n);

    long long max_dp = 1LL << 36;
    int found = 0;
    int num_cores = omp_get_max_threads();
    printf("[+] CPU Cores: %d\n", num_cores);
    printf("[+] Starting Ultra-Fast Search (Wheel Factorization 2,3,5 & Lazy Modulo)...\n");

    // 素数車輪 (mod 30) のギャップ事前計算
    // 30と互いに素な数の間隔: 6, 4, 2, 4, 2, 4, 6, 2
    int gaps[8] = {6, 4, 2, 4, 2, 4, 6, 2};
    mpz_t g_gaps[8];
    for(int i = 0; i < 8; i++) {
        mpz_init(g_gaps[i]);
        mpz_t temp; 
        mpz_init_set_ui(temp, gaps[i]);
        mpz_powm(g_gaps[i], g, temp, n);
        mpz_clear(temp);
    }

    double start_time = omp_get_wtime();

    #pragma omp parallel
    {
        mpz_t V, P, gcd_res, p, q, V_minus_2;
        mpz_inits(V, P, gcd_res, p, q, V_minus_2, NULL);
        int thread_id = omp_get_thread_num();

        // 探索空間のチャンク分割
        long long chunk_size = max_dp / num_cores;
        long long start_dp = thread_id * chunk_size;
        long long end_dp = start_dp + chunk_size;
        if (thread_id == num_cores - 1) end_dp = max_dp;

        // このチャンクで最初の「2, 3, 5の倍数ではない数」を探す
        long long current_dp = start_dp;
        if (current_dp <= 1) current_dp = 1;
        while (current_dp % 2 == 0 || current_dp % 3 == 0 || current_dp % 5 == 0) {
            current_dp++;
        }

        // 現在の mod 30 の位置からギャップのインデックスを特定
        int gap_idx = 0;
        int mod30 = current_dp % 30;
        int coprimes[] = {1, 7, 11, 13, 17, 19, 23, 29};
        for(int i = 0; i < 8; i++) {
            if(mod30 == coprimes[i]) {
                gap_idx = i;
                break;
            }
        }

        // V = g^current_dp mod n
        mpz_t start_pow; 
        mpz_init_set_ui(start_pow, current_dp);
        mpz_powm(V, g, start_pow, n);
        mpz_clear(start_pow);

        mpz_set_ui(P, 1);
        int batch_count = 0;

        while(current_dp <= end_dp && !found) {
            mpz_sub_ui(V_minus_2, V, 2);
            mpz_mul(P, P, V_minus_2);

            // Lazy Modulo: 32回に1回だけ mod n を実行して割り算を大幅削減
            if (batch_count % 32 == 31) {
                mpz_mod(P, P, n);
            }

            batch_count++;

            // Batchの終端で一気にGCD
            if (batch_count == BATCH_SIZE) {
                mpz_mod(P, P, n); // GCD前に確実にmodを取る
                mpz_gcd(gcd_res, P, n);
                
                if (mpz_cmp_ui(gcd_res, 1) > 0 && mpz_cmp(gcd_res, n) < 0) {
                    #pragma omp critical
                    {
                        if (!found) {
                            found = 1;
                            // Pにpが含まれていたので、GCDの結果がそのまま p になる！
                            mpz_set(p, gcd_res);
                            mpz_divexact(q, n, p);
                            
                            printf("\n[+] BINGO!\n");
                            gmp_printf("[+] p = %Zd\n", p);
                            gmp_printf("[+] q = %Zd\n", q);
                            
                            mpz_add(p, p, q);
                            gmp_printf("\n[+] Answer (p + q) = %Zd\n", p);
                            printf("[+] Time elapsed: %.2f seconds\n", omp_get_wtime() - start_time);
                        }
                    }
                }
                mpz_set_ui(P, 1);
                batch_count = 0;

                // 進捗表示
                if (thread_id == 0) {
                    printf("Progress: %.2f%%\r", (double)(current_dp - start_dp) / chunk_size * 100);
                    fflush(stdout);
                }
            }

            // 次の V へ（ギャップ分だけ進む）
            mpz_mul(V, V, g_gaps[gap_idx]);
            mpz_mod(V, V, n);
            current_dp += gaps[gap_idx];
            gap_idx = (gap_idx + 1) % 8;
        }

        mpz_clears(V, P, gcd_res, p, q, V_minus_2, NULL);
    }

    mpz_clears(n, e, base, g, NULL);
    return 0;
}