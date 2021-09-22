# Date Detection
 
Automate The Boring Stuff Chapter 7 Project

This is my take on the Date detector project. I added the possibility to pass arguments to the program that reformat the dates detected.

## Getting Started

For this project, you will need Python3 installed and the pyperclip module.

## Installing pyperclip

```pip install pyperclip```

## Running the app

```dateDetection [format] [separator]```

* [format]
		  * "DMY"(by default)
		  * "help"
		  * "validation"
		  * "MDY"
		  * "YMD"

* [separator]
		  * "/" by default if not specified
		  * "_any string_" will replace the '/' with the specified string
		  * "space" for " " separator