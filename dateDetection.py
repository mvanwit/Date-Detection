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
	day.append(dates[0])
	month.append(dates[1])
	year.append(dates[2])

#TODO: Create a function that can detect if a date is valid

#TODO: Copy the extracted dates and the validation infos to the clipboard