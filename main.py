def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    alphabet = get_alpha(chars_dict)
    for num in alphabet:
        print(f"The '{num}' character was found {alphabet[num]} times")

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()   
    return(file_contents)

def get_num_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    lowered_text = text.lower()
    dict = {}
    for char in lowered_text:
        if char not in dict:
            dict[char] = 1
        else:
            dict[char] += 1
    return(dict)

def get_alpha(dict):
    dict2 = {}
    for char in dict:
        if char.isalpha():
            dict2[char] = dict[char]
    
    return dict2

main()