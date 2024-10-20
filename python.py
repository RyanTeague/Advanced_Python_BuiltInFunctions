def decode(message_file):
    #initialize an empty dictionary to store words and numbers
    word_dict = {}

    # read the contents of the message_file
    with open(message_file, 'r') as file:
        for line in file:
            #split each line into a list of words
            words = line.split()

            #extract the number and word from the line
            num = int(words[0])
            word = ' '.join(words[1:])

            #store the word in the dictionary with its associated number
            word_dict[num] = word

    #sort the keys of the dictionary to get the ordered list of words
    ordered_words = [word_dict[key] for key in sorted(word_dict.keys())]

    #join the ordered words into a string and return
    decoded_message = ' '.join(ordered_words)
    return decoded_message

#example usage:
message_file_path = 'path/to/your/message_file.txt'
decoded_message = decode(message_file_path)

print(decoded_message)