import pickle

def add_Players():
    # with open('player.dat','ab') as f:
        # x = int(input('Number of players to add: '))
        # for i in range(x):
        #     name = input('Enter the name of the player: ')
        #     age = int(input('Enter the age of the player: '))
        #     id = int(input('Enter the ID of the player : '))
            
        #     details = {id: [name,age]}
            
        #     pickle.dump(details,f)
            
    with open('player.dat','ab') as f:
        while True:
            name = input('Enter the name of the player: ')
            age = int(input('Enter the age of the player: '))
            id = int(input('Enter the ID of the player : '))
            details = {id: [name,age]}
            
            pickle.dump(details,f)
            
            print('Player added successfully!')
            
            bool = input('Do you want to enter more players?(Y/n): ')
            
            if bool.upper() == 'Y':
                continue
            elif bool.upper() == 'N':
                break
            else:
                print('Enter a valid option!')
               
def delete_Player():
    search_id = int(input('Enter the ID of the player to remove: '))
    with open('player.dat','rb') as f:
        data = []
        found = 0
        while True:
            try:
                holder = pickle.load(f)
                if search_id in list(holder.keys()):
                    found += 1   
                    print(f'Successfully deleted player with ID: {search_id}')
                    continue
                else:
                    data.append(holder)
            except EOFError:
                break
            
    with open('player.dat','wb')as f :
        for i in data:
            pickle.dump(i,f)
                
def show_Players():
    with open('player.dat','rb') as f:
        data = []
        while True:
            try:
                holder = pickle.load(f)
                data.append(holder)
            
            except EOFError:
                print('Successfully read all the data!\n')
                break
            
    for i in data:
        # print(i, type(i))
        for id, l in i.items():
            print(f'ID:{id} Name:{l[0]} Age:{l[1]}\n')
    
def main_Menu():
    while True:
        print("1. Add New Player")
        print("2. Show all Player")
        print("3. Remove Player")
        print("4. Exit") 
        choice = int(input('Enter your choice(1-4): '))
                
        match choice:
            case 1:
                add_Players()
            case 2:
                show_Players()
            case 3:
                delete_Player()
            case 4:
                exit()

main_Menu()           