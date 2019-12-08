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

enterAcard = 'yes'

def entercard():
	ccname = input('Enter the name of the new card: ')
	ccnumber = input('Enter the card number: ')
	ccexp_date = input('Enter the Expiration date: ')
	cccsv = input('Enter the CSV number from the back of the card: ')
	c.execute("INSERT INTO cards VALUES (?, ?, ?, ?)",(ccname, ccnumber, ccexp_date, cccsv));
	conn.commit()
	printall()
	

def printall():
	for card in c.execute('SELECT * FROM cards'):
		print(card)

createTABLE()

print('the current cards in database are:')
printall()

while enterAcard == 'yes':
	enterAcard = input('Do you want to enter a card?: ')
	if enterAcard.lower() == 'yes':
		entercard()
	else: 
		printall()
		exit()

printall()
conn.close()

