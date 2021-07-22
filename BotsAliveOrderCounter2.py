
'''
Script for counting number of Bots Alive orders of the combination double bot kit + add-on kits


Create dictionary from csv file
csv file columns: Email, Channel, Product Name, Quantity

ID = email, values = channel purchased, product name, quantity
{'unique email': [(tuple of first order), (tuple of second order),...,(tuple of nth order)]}
{'email': [('channel purchase', 'product name', 'quantity'), ('channel purchase', 'product name','quantity')]}


Created by Brendan McKenna on 10/26/17

'''
import csv
import re
from collections import defaultdict


misc = []
doubleBotKitsWithAddOns = 0
customers = []
temp = []

import_file = raw_input("Name of csv to import: ")
print "import successful"

with open(import_file, 'rb') as f:
	f_reader = csv.reader(f)
	print "f_reader successful"
	it = 0
	d = defaultdict(list)
	print d

	for row in f_reader:
		if it == 0:
			it+=1
		else:
			if row[0] in d:
				d[row[0]].append((row[1],row[2],row[3]))
			else:
				d[row[0]] = []
				d[row[0]].append((row[1],row[2],row[3]))
#print "adavidson@icloud.com", len(d['adavidson@icloud.com'])
#print "aecobo@gmail.com", len(d['aecobo@gmail.com'])

# Loop through all keys and each value assigned to each key
# Enumerate double bot kits and add-on kits
# For each pair of double bot kit and add-on kit, add to total
for k in d:
	dbk = 0
	aok = 0
	print d['maureentumenas@gmail.com']
	for v in d[k]:
		if v[1] == 'Bots_alive Kit + 2 Hexbug\xa8 Spiders': 
			dbk += int(v[2]) 
			temp.append(v)
		elif v[1] == 'Add-on Obstacle Vision Block 10 Pack': 
			aok += int(v[2]) 
			temp.append(v)
		elif v[1] == 'BOTS_ALIVE DOUBLE BOT KIT':
			dbk += int(v[2])
			temp.append(v)
		elif v[1] == '2 BOTS_ALIVE DOUBLE BOT KITS':
			dbk += (2*int(v[2]))
			temp.append(v)
		elif v[1] == '10 add-on obstacles':
			aok += int(v[2])
			temp.append(v)
		elif v[1] == 'Add-on kit (promotion)':
			aok += int(v[2])
			temp.append(v)
		elif v[1] == 'bots_alive + 2 Hexbug Spiders':
			dbk += int(v[2])
			temp.append(v)
		else:
			misc += v


	if dbk > 0 and aok > 0:
		temp.insert(0,[k])
		customers.extend(temp)
		#print "customers",customers
		if dbk >= aok:
			doubleBotKitsWithAddOns += aok	
		else:
			doubleBotKitsWithAddOns += dbk
	del temp[:]

print "Total number of orders of Double Bot Kits with Add-On Kits: ", doubleBotKitsWithAddOns

listCustomers = raw_input("Would you like to see a list of all customers who ordered the combination of Double Bot Kit and Add-on Kit? yes/no \n")
if listCustomers.lower() == 'yes':
	try:
		output_file = raw_input("Name output file: ")
		with open(output_file, 'wb') as csvFile:
			csvWriter = csv.writer(csvFile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
			for line in customers:
				csvWriter.writerow(line)
			print "CSV file created"
			print "Thank you and have a nice day!"
	except:
		print "Error: something went wrong while creating csv file"
else:
	print "Mission completed"



#TODO: People who used different emails. Compare address and names
#TODO: Compare with billing zip code

