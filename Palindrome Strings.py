line_1 = input().split(' ')
palindrome = input()

found_palindromes = [x for x in line_1 if x == x[::-1]]
number_of_occurrences = 0
for x in found_palindromes:
    if palindrome == x:
        number_of_occurrences += 1

print(found_palindromes)
print(f'Found palindrome {number_of_occurrences} times')
