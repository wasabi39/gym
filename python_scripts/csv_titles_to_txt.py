import csv

with open(r'C:\Users\Benjamin\Documents\Kodning\Gym project\raw data\jobtitles_61020_66799.csv', 'r') as inputfile:
    csvreader = csv.reader(inputfile)
    with open (r'C:\Users\Benjamin\Documents\Kodning\Gym project\gym_titles.txt', 'w') as outputfile:
        for line in csvreader:
            try:
                title = line[1] + '\n'
                outputfile.write(title)  
            except:
                print("error occurred")