version_1 = int(''.join(x for x in input().split('.')))
version_2 = '.'.join([x for x in str(version_1 + 1)])
print(version_2)
