def get_num_words(content):
    
    num_words = len(content.split())
    return num_words

def get_num_chars(content):

    dictionaire = {}
    for x in content.lower():
        if x in dictionaire:
            dictionaire[x] += 1
        else:
            dictionaire[x] = 1 

    return dictionaire

def sort_on(items):
    return items["num"]

def sort_num_chars(dictionary_input):

    '''
    this is a more professional approach using items() - however it did appear in lessons yet..
    char_list = [
    {"char": char, "num": num}
    for char, num in dictionary_input.items()
    ]
    '''
    modified_dict = []
    for x in dictionary_input:
        modified_dict.append({"char": x, "num": dictionary_input[x]})

    modified_dict.sort(reverse=True, key=sort_on)

    return modified_dict