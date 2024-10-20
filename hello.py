def reverse_word(string, word):
    reversed = ""
    for letter in word:
        reversed = letter + reversed
    return reversed

def check_all_palindromes(array, arr):
    reversed1 = reverse_word(word1)
    reversed2 = reverse_word(word2)
    reversed3 = reverse_word(word3)

    if arr[0] != reversed1:
        return False
    
    if arr[1] != reversed2:
        return False
    
    if arr[2] != reversed3:
        return False
    return True
print(reverse_word)