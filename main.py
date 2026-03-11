import sys
from stats import get_num_words, get_count_characters, format

if len(sys.argv) != 2:
	print("Usage: python3 main.py <path_to_book>")
	sys.exit(1)

book_path = sys.argv[1]

def get_book_text():
	with open(book_path) as f:
		file_contents = f.read()

	return file_contents

def main():
	text = get_book_text()
	num_words = get_num_words(text)
	char_counts = get_count_characters(text)
	sorted_chars = format(char_counts)

	print(sys.argv)

	print("============== BOOKBOT ==============")
	print(f"Analyzing book found at {book_path}...")
	print("------------ Word Count -------------")
	print(f"Found {num_words} total words")
	print("---------- Character Count ----------")

	for item in sorted_chars:
		ch = item["char"]
		num = item["num"]
		if not ch.isalpha():
			continue
		print(f"{ch}: {num}")

	print("================ END ================")


main()


