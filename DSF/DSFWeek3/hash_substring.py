# python3

def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    tLen = len(text)
    pLen = len(pattern)
    hash_ = 1
    pHash = 0
    tHash = 0
    charCount = 52
    mod = 101
    outSet = []
    
    for i in range(pLen - 1):
        hash_ = (hash_ * charCount) % mod

    for i in range(pLen):
        pHash = (charCount * pHash + ord(pattern[i])) % mod
        tHash = (charCount * tHash + ord(text[i])) % mod
    
    for i in range(tLen - pLen + 1):
        if pHash == tHash:
            if pattern == text[i: i + pLen]:
                outSet.append(i)
        if i < tLen - pLen:
            tHash = (charCount * (tHash - ord(text[i]) * hash_) + ord(text[i + pLen])) % mod
            if tHash < 0:
                tHash = tHash + mod

    return outSet

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

