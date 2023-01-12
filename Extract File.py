line_1 = input().split('\\')
file_extension = line_1[-1].split('.')
file_name = file_extension[0]
extension = file_extension[1]

print(f"File name: {file_name}")
print(f"File extension: {extension}")
