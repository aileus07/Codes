with open("File Handling\\Data Base\\practice.txt", 'w') as f:
    data = ['Hi everyone','we are File I/O','using Java','I like programming in Java','learning']
    f.write("\n".join(data))
    
def replace():
    with open('File Handling\\Data Base\\practice.txt','r+') as f:
        data = f.readlines()
        n_data = []
        for line in data:
            if "java" in line.lower():
                n_line = line.split()
                index = n_line.index("Java")
                n_line[index] = 'Python'
                n_word = ''
                for word in n_line:
                    n_word += str(word + ' ')
                n_word = n_word.strip()
                n_data.append(n_word+'\n')
            else:
                n_data.append(line)
        n_data = "".join(n_data)
        f.seek(0)
        f.write(n_data)
# replace()

############## Or ###################
with open('File Handling\\Data Base\\ practice.txt','r') as f:
    data = f.read()
new_data = data.replace('Java','Python')
# print(new_data)

with open('File Handling\\Data Base\\ practice.txt','w') as f:
    f.write(new_data)
#####################################


def search():
    with open('File Handling\\Data Base\\practice.txt','r') as f:
        data = f.readlines()
        for line in data:
            if "learning"  not in line.lower():
                continue
            else:
                return True
    return False
# print(search())


def line_no(word):
    with open('File Handling\\Data Base\\practice.txt','r') as f:
        data = f.readlines()
        for line in data:
            if word.lower() in line.lower():
                index = data.index(line)
                return index + 1
    return -1

print(line_no('learning'))