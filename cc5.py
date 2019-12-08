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






def entercard():
	ccname = input('Enter the name of the new card: ')
	ccnumber = input('Enter the card number: ')
	ccexp_date = input('Enter the Expiration date: ')
	cccsv = input('Enter the CSV number from the back of the card: ')
	c.execute("INSERT INTO cards VALUES (?, ?, ?, ?)",(ccname, ccnumber, ccexp_date, cccsv));
	conn.commit()
	print(' ')
	printall()
	

def printall():
	for card in c.execute('SELECT ROWID, * FROM cards'):
		print(card)

def enterCards():
	enterAcard = 'yes'
	entercard()
	while enterAcard == 'yes' or enterAcard == 'y':
		print(' ')
		enterAcard = input('enter another card?: ')
		if enterAcard.lower() == 'yes' or enterAcard.lower() == 'y':
			entercard()
	else: 
		printall()
		#exit()

createTABLE()


print(' ')
print('the current cards in database are:')
print(' ')


printall()
print(' ')

choice = '1'
while choice != '4':
	print('What do you want to do? ')
	print('1 Enter a new card')
	print('2 Delete a card')
	print('3 Edit a card')
	print('4 Exit')
	choice = input('choose a number: ')
	if choice == '1':
		enterCards()
	elif choice == '2':
		pass
		#deleteAcard()
	elif choice == '3':
			pass
			#editAcard()
	elif choice == '4':
		print('Exiting')
		exit()
	else:
		print('please choose 1,2 3 or 4')











printall()
conn.close()

