import csv


# open file handles to both csv files
orig_csv = "project-data.csv"
clean_csv = "clean_proj_data.csv"
clean = open(clean_csv, 'w', newline='')

with open(orig_csv, 'r') as orig:
    lines = orig.readlines()
    count = 0
    for line in lines:
        if count == 0:
            clean.write(line)
        if line[0].isdigit():
            print(line)
            clean.write(line)
        count += 1

# for each original row, if the row starts with "a number,"keep it 
# write it to the clean csv file
