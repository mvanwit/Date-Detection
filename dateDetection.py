#! python3

import re, pyperclip

# Create a regex object for dates in the DD/MM/YYYY format

dateRegex = re.compile(r''' 
	(
	(0[1-9] | [12]\d | 3[01])	# Days from 01 to 31
	/							# / separator
	(0[1-9] | 1[0-2])			# Months from 01 to 12
	/							# / separator
	([12]\d\d\d)
	)				# Year from 1000 to 2999
	''', re.VERBOSE)

# Get the text off the clipboard

text = pyperclip.paste()

# Extract the dates from this text

extractedDates = dateRegex.findall(text)

# Store these strings in variables "day" "month" "year"

allDates = []
day = []
month = []
year = []

for dates in extractedDates:
	allDates.append(dates[0])
	day.append(dates[1])
	month.append(dates[2])
	year.append(dates[3])

# Detect if a date is valid

isValid = []
thirtyMonths = ['04', '06', '09', '11'] #April, June, September, November have 30 days

	# Function that detects if a year is a leap year
def isLeapYear(someYear):
	if someYear%4 == 0 and someYear%100 != 0:
		return True
	elif someYear%400 == 0:
		return True
	else:
		return False

combinedDateValidation = []
for i in range(len(allDates)):
	if month[i] in thirtyMonths and int(day[i]) == 31: #31 days in a 30 days month
		isValid.append('not valid')
	elif month[i] == '02' and int(day[i]) > 29: #more than 29 days in February
		isValid.append('not valid')
	elif month[i] == '02' and int(day[i]) == 29 and not isLeapYear(int(year[i])): #29 days in February not on a leap year
		isValid.append('not valid')
	else:
		isValid.append('valid')

# Copy the extracted dates and the validation infos to the clipboard	
	combinedDateValidation.append(allDates[i] + '   ' + isValid[i])


	
result = '\n'.join(combinedDateValidation)

pyperclip.copy(result)

#UPGRADE IDEA
#Call the program with an argument, to modify the date format
#
#			for example : dateDetection [YYYY/MM/DD]
#