def calculator():
    print('\n-------------------------------------')
    print('CSU BOOK CLUB AWARD POINTS CALCULATOR')
    print('-------------------------------------')
    
    books_purchased = int(input("How many books did you purchase this month? "))
    
    if books_purchased == 0:
        points = 0
        message = "Purchase at least 2 Books in a month to start earning award points!"
    elif 2 <= books_purchased < 4:
        points = 5
        message = "Great start! Purchase 4 books or more in a month to earn some more award points!"
    elif 4 <= books_purchased < 6:
        points = 15
        message = "Good work! Purchase 6 books or more in a month to earn even more award points!"
    elif 6 <= books_purchased < 8:
        points = 30
        message = "Amazing! You are almost there. Purchase 8 books or more in a month to earn even MORE award points!"
    elif books_purchased >= 8:
        points = 60
        message = "Book Superstar!! You earned the max amount of award points this month. See you next month!"
    else:
        points = 0
        message = "Purchase at least 2 Books in a month to start earning award points!"

    print(f"You earned {points} CSU Book Club Award Points this month.")
    print(f'{message}\n')
    
    end_input=input('Type e to exit or r to restart')
    if end_input =='e':
        exit
    elif end_input =='r':
        calculator()
calculator()
