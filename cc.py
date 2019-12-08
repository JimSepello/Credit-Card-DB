#enter credit card info
credit_card_number = ''
credit_cards = []
exp_dates = []
credit_card = ''
another_card = 'y'
dictcc = {''}
another_card = input('Do you want to enter a new card? (enter n to exit)')
while another_card != 'n':
    credit_card_number = input("enter a cedit card number")
    credit_cards.append(credit_card_number)
    exp_date = input("Enter the Expiration Date ")
    exp_dates.append(exp_date)
    dictcc = dict(zip(credit_cards, exp_dates))

    another_card = input('Do you want to enter a new card? (enter n to exit)')
print(dictcc)
