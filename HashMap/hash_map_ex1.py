# exercise 1
arr = []
with open('nyc_weather.csv', 'r') as f:
    for line in f:
        tokens = line.split(',')
        try:
            temp = int(tokens[1])
            arr.append(temp)
        except:
            print("Invalid temperature..Try again..")

# except inbuilt max function
# let's build own function for get the max
def get_max(array):
    maximum = 0
    for element in array:
        if maximum < element:
            maximum = element
    return maximum


arr
print(arr)
print(sum(arr[0:])/len(arr[0:]))
print(max(arr[0:]))
print(get_max(arr))
