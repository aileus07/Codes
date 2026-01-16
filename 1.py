def c_words():
    lc=uc=0
    with open(r"Files\File Handling\Data Base\practice.txt", "r") as f:
        data = f.read()
        for ch in data:
            if ch.isalpha() and ch.isupper():
                uc += 1
            if ch.isalpha() and ch.islower():
                lc += 1
    print(lc,uc)
# c_words()

def vowel_count():
    vowel = const = 0
    with open(r'Files\File Handling\Data Base\practice.txt', 'r') as f:
        data = f.read()
        for ch in data:
            if ch in 'aeiouAEIOU':
                vowel += 1
            else:
                const += 1   
            
    print(vowel,const)
# vowel_count()

def test():
    with open(r'Files\File Handling\Data Base\practice.txt', 'r') as f:
        data = f.readlines()
        # print(type(data))
        for i in range(len(data)):
            line = data[i].rstrip()
            line = line.split()
            if line[0].lower() == 'you':
                print(' | '.join(line))
            
            
            # else:
            #     print('no')
# test()
# with open(r'Files\File Handling\Data Base\practice.txt', 'a') as f:
#     names = ['Alice', 'Bob', 'Charlie', 'Diana']
    # f.writelines(names)
    
    

def capitalize_sentence():
    with open(r'Files\File Handling\Data Base\practice.txt', 'r') as f1:
        data = f1.read()
        str = ''
        capNext = True
        for ch in data:
            if capNext and ch.isalpha():
                str += ch.upper()
                capNext = False
            else:
                str += ch
            if ch == '.':
                capNext = True
            
        print(str)
    
    
    
capitalize_sentence()