MOD = 10**9 + 7

class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
      
        fact = [1] * (n + 1)
        inv_fact = [1] * (n + 1)

        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i % MOD

        inv_fact[n] = pow(fact[n], MOD - 2, MOD)
        for i in range(n - 1, -1, -1):
            inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD

        def comb(a, b):
            if b < 0 or b > a:
                return 0
            return fact[a] * inv_fact[b] % MOD * inv_fact[a - b] % MOD

        ways = m                      
        ways *= comb(n - 1, k)     
        ways %= MOD
        ways *= pow(m - 1, n - 1 - k, MOD) 
        ways %= MOD

        return ways
