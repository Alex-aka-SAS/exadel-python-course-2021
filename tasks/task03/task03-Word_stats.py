import string

text = ["The world is mine.",
        "World Hello!",
        "Hello, how are you?"
        ]
text1 = [y for x in text for y in x.split(' ')]
text1 = str(text1)
for p in string.punctuation:
    if p in text1:
        text1 = text1.replace(p, '')
text1 = str(text1).lower()
print(text1)
words_list = text1.split()
stats = {}
for word in words_list:
    if word not in stats:
        stats[word] = 0
    stats[word] += 1
print(stats)

# tpl = tuple(text1)
# s0 = tpl[0:4]
# print(s0)
# s1 = tpl[4:6]
# print(s1)
# s2 = tpl[6:10]
# # print(s2)
