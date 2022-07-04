temp_dic = {}

with open('nyc_weather.csv','r') as d:
    for line in d:
        tokens = line.split(',')
        day = tokens[0]
        try:
            temp = int(tokens[1])
            temp_dic[day] = temp
        except:
            print('Invalid temperature. try again..')

print(temp_dic['Jan 9'])
print(temp_dic['Jan 4'])