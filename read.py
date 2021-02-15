
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

# names = ['Tom', 'Simon', 'Mike', 'angerina']
new = []
for review in data :
    if len(review) < 100 :
        new.append(review)
    else :
        pass
print(len(new))

good = []
for review in data :
    if 'good' in review :
        good.append(review)
print(len(good))
print(good[0])