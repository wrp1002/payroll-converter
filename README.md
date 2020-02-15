# payroll-converter

# Running the program
	Whenever the program is started, the user is prompted to tell it where the payroll file is. This file must be in csv format. Specifying where the file is can be done using absolute file paths or relative file paths. For example, if the csv is in the same folder, you could simply enter “payroll.csv”. For absolute paths, an example could be “C:/Program Files/payroll.csv”. If you do this and the file is opened successfully, it will begin processing the file. 
There are a few errors that can occur from reading the file
- •	Error: Different Co Code in file # - This occurs whenever there are multiple ‘Co Code’ found in a single file. The program will tell you which file caused this error so that it can be fixed. It also gives the option to manually specify which ‘Co Code’ you would like to use for naming the file
- •	Error: Could not find REG hours of file # - This occurs whenever a record does not have a REG hour. The program will still finish, but that record will have 0 REG hours. 
- •	Error: Not enough room in row for file # - There is a set number of columns available for special hour types. If a record has too many hour types, some of them will not be saved to the file. This error warns you about this and tells you which file # this occurs in. 
- •	Error: Permission denied writing to output file – Unable to write to output file. Make sure that the output file is not open in another program. 
 	After the file is processed, an output file will be created using the Co Code found in the input file. This file will also be a csv and can be opened and edited easily with Excel. 

# Editing the program
To edit the program, you must open “payroll.py” with a text editor. I recommend using a text editor that is made for programming. I like using Notepad++ or Visual Studio Code. If you want something with more features aimed towards python, you can search google for “python IDE”. After making your changes, you can run the script with python to be sure it works as intended. 

# Making your own exe from python
There are many tools that allow you to turn a python script into an executable program. I use something called pyinstaller. This can be downloaded using pip, which comes with your python installation. You can get pyinstaller by running “pip install pyinstaller” from cmd. After you have gotten this program, you can compile the python script by running “pyinstaller --onefile payroll.py” 
