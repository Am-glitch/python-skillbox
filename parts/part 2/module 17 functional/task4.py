def count_unique_characters(s: str) -> int:
    unique_count = len(set(filter(lambda char: char.isalpha(), s.lower())))
    return unique_count

def main(): 
    message = "Today is a beautiful day! The sun is shining and the birds are singing."
    unique_count = count_unique_characters(message)
    print("Количество уникальных символов в строке:", unique_count)

if __name__=='__main__':
    main()

