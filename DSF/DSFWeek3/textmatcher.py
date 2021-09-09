def rabinKarpMatcher(text, pattern, charCount, mod):
    tLen = len(text)
    pLen = len(pattern)
    hash_ = 1
    pHash = 0
    tHash = 0
    
    for i in range(pLen - 1):
        hash_ = (hash_ * charCount) % mod

    for i in range(pLen):
        pHash = (charCount * pHash + ord(pattern[i])) % mod
        tHash = (charCount * tHash + ord(text[i])) % mod
    
    for i in range(tLen - pLen + 1):
        if pHash == tHash:
            if pattern == text[i: i + pLen]:
                print(i)
        if i < tLen - pLen:
            tHash = (charCount * (tHash - ord(text[i]) * hash_) + ord(text[i + pLen])) % mod
            if tHash < 0:
                tHash = tHash + mod

text = "baaaaaaa"
pattern = "aaaaa"
charCount = 52
mod = 101
rabinKarpMatcher(text, pattern, charCount, mod)
