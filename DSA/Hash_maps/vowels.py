import sys

def vowelsCount(str1):
    vow = ["a", "e", "i", "o", "u"]
    count = 0
    for i in str1:
        if i in vow:
            count += 1
    return count

def vowelsHash(str1):
    vow = {}
    vowels = ["a", "e", "i", "o", "u"]
    
    for i in str1:
        if i in vowels and vow[i] == 0:
            vow[i] +=1
        else:
            vow[i] = 1
    return vow
            

if __name__ == "__main__":
    str1 = " ".join(sys.argv[1:])
    print(vowelsCount(str1))
    print(vowelsHash(str1))