class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        d = {}
        for i in word:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1

        freq = []
        for i in d:
            freq.append(d[i])

        unique_freqs = []
        for f in freq:
            if f not in unique_freqs:
                unique_freqs.append(f)

        unique_freqs.sort()
        min_deletions = len(word) 

        for target in unique_freqs:
            deletions = 0
            for f in freq:
                if f < target:
                    deletions += f 
                elif f > target + k:
                    deletions += f - (target + k)
            
            if deletions < min_deletions:
                min_deletions = deletions

        return min_deletions






        
