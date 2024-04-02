import csv


# open file handles to both csv files
orig_csv = "project-data.csv"
clean_csv = "clean_proj_data.csv"
clean = open(clean_csv, 'w', newline='')

with open(orig_csv, 'r') as orig:
    lines = orig.readlines()
    for line in lines:
        if line[0].isdigit():
            print(line)
            clean.write(line)

# for each original row, if the row starts with "a number,"keep it 
# write it to the clean csv file
