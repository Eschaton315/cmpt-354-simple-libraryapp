import sqlite3
from datetime import datetime, timedelta, date
import datetime
import random
#import string 
conn = sqlite3.connect('Lib.db')

i = 1
while i < 2:
	menu = 0
	#1 = int, 2 = int 3 = string 4 = string
	print("Welcome to the menu \n")
	print("1: Find an item \n")
	print("2: Borrow an item \n")
	print("3: Return an item \n")
	print("4: Donate an item \n")
	print("5: Find an event \n")
	print("6: Participate in an event \n")
	print("7: Recommend me an event \n")
	print("8: Become a library staff \n")
	print("9: Ask for assistance \n")
	print("10: quit")
	
	menu = int(input("Please enter one of the following options: "))
	#print(menu)
	##finding an item
	if menu == 1:
		#print("in 1")
		userInput1 = int(input("Search by name (1), Item ID(2), or borrower ID (3)?: "))
		if userInput1 == 1:
			userInput3 = input("Please Enter the Search key: ")
		else:
			userInput2 = int(input("Please Enter the Search key: "))
		cursor = conn.cursor()
		print("Opened database successfully \n")
		
		with conn:
			cur = conn.cursor()
			if userInput1 == 1:
				userInput6 = "%" + userInput3 + "%"
				myQuery = "SELECT itemID, name, type FROM item WHERE name LIKE :nameKey"
				cur.execute(myQuery,{"nameKey": userInput6})
				rows=cur.fetchall()
				if rows:
					print("We have the following items by that name, " + userInput3 + ": ")
				else:
					print("Unfortunately, we do not have any item by " + userInput3 + "!\n")
				
				
				for row in rows:
					print("\n","ID:",row[0],"Name:", row[1] ,"Type:", row[2])
				print("\n")	
			
			elif userInput2 == 2:
				myQuery = "SELECT itemID, condition, name, type FROM item WHERE itemID=:itemIDKey"
				cur.execute(myQuery,{"itemIDKey": userInput2})
				rows=cur.fetchall()
				if rows:
					print("We have the following items by that ID, " + userInput2 + ": ")
				else:
					print("Unfortunately, we do not have any item by " + userInput2 + "!\n")

				for row in rows:
					print("\n","ID:",row[0],"Name:", row[1] ,"Type:", row[2])
				print("\n")
			
			elif userInput2 == 3:
				myQuery = "SELECT itemID, condition, name, type FROM item WHERE borrowerID=:borrowerIDKey"
				cur.execute(myQuery,{"borrowerIDKey": userInput2})
				rows=cur.fetchall()
				if rows:
					print("We have the following items borrowed by that ID, " + userInput2 + ": ")
				else:
					print("Unfortunately, we do not have any item borrowed by " + userInput2 + "!\n")

				for row in rows:
					print("\n","ID:",row[0],"Name:", row[1] ,"Type:", row[2])
				print("\n")
	
	##Borrowing an item	
	elif menu == 2:
		#print("in 2")
		userInput1 = int(input("Please enter the itemID: "))
		userInput2 = int(input("please enter the member ID: "))
		cursor = conn.cursor()
		print("Opened database successfully \n")
		
		with conn:

			cur = conn.cursor()
			myQuery = "UPDATE item SET borrowerID =:borrowerIDKey, condition = 'b' WHERE itemID =:itemIDKey"
			try:
				cursor.execute(myQuery,{"borrowerIDKey": userInput1,"itemIDKey": userInput2})
			except sqlite3.IntegrityError:
				print("ERROR: There was a problem borrowing the item!\n")     	
				
		if conn:
				conn.commit()
				print("Committed Changes!\n")	

     
	elif menu == 3:
		#print("in 3")
		userInput1 = int(input("please enter the itemID: "))
		cursor = conn.cursor()
		print("Opened database successfully \n")
		
		with conn:
			cur = conn.cursor()
			myQuery = "SELECT dueDate FROM item WHERE itemID=:itemIDKey"
			cur.execute(myQuery,{"itemIDKey": userInput1})
			rows=cur.fetchall()
			comp = rows
			for row in rows:
				comp = row[0]
				year, month, day = map(int, comp.split('-'))
				dateComp = datetime.date(year, month, day)
				#dateComp = datetime.datetime(comp)
			#print(dateComp)
			today = date.today()
			date1 = today - timedelta(30)
			#print(date1)
			if dateComp < date1:
				myQuery = "SELECT fine FROM item WHERE itemID=:itemIDKey"
				cur.execute(myQuery,{"itemIDKey": userInput1})
				rows=cur.fetchall()
				if rows:
					print("This book is returned late, you owe: $" + rows)
			else:
				print("The item is not returned late.")
				
			myQuery = "UPDATE item SET condition = 'a' WHERE itemID =:itemIDKey"
			try:
				cursor.execute(myQuery,{"itemIDKey": userInput1})
				cufsor.execute("")
			except sqlite3.IntegrityError:
				print("ERROR: There was a problem returning the item!\n")   
  				
		if conn:
				conn.commit()
				print("Committed Changes!\n")	
	
	elif menu == 4:
		#print("in 4")
		userInput1 = random.randrange(1,999999,1)
		userInput3 = input("please enter the name: ")
		userInput4 = input("please enter the type: ")
		userInput2 = int(input("please enter the value: "))
		
		cursor = conn.cursor()
		print("Opened database successfully \n")
		
		with conn:
			cur = conn.cursor()
			myQuery = "INSERT INTO item(itemID, name, type, value) VALUES(:itemIDKey, :nameKey, :typeKey, :valueKey)"
			try:
				cur.execute(myQuery,{"itemIDKey":userInput1,"nameKey":userInput3,"typeKey":userInput4,"valueKey":userInput2})
			except sqlite3.IntegrityError:
				print("ERROR: There was a problem adding item to the dabase!\n")      

	elif menu == 5:
		#print("in 5")
		userInput3 = input("please enter the event name: ")
		userInput6 = "%" + userInput3 + "%"
		cursor = conn.cursor()
		print("Opened database successfully \n")
		
		with conn:
			cur = conn.cursor()
			myQuery = "SELECT name, eventID, type, room FROM event WHERE name=:nameKey"
			cur.execute(myQuery,{"nameKey": userInput6})
			rows=cur.fetchall()
			if rows:
				print("We have the following events, :")
			else:
				print("Unfortunately, we do not have any events called " + userInput3 + "!\n")

			for row in rows:
				print("\n","Name:",row[0],"EventID:", row[1] ,"Type:", row[2],"Room:", row[3])
			print("\n")
		
	elif menu == 6:
		#print("in 6")
		userInput1 = int(input("please enter the eventID: "))
		userInput2 = int(input("please enter your memberID: "))
		
		cursor = conn.cursor()
		print("Opened database successfully \n")
		
		with conn:
			cur = conn.cursor()
			myQuery = "INSERT INTO memberEvent(eventID,ID) VALUES(:eventIDKey, :memberIDKey)"
			try:
				cur.execute(myQuery,{"eventIDKey":userInput1,"memberIDKey":userInput2})

			except sqlite3.IntegrityError:
				print("ERROR: There was a problem adding item to the dabase!\n")      

		if conn:
			conn.commit()
			print("Committed Changes!\n")
	
	
	elif menu == 7:
		#print("in 7")
		userInput1 = int(input("Do you prefer books or movies? Answer (0) for movie and (1) for books"))
		
		cursor = conn.cursor()
		print("Opened database successfully \n")
		
		with conn:
			cur = conn.cursor()
			if userInput1 == 0:
				eventType = "%movie%"
				myQuery = "SELECT name, eventID, type, room, date FROM event WHERE type like :eventTypeKey"
				eventType = "movie"
			else:
				eventType = "%book%"
				myQuery = "SELECT name, eventID, type, room, date FROM event WHERE type like :eventTypeKey"
				eventType = "book"
				
			cur.execute(myQuery,{"eventTypeKey":eventType})
			rows=cur.fetchall()
			if rows:
				print("We have the following events, " + eventType + ": ")
			else:
				print("Unfortunately, we do not have any events to recommend \n")

			for row in rows:
				print("\n","Name:",row[0],"EventID:", row[1] ,"Type:", row[2],"Room:", row[3], "Date:", row[4])
			print("\n")
		
	elif menu == 8:
		#print("in 8")
		userInput3 = input("what is your name?: ")
		birthDay = input("Enter you birthday in YYYY-MM-DD format: ")
		year, month, day = map(int, birthDay.split('-'))
		date1 = datetime.datetime(year, month, day)
		userInput4 = input("what is your email?: ")
		gender = input("what is your gender? (M for male, F for female: ")
		
		
		cursor = conn.cursor()
		print("Opened database successfully \n")
		
		with conn:
			cur = conn.cursor()
			myQuery = "INSERT INTO staff(name, DOB, email, gender) VALUES(:nameKey,:DOBKey,:emailKey,:genderKey)"
			try:
				cur.execute(myQuery,{"nameKey":userInput3,"DOBKey":date1,"emailKey":userInput4,"genderKey":gender})

			except sqlite3.IntegrityError:
				print("ERROR: There was a problem adding item to the dabase!\n")      

		if conn:
			conn.commit()
			print("Committed Changes!\n")
	
	elif menu == 9:
		#print("in 9")
		cursor = conn.cursor()
		print("Opened database successfully \n")
		a = "Librarian"
		with conn:
			cur = conn.cursor()
			myQuery = "SELECT name, staffID FROM staff WHERE job=:jobKey"
			cur.execute(myQuery,{"jobKey":a})
			rows=cur.fetchall()
			if rows:
				print("We have the following librarians available, " + userInput1 + ": ")
			else:
				print("Unfortunately, we do not have anyone available. \n")

			for row in rows:
				print("\n","Name:",row[0],"StaffID:", row[1])
			print("\n")
	
	
	elif menu == 10:
		i = 3
	
	else:
		print("invalid input.")
		
		
conn.close()
print("Closed database successfully")
print("have a nice day \n")
