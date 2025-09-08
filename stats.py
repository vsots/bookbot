def text_word_count(book_text):
    return len(book_text.split())

def text_character_count(book_text):
    char_counts = {}
    for char in book_text:
        lo_char = char.lower()
        if lo_char in char_counts:
            char_counts[lo_char] += 1
        else:
            char_counts[lo_char] = 1
    
    return char_counts

def sorted_character_counts(char_counts):
    def sort_on(items):
        return items["num"]

    to_sort = []
    for char, num in char_counts.items():
        to_sort.append({"char": char, "num": num})

    to_sort.sort(reverse=True, key=sort_on)
    return to_sort
