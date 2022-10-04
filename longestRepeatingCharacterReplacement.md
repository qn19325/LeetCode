# Longest Repeating Character Replacement

## Type: Sliding Window

## Method:
1) Checking validity: length of window - count(most_freq_elem) <= k
2) How window works: expand window size whilst substring is valid, when it doesn't hold shift left pointer (removing elements from hashmap) until it is valid again
3) Most frequent character variable will only need to be updated when increasing max length

### Notes:
1) Storing occurences of characters in hashmap

## Code
```{py}
def characterReplacement(self, s: str, k: int) -> int:
        hash_table = {}
        left = 0
        maxf = 0
        maxlen = 0
        for right in range(len(s)):
            hash_table[s[right]] = 1 + hash_table.get(s[right], 0)
            maxf = max(maxf, hash_table[s[right]])

            if (right - left + 1) - maxf > k: 
                hash_table[s[left]] -= 1
                left += 1
            
            maxlen = max(right - left + 1, maxlen)

        return maxlen
```        
