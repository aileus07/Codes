stack = []

def push_Book():
    
    
    n = int(input('Number of book to add to the stack: '))
    
    for i in range(n):
        book_name = input('Enter the name of the book: ')
        book_no = int(input('Enter the ID of the book: ')) 
        price = int(input('Enter the price of book (in Rs): '))
    
        book = [book_name,book_no,price]
        stack.append(book)
        
        print('Book added to stack!')
        
        
           
def pop_Book():
    
    if len(stack) == 0:
        print('*'*6,'Under flow!','*'*6)
    else:
        book = stack.pop()
        print(book)
        
    
    
    
def show_Book():
    
    if len(stack) == 0:
        print('*'*6,'Under flow!','*'*6)
    else:
        for i in stack:
            print(f'     Name:{i[0]} Book ID: {i[1]}  Book Price: {i[2]}')
        
 
       

def main_menu():
    
    while True:
        
        print("1. Add New Books")
        print("2. Remove a Book")
        print("3. Show Books")       
        print("3. Exit")       
        
        try:
            choice = int(input(' Enter your choice (1-4): '))
            
            if choice == 1:
                push_Book()
                
            if choice == 2:
                pop_Book()
                
            if choice == 3:
                show_Book()
                
            if choice == 4:
                exit()
                
        except ValueError:
            print("\n*** Error: Please enter a number between 1-3 ***")                
            
# main_menu()


import pickle

def add_customer():
    with open('cus.dat', 'ab') as f:
        n = int(input(' Enter the number to enteries to enter: '))
        for i in range(n):
            name = input('  Enter your name: ')
            age = int(input('   Enter your age: '))
            cus_id = int(input('    Enter your customer ID: '))
        
            details = [name, age, cus_id]

            pickle.dump(details,f)
            print('Customer added to database!')


def show_cus():
    data = []
    with open('cus.dat', 'rb') as f:
        while True:
            try:
                holder = pickle.load(f)
                data.append(holder)
            except EOFError:
                print('All data has been read successfully!')
                break
                
        for i in data:
            print(i)
        
def remove_cus():
    found = 0 
    new_data = []
    
    id = int(input('Enter the ID to delete: '))
    with open('cus.dat', 'rb') as f:
        while True:
            try:
                holder = pickle.load(f)
                if holder[2] == id:
                    found = 1
                    continue
                else:
                    new_data.append(holder)
            except EOFError:
                break
            
    if found == 1:
        with open('cus.dat', 'wb') as f:
            for i in new_data:
                pickle.dump(i,f)       
        print(f'Customer id:{id} has beed removed successfully!')
            
    
def main_menu2():
    
    while True:
        
        print("1. Add New Customers")
        print("2. Show all Customers")
        print("3. Remove Customer")
        print("4. Exit")       
        
        try:
            choice = int(input(' Enter your choice (1-4): '))
            
            if choice == 1:
                add_customer()
                
            if choice == 2:
                show_cus()
                
            if choice == 3:
                remove_cus()
            
            if choice == 4:
                exit()
            
                
        except ValueError:
            print("\n*** Error: Please enter a number between 1-4 ***")

main_menu2()