import sys
from stats import get_num_words, get_num_chars, sort_num_chars

if len(sys.argv) == 1:
    print(f"Usage: python3 {sys.argv[0]} <path_to_book>")
    sys.exit(1)


def get_book_text(input_file):
    with open(input_file) as f:
    # do something with f (the file) here
        # f is a file object
        content = f.read() 

    return content


def main():
    content = get_book_text(sys.argv[1])
    num_words = get_num_words(content)
    num_chars = get_num_chars(content)
    sorted_num_chars = sort_num_chars(num_chars)

    # Print Report:
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    # list of sorted chars by count desc
    for item in sorted_num_chars:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")

    print("============= END ===============")

main()