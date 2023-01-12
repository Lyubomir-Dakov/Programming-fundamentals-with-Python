num = int(input())

for chr_1 in range(97, 97 + num):
    for chr_2 in range(97, 97 + num):
        for chr_3 in range(97, 97 + num):
            result = chr(chr_1) + chr(chr_2) + chr(chr_3)
            print(result)