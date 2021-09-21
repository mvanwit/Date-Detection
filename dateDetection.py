#! python3

import re, pyperclip, sys

#Dictionary of output formats

helpText = 'dateDetection [format] [separator]\n\n[format]\n"validation"\n"DMY"(by default)\n"MDY"\n"YMD"\n\n[separator]\n"/" by default if not specified\nany string\n"space" for " " separator'
message = ''
dateFormats = {
	'validation': lambda: dateFormating.append(allDates[i] + '   ' + isValid[i]),
	'DMY': lambda: dateFormating.append(day[i] + argSep + month[i] + argSep + year[i]),
	'MDY': lambda: dateFormating.append(month[i] + argSep + day[i] + argSep + year[i]),
	'YMD': lambda: dateFormating.append(year[i] + argSep + month[i] + argSep + day[i])
}



#Check if an argument has been passed and set default values if not
if len(sys.argv) == 1: #default values if no arguments
	argFormat = 'DMY'
	argSep = '/'
elif sys.argv[1] == 'help': #help message
		print(helpText)
		sys.exit()
elif len(sys.argv) > 1: #if 1 argument
	argFormat = sys.argv[1]
	if len(sys.argv) > 2:#if 2 arguments
		if sys.argv[2] == 'space':
			argSep = ' '
		else:
			argSep = sys.argv[2]
	else: 
		argSep = '/' #default if only format argument

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

dateFormating = []
	# Date validation
for i in range(len(allDates)):
	if month[i] in thirtyMonths and int(day[i]) == 31: #31 days in a 30 days month
		isValid.append('not valid')
	elif month[i] == '02' and int(day[i]) > 29: #more than 29 days in February
		isValid.append('not valid')
	elif month[i] == '02' and int(day[i]) == 29 and not isLeapYear(int(year[i])): #29 days in February not on a leap year
		isValid.append('not valid')
	else:
		isValid.append('valid')


# Date formating depending on argument
	if argFormat in dateFormats:
		dateFormats[argFormat]()
		message = 'Dates have been copied to the clipboard in the "' + argFormat + '" format with "' + argSep + '" separator.'
	else:
		message = 'Error : There is no "' + argFormat + '" format. Try dateDetection help for a list of formats.'
		break

if allDates == []:
        message = 'No dates detected in copied text. This program only find dates DD/MM/YYYY format.'
        
print(message)	
result = '\n'.join(dateFormating)

pyperclip.copy(result)
