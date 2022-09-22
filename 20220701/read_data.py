file = open('data.txt', encoding='utf-8')
a = file.readlines()
d = {}
for line in a:
    # print(line)
    # print(line.split())

    words = line.split()
    for word in words:
        if d.get(word) == None:
            d[word] = 1
        else:
            d[word] = d[word] + 1

print("1111",d)
a = d.items()
# print(a)
# print(sorted(d.items(), key=lambda kv:kv[1], reverse=True))

# for key in a:
#     print(key)

b = sorted(d.items(), key=lambda kv: kv[1], reverse=True)
print(b)
f = open('E:/data2.txt', 'w', encoding='utf-8')

for i in b:
    f.writelines(str(i[0]) + ':' + str(i[1]) + '\n')
f.close