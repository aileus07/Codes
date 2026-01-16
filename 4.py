f = open("File Handling\\Data Base\\4.txt" , "r")
# for i in range(1,11):
#     number = str(i) 
#     f.write(number+"\n")
data = f.read()
try:
    for i in data:
        print(i)
        
except EOFError:
    raise ValueError("No more data")
    