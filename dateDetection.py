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

#TODO: Get the text off the clipboard

#TODO: Extract the dates from this text

#TODO: Store these strings in variables "day" "month" "year"

#TODO: Create a function that can detect if a date is valid

#TODO: Copy the extracted dates and the validation infos to the clipboard