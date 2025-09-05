def word_count(book):
    words = book.split()
    wc= len(words)
    return wc



def char_count(book):
    char_dict = {
    }
    
    for char in book:
        char_lower = char.lower()
        char_dict[char_lower] = char_dict.get(char_lower, 0) + 1
    return char_dict

def sort_on(items):
    return items["num"]

def list_sort(char_dict):
    dict_list = []
    for key, value in char_dict.items():
        temp_dict = {}
        if key.isalpha():
            temp_dict["char"] = key
            temp_dict["num"] = value
            dict_list.append(temp_dict)
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list