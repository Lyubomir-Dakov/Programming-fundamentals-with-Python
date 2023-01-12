text = input()
vowels = ['a', 'o', 'u', 'e', 'i']
text = ''.join([x for x in text if x not in vowels])
print(text)