import re
f = open('2019_largest_cities.txt', 'r')
content = f.read()
print(re.search(r'\tgi[0-9]', content).group())