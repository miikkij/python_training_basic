import re

n = int(input())
regex_strings = list()

# read n lines of input
for i in range(n):
    regex_strings.append(input())

for regex in regex_strings:
    try:
        re.compile(regex)
        is_valid = True
    except re.error:
        is_valid = False
    print(is_valid)

