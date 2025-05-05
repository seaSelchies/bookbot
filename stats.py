def get_num_words(text):
    return len(text.split())

def get_num_characters(text):
    result = {}
    words = text.split()
    for word in words:
        for letter in word:
            letter = letter.lower()
            if (letter in result):
                result[letter] += 1
            else: 
                result[letter] = 1
    
    return result

def sort_on(dict):
    return dict["num"]

def sort_num_characters(characters):
    result  = []
    for character in characters:
        result.append({"char": character,"num":characters[character]})
    result.sort(key=sort_on, reverse=True)
    return result

        

