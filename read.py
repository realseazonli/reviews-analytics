data = []
count = 0
with open('reviews.txt', 'r') as f :
    for line in f :
        data.append(line.strip())
        count += 1
        if count % 1000 == 0 :
            print(len(data))
print('档案读取完了，总共有', len(data), '个留言')