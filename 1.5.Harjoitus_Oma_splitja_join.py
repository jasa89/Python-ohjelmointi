
# Exercise 
def my_split(sentence, delimiter):
    words = []
    current_word = ""
    
    for char in sentence:
        if char == delimiter:
            words.append(current_word)
            current_word = ""
        else:
            current_word += char
            
    
    if current_word:
        words.append(current_word)
    
    return words

def my_join(word_list, delimiter):
    result = ""
    
    for i, word in enumerate(word_list):
        result += word
        if i < len(word_list) - 1:
            result += delimiter
    
    return result
# Put your code here



sentence = str(input("Kirjoita lause:"))
print(my_join(my_split(sentence,' '),','))
print(my_join(my_split(sentence,' '),'\n'))