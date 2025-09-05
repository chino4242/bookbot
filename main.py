from stats import word_count, char_count, list_sort

def get_book_text(filepath):
        with open(filepath) as f:
            file_contents = f.read()
        return file_contents

def main():
    book_text = get_book_text("./books/frankenstein.txt")
    char_dict = char_count(book_text)
    wc= word_count(book_text)
    print(f"Found {wc} total words")
    sorted_list = list_sort(char_dict)
    for item in sorted_list:
        char = item["char"]
        num = item["num"]
        print(f"{char}: {num}")

main()