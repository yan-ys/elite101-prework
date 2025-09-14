import time
def book_a_taxi():
    print('----------Booking A Taxi Page----------')
    time = input('What time you would like your taxi to arrive X:XX: ')
    am_or_pm = input('AM or PM: ')
    try:
        distance = int(input('How many miles away is your destination: '))
        confirm_booking = input('Enter 1 to confirm your order or any other key to cancel: ')
        if confirm_booking == '1':
            print(f'----------Receipt For {name}----------')
            print(f'Taxi order confirmed. Your taxi will arive at {time}{am_or_pm}.')
            print('Your total will be ' + str(1.5*distance) + " dollars")
        else:
            print('Taxi order canceled.')
    except:
        print('Invalid input...returning to main menu.')
        print('Taxi order canceled.')
def review():
    print('----------Reviews Page----------')
    app_or_driver = input('Enter 1 to leave a review for the app or 2 to review your driver: ')
    if app_or_driver == '1':
        rating = input('Rate us from 1-5 stars: ')
        if rating == '5' or '4':
            print('Thank you!')
        else:
            print('How can we improve? ')
            feedback = input('Enter your valued feedback: ')
    else:
        review_who = input('Enter the name of the driver you want to review: ')
        rating = input('Rate your driver from 1-5 stars: ')
        print(f'You rated {review_who} {rating} stars.')
        if rating == '5' or rating == '4':
            print('Thank you for your feedback on our drivers.')
        else:
            print('What went wrong? ')
            feedback = input('Enter your valued feedback: ')
            refund_wanted = input('Enter 1 if you would like to request a refund: ')
            if refund_wanted == '1':
                refund()
def refund():
    print('----------Refunds Page----------')
    want_a_refund = input('Enter 1 to confirm your refund request: ')
    if want_a_refund == '1':
        refund_to_where = input('Enter 1 for app credit refund (with bonus credit) or 2 to refund the funds to the original payment method')
        if refund_to_where == '1':
            print('Refund request sent...if request is approved you will recieve bonus app credit.')
        else:
            print('Refund request sent...if request is approved you will recieve your refunded funds in your original payment method.')
    else:
        print('Refund request canceled...')
    


def chatbot(choice):
    while choice != '4':
        print(f'\nHi, {name} how can I help you?')
        print('\t1. book a taxi\n\t2. leave a review\n\t3. request a refund\n\t4. exit the conversation')
        choice = input('Enter the number of your choice: ')
        if choice == '1':
            book_a_taxi()
        elif choice == '2':
            review()
        elif choice == '3':
            refund()
        elif choice == '4':
            print(f'Goodbye {name}! Thank you for using the taxi chatbot.')
        else:
            print('Please enter a valid option.')
        time.sleep(2)
        


print("Welcome to taxi chatbot")
choice = None
name = input('Enter your name: ')
try:
    age = int(input('Enter your age: '))
except:
    print('Please enter a valid age...restarting chatbot')
    sys.exit()
if age < 13:
    print('You need to be at least 13 to use the taxi chatbot\nEnding conversation...')
else:
    chatbot(choice)