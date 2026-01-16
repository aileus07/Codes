with open("File Handling\\Data Base\\ numbers.txt", 'w') as f:
    for i in range(1,12):
        f.write(str(i) + ",")
    
with open("File Handling\\Data Base\\ numbers.txt", 'r') as f:
    data = f.read()
    x = 0
    data = data.split(',')
    for num in data:
        if num.isdigit():
            # print(num)
            if  int(num)%2 == 0:
                x += 1
        else:
            continue
print(x)