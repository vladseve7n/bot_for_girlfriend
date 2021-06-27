import re
f2 = open('Clear_compliment.txt', 'w')
with open('New_compliments.txt') as f:
    text = f.readline()
    answer = re.findall(r'\d*..(\D*)\d*', text)
    for i in answer:
        f2.write(i + '\n')
