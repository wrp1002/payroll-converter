# -*- coding: utf-8 -*-

# Read input file, process it, and return a list of the lines from the file
def ReadFile():
	try:
		file = open(input("Enter path to file: "))
		lines = file.readlines()
		for i in range(len(lines)):
			lines[i] = lines[i].replace("\n", "").replace(":", ".").split(',')
		return lines
	except FileNotFoundError:
		print("Error: File not found")
		return ReadFile()
	except OSError:
		print("Error: Invalid file path format")
		return ReadFile()
	except PermissionError:
		print("Error: Permission denied opening file")
		return ReadFile()
	except:
		print("Error: Could not open file")
		return ReadFile()


if __name__ == "__main__":
	print("Payroll Converter v1.1\n")
	fileLines = ReadFile()
	records = {}
	coCodes = []
	outputName = ""
	errorFound = False
	lineNumber = 1
	
	print("\nLoading file...")

	# Process each line and store their attributes
	for line in fileLines:
		line = [i.strip() for i in line]
		
		if not len(line) == 5 or not all(line):
			print("Warning: Skipping line", lineNumber, "because of missing data")
			lineNumber += 1
			continue
		
		coCode = line[0]
		fileNum = line[1]
		numbers = line[2]
		hoursType = line[3]
		hours = line[4]
		
		if not fileNum in records:
			records[fileNum] = {}
			records[fileNum]['coCode'] = coCode
		else:
			if records[fileNum]['coCode'] != coCode:
				print("Warning: Different Co Code in file #" + fileNum)
				errorFound = True
		
		records[fileNum][hoursType] = hours

		if not coCode in coCodes:
			coCodes.append(coCode)
			
		lineNumber += 1

	for i in records:
		del records[i]['coCode']
		
	if errorFound:
		print("\nMulitple Co Codes found in file: " + ', '.join(cc for cc in coCodes))
		print("Output file will not have accurate Co Codes if there are multiple Co Codes per record")
		outputName = "PR" + input("Enter Co Code to use for output file name: ") + "EPI.csv"
	else:
		outputName = "PR" + coCodes[0] + "EPI.csv"
	
	#   Outputs all records to console. Useful for debugging, but takes extra time
	#for i in records:
	#	print("File #" + i, ':', records[i])
		
			  
	try:
		print("\nWriting to output file...\n")
		with open(outputName, "w") as out:
			out.write("Co Code,Batch ID,File #,Batch Description,Reg Hours,O/T Hours,Hours 3 Code,Hours 3 Amount, Hours 3 Code, Hours 3 Amount, Hours 3 Code, Hours 3 Amount, Hours 3 Code, Hours 3 Amount, Hours 4 Code, Hours 4 Amount, Hours 4 Code, Hours 4 Amount, Temp Dept\n")
			for rec in records:
				otherHoursCount = 0
				
				# Write basic info to each row
				out.write(coCode + ", ")
				out.write("1, ")
				out.write(rec + ", ")
				out.write("OSS Payroll, ")
				
				# Write REG hours for record
				if "REG" in records[rec]:
					out.write(records[rec]["REG"] + ", ")
				else:
					out.write("0, ")
					print("Error: Could not find REG hours of file #" + rec)
				
				# Write OVT hours for record
				if "OVT" in records[rec]:
					out.write(records[rec]["OVT"])
				else:
					out.write("0")
					
				# Write any other hour types to row other than COM because COM should be in the last column
				for i in records[rec]:
					if i not in ["REG", "OVT", "COM"]:
						if otherHoursCount <= 5:
							out.write(", " + i)
							out.write(", " + records[rec][i])
							otherHoursCount += 1
						else:
							print("Error: Not enough room in row for file #" + rec)
							break
					
				# If COM hours exist for this record and there is room for it, add it to the row
				if "COM" in records[rec]:
					commas = 10 - otherHoursCount * 2
					if commas >= 0:
						for i in range(commas):
							out.write(",")
						out.write(",COM, ")
						out.write(records[rec]["COM"])
					else:
						print("Error: Not enough room in row for file #" + rec)
					
				out.write("\n")
				
	except PermissionError:
		print("Error: Permission denied writing to output file")
		input("Press enter to exit...")
		quit()
	except:
		print("Error writing to file")
		input("Press enter to exit...")
		quit()
			
		
print("\nDone! Saved as " + outputName)
input("Press enter to exit...")
		
		
		
		
		
		
		
		
		
		
		
		