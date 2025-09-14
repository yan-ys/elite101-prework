print("Welcome to taxi chatbot")
name = input('Enter your name: ')
try:
    age = int(input('Enter your age: '))
    if age < 13:
        choice = '4'
        print('You need to be at least 13 to use the taxi chatbot.\n Ending conversation...')
except:
    print('Please enter a valid age...restarting chatbot')
    choice = '4'
choice = None


while choice != '4':
    print(f'\nHi, {name} how can I help you?')
    print('\t1. book a taxi\n\t2. leave a review\n\t3. request a refund\n\
    \t4. exit the conversation')
    choice = input('Enter the number of your choice: ')
    if choice == '1':
        print('placeholder')
    elif choice == '2':
        print('placeholder')
    elif choice == '3':
        print('placeholder')
    elif choice == '4':
        print(f'Goodbye {name}! Thank you for using the taxi chatbot.')
    else:
        print('Please enter a valid option.')
        
