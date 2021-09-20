#! python3

import re, pyperclip

# Create a regex object for dates in the DD/MM/YYYY format

dateRegex = re.compile(r''' 

	(0[1-9] | [12]\d | 3[01])	# Days from 01 to 31
	/							# / separator
	(0[1-9] | 1[0-2])			# Months from 01 to 12
	/							# / separator
	([12]\d\d\d)				# Year from 1000 to 2999
	''', re.VERBOSE)

# Get the text off the clipboard

text = pyperclip.paste()

# Extract the dates from this text

extractedDates = dateRegex.findall(text)

# Store these strings in variables "day" "month" "year"

day = []
month = []
year = []

for dates in extractedDates:
	day.append(int(dates[0]))
	month.append(int(dates[1]))
	year.append(int(dates[2]))

#TODO: Detect if a date is valid

isValid = []
30daysMonths = [04, 06, 09, 11]

def isLeapYear(someYear):
	if someYear%4 == 0 and someYear%100 != 0:
		return True
	elif someYear%400 == 0:
		return True
	else:
		return False

for i in range(len(day)):
	if month[i] in 30daysMonths and day[i] == 31:
		isValid.append('not valid')
	elif month[i] == 02 and day[i] > 29:
		isValid.append('not valid')
	elif month[i] == 02 and day[i] == 29 and not isLeapYear(year[i])
		isValid.append('not valid')
	else:
		isValid.append('valid')



#TODO: Copy the extracted dates and the validation infos to the clipboard