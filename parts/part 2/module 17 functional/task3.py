from collections import Counter

def can_be_poly(s: str) -> bool:
    char_count = Counter(s)
    odd_count = sum(count % 2 for count in char_count.values())

    return odd_count <= 1

def main():
    print(can_be_poly('abcba'))  
    print(can_be_poly('abbbc'))  

if __name__=='__main__':
    main()


