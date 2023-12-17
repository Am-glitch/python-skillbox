from typing import List

def main():
    letters: List[str] = ['a', 'b', 'c', 'd', 'e']
    numbers: List[int] = [1, 2, 3, 4, 5, 6, 7, 8]

    results = list(map(lambda x, y: (x, y), letters, numbers))
    print(results)

if __name__ == '__main__':
    main()
