num_words = int(input())
my_dict = {}

for _ in range(num_words):
    word = input()
    synonym = input()
    if word not in my_dict:
        my_dict[word] = []
    my_dict[word].append(synonym)

for (word, synonyms) in my_dict.items():
    print(f"{word} - {', '.join(synonyms)}")

