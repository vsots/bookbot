import sys
from stats import text_word_count, text_character_count, sorted_character_counts

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_text = get_book_text(sys.argv[1])
    num_words = text_word_count(book_text)
    char_counts = text_character_count(book_text)
    sorted_counts = sorted_character_counts(char_counts)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for count in sorted_counts:
        if count["char"].isalpha():
            print(f"{count["char"]}: {count["num"]}")
    print("============= END ===============")

main()
