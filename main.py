import sys
from stats import word_count, char_count, list_sort

def get_book_text(filepath):
        with open(filepath) as f:
            file_contents = f.read()
        return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_text = get_book_text(sys.argv[1])
    char_dict = char_count(book_text)
    wc= word_count(book_text)
    print(f"--- Begin report of {sys.argv[1]} ---")
    print(f"Found {wc} total words")
    sorted_list = list_sort(char_dict)
    for item in sorted_list:
        char = item["char"]
        num = item["num"]
        print(f"{char}: {num}")
    print("--- End Report ---")

main()