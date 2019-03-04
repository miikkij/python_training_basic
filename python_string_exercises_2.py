temp_str = 'Anomalocaris'
print(temp_str)
result = temp_str.index('o')
print(result)
result = temp_str.index('r')
print(result)

temp_str = 'Waging on the purple drone'
print(temp_str)
print("Substring: " + temp_str[len(temp_str)//2:len(temp_str)])
result = temp_str[len(temp_str)//2:len(temp_str)].index('on')
print(temp_str.find)
print(result)

temp_str = 'Waging on the purple drone'
result = temp_str.index('on')
print(result)

temp_str = ''

temp_str = 'There try is a dazzling bright world out there, waiting for us to explore.'
result = temp_str.index('a', int(len(temp_str)/2), len(temp_str))
print(result)

result = temp_str.index('a', 0, int(len(temp_str)/2))
print(result)

temp_str = '91342391'
print(temp_str)
print(temp_str.lstrip('913').rstrip('391'))
print(temp_str[3:5])

temp_str = '-== Warning! ==-'
print(temp_str)
print(temp_str.lstrip('-== ').rstrip('! ==-'))
print(temp_str[4:11])
print(temp_str.index('W'))
print(temp_str[temp_str.index('W'):temp_str.index('!')])


temp_str = 'a loooooooooooooooooooong word'
print(temp_str.count('o'))

temp_str = 'Something out of nothing? I really doubt we can do it anytime soon..'
print(temp_str.count('n', 0, int(len(temp_str)/2)))

temp_str = 'what,if,we,have,no,choice?....'
print(temp_str.replace(',', ' ').replace('.', '').capitalize())

temp_str = 'first half second half'
print(temp_str[:len(temp_str)//2])