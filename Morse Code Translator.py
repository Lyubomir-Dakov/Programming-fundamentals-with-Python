my_string = (input().split('|'))
result_list = []

my_dict = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I',
           '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R',
           '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z'}

for word in my_string:
    my_word = word.strip().split(' ')
    the_word = ''
    for symbol in my_word:
        letter = my_dict[symbol]
        the_word += letter
    result_list.append(the_word)

print(' '.join(result_list))


