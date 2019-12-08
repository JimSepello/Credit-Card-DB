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
	print(' ')
	printall()
	

def printall():
	for card in c.execute('SELECT ROWID, * FROM cards'):
		print(card)



createTABLE()


print(' ')
print('the current cards in database are:')
print(' ')


printall()





while enterAcard == 'yes' or enterAcard == 'y':
	print(' ')
	enterAcard = input('Do you want to enter a card?: ')
	if enterAcard.lower() == 'yes' or enterAcard.lower() == 'y':
		entercard()
	else: 
		printall()
		exit()







printall()
conn.close()
