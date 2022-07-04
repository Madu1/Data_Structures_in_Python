# with open('poem.txt','r') as f:
#     for line in f:
#         print(line)

poem_dic = {}
with open('poem.txt','r') as f:
    for line in f:
        tokens = line.split(' ')
        for token in tokens:
            token = token.replace('\n','')
            if token in poem_dic:
                poem_dic[token] += 1
            else:
                poem_dic[token] = 1


print(poem_dic)
