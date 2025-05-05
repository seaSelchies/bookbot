from stats import get_num_words, get_num_characters,sort_num_characters
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        content = f.read()
    return content

def print_report(filepath):
    text = get_book_text(filepath)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(text)} total words")
    print("--------- Character Count -------")
    sorted = sort_num_characters(get_num_characters(text))
    for sorted_num in sorted:
        if sorted_num['char'].isalpha():
            print(f"{sorted_num['char']}: {sorted_num['num']}")


def main():
    args = sys.argv
    if len(args) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = args[1]
    print(filepath)
    print_report(filepath)

    

main()