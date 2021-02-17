
data = []
count = 0
len_list = []
total = 0
result = 0
word_count = {}
with open('reviews.txt', 'r') as f :
    for line in f :
        data.append(line.strip())
        count += 1
        if count % 1000 == 0 :
            print(len(data))
print('档案读取完了，总共有', len(data), '个留言')
for d in data :
    words = d.split()
    for word in words :
            if word in word_count:
                word_count[word] += 1
            else :
                word_count[word] = 1
while True:
    search = input('请输入要查询的单词（输入q/Q退出查询）：')
    if search == 'q' or search == 'Q':
        print('感谢使用查询功能')
        break
    elif search in word_count:
        print(search, '的出现次数为：', word_count[search])
    else:
        print(search, '查询不到')

for word in word_count:
    if word_count[word] > 2000000:
        print(word, ':', word_count[word])


# # names = ['Tom', 'Simon', 'Mike', 'angerina']
# new = []
# for review in data :
#     if len(review) < 100 :
#         new.append(review)
#     else :
#         pass
# print(len(new))# 

# # good = []
# # for review in data :
# #     if 'good' in review :
# #         good.append(review)
# # print(len(good))
# # print(good[0])# 

# good = [d for d in data if 'good' in d]
# print(len(good))
# print(good[1])