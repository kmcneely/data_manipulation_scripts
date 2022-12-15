# Kelsey McNeely
# University of Chicago
# 4.14.2021
# Get intersection of multianno txt files
# Input: directory with 2 or more txt files
# Edit: line 13 with directory containing ONLY files to find intersection of

# Python 3.7.4

import os

# get list of multianno.txt files to be merged
multiannos_dir = "directory with files"
os.chdir(multiannos_dir)
files_list = os.listdir(multiannos_dir)
# print(type(files_list))
# print(files_list)

# open input files and read line by line into fileLines[]
# list of lines for each individual
fileLines = []
for fileName in files_list:
    print(fileName)
    with open(fileName, 'r') as tempFile:
        tempLines = tempFile.readlines()
        fileLines.append(tempLines)
        # print(fileName)

found = 0
removed = 0
notFound = 0
kept = 0

# if a line shared between first and second file, append to mergedLines[]
# if a line from mergedLines[] not in remaining files, remove
mergedLines = []
if len(files_list) > 1:
    print("Processing " + str(len(files_list)) + " files.")
    for line1 in fileLines[0]:
        if line1 in fileLines[1]:
            found += 1
            # print("Found = " + str(found))
            mergedLines.append(line1)
        else:
            notFound += 1
            # print("notFound = " + str(notFound))
    print("Completed merge. MergedLines = " + str(len(mergedLines)))

    if len(files_list) > 2:
        i = 2
        while i < len(fileLines):
            # loop through copy of mergedLines, remove from mergedLines if not found in current file's lines
            for mLine in mergedLines[:]:
                if mLine in fileLines[i]:
                    kept += 1
                else:
                    mergedLines.remove(mLine)
                    removed += 1
            i += 1
else:
    print("Not enough input files. Need at least 2.")

print("Found = " + str(found))
print("notFound = " + str(notFound))
print("Removed = " + str(removed))
print("Kept = " + str(kept))
print("Intersection total: " + str(len(mergedLines)))

with open("intersection_output.txt", "w") as outputFile:
    for line in mergedLines:
        outputFile.write(line)

