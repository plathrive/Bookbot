def get_num_words(text):
	words = text.split()
	num_words = len(words)

	return num_words

def get_count_characters(text):
	counts = {}
	char = text.lower()

	for ch in char:
		if ch in counts:
			counts[ch] = counts[ch] + 1
		else:
			counts[ch] = 1

	return counts

def sort_on(items):
	return items["num"]

def format(char_counts):
	lists = []

	for ch, counts in char_counts.items():
		char_count = {"char": ch, "num": counts}

		lists.append(char_count)

	lists.sort(reverse=True, key=sort_on)

	return lists
