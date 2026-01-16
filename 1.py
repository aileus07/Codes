import csv


def add_Player():
    with open('player.csv','a',newline = '') as f:
        while True:
            w = csv.writer(f,delimiter='|')
            name = input('Enter the name of the player: ')
            sport = input('Enter the sport: ')
            age = int(input('Enter the age: '))
            p_id = int(input('Enter the player ID: '))
            
            deatils = [p_id,name,age,sport]
            w.writerow(deatils)
            
            bool = input('Do you want to enter more data(Y/n): ')
            if bool.lower() == 'y':
                continue
            elif bool.lower() == 'n':
                break
# add_Player()            

def show_Player():
    with open('player.csv', 'r') as f:
        reader = csv.reader(f)
        data = list(reader)
        for i in data:
            print(" ".join(i))
show_Player()