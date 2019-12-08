import sqlite3
conn = sqlite3.connect('cc.db')
c = conn.cursor()

def createTABLE():
    c.execute("""CREATE TABLE IF NOT EXISTS cards (
        name text,
        ccnumber integer,
        exp_date text,
                    csv integer
        )""")
    conn.commit()

def enterCards():
    enterAcard = 'yes'
    entercard()
    while enterAcard == 'yes' or enterAcard == 'y':
        print(' ')
        enterAcard = input('enter another card? (y or n): ')
        if enterAcard.lower() == 'yes' or enterAcard.lower() == 'y':
            entercard()
    else:
        printall()

def bbentercard():
    print(' ')
    ccname = input('Enter the name of the new card: ')
    ccnumber = input('Enter the card number: ')
    ccexp_date = input('Enter the Expiration date: ')
    cccsv = input('Enter the CSV number from the back of the card: ')
    c.execute("INSERT INTO cards VALUES (?, ?, ?, ?)",(ccname, ccnumber, ccexp_date, cccsv));
    conn.commit()
    print(' ')
    printall()

def deleteAcard():
    delCard = input('/nWhich card do you want to delete?: ')
    c.execute ("DELETE from cards WHERE ROWID = ?", delCard);
    conn.commit()
    print(' ')
    print('the current cards in database are:')
    print(' ')
    printall()

def editAcard():
    print(' ')
    printall()
    print(' ')
    cardToEdit = input('Which CARD do you want to edit?: ')
    print(' ')
    print(' 1 Name of Card')
    print(' 2 Card Number')
    print(' 3 Expiration Date')
    print(' 4 CSV')
    print(' ')
    colToEdit = input('Which COL do you want to edit?: ')
    if colToEdit == '1':
        newvalue = input('What is the new name?: ')
        c.execute("UPDATE cards SET name = ? WHERE ROWID=?",(newvalue, cardToEdit));
        conn.commit()
    elif colToEdit == '2':
        newvalue = input('What is the new number?: ')
        c.execute("UPDATE cards SET ccnumber = ? WHERE ROWID=?",(newvalue, cardToEdit));
        conn.commit()
    elif colToEdit == '3':
        newvalue = input('What is the new expiration date?: ')
        c.execute("UPDATE cards SET exp_date = ? WHERE ROWID=?",(newvalue, cardToEdit));
        conn.commit()
    elif colToEdit == '4':
        newvalue = input('What is the new csv value?: ')
        c.execute("UPDATE cards SET csv = ? WHERE ROWID=?",(newvalue, cardToEdit));
        conn.commit()
    else:
        print(' ')
        chosen = str(colToEdit)
        print('YOU CHOSE ' + colToEdit + ' WHICH IS OUT OF RANGE')
        print('please choose 1,2 3 or 4')

def printall():
	print(' ')
	for card in c.execute('SELECT ROWID, * FROM cards'):
		print(card)
	print(' ')

createTABLE()

print(' ')
print('the current cards in database are:')
print(' ')
printall()


choice = '1'
while choice != '4':
	print(' ')
	print('What do you want to do? ')
	print(' ')
	print(' 1 Get a list of cards in the database? ')
	print(' 2 Enter a new card? ')
	print(' 3 Delete a card? ')
	print(' 4 Edit a card? ')
	print(' 5 Exit? ')


	print(' ')
	choice = input('choose a number: ')
	if choice == '1':
		printall()

	elif choice == '2':
		entercard()

	elif choice == '3':
		deleteAcard()

	elif choice == '4':
		editAcard()

	elif choice == '5':
		print('Exited the Program')
		exit()

	else:
		print(' ')
		chosen = str(choice)
		print('YOU CHOSE ' + chosen + ' WHICH IS OUT OF RANGE')
		print('please choose 1,2 3 or 4')


printall()
conn.close()

