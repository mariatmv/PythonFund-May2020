line = input()
new = line.split('.')
extension = new[1]
zdr = new[0].split('\\')
name = zdr[-1]
print(f'File name: {name}')
print(f'File extension: {extension}')