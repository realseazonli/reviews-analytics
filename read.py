
data = []
count = 0
len_list = []
total = 0
result = 0
with open('reviews.txt', 'r') as f :
    for line in f :
        data.append(line.strip())
        count += 1
        if count % 1000 == 0 :
            print(len(data))
print('档案读取完了，总共有', len(data), '个留言')

names = ['Tom', 'Simon', 'Mike', 'angerina']
for review in data :
    total = total + len(review)
result = total / len(data)
print(result)