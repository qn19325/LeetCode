# Longest Repeating Character Replacement

## Type: Sliding Window

## Method:
1) Checking validity: length of window - count(most_freq_elem) <= k
2) How window works: expand window size whilst substring is valid, when it doesn't hold shift left pointer (removing elements from hashmap) until it is valid again
3) Most frequent character variable will only need to be updated when increasing max length

### Notes:
1) Storing occurences of characters in hashmap
