import csv

with open(r'C:\Users\Benjamin\Documents\Kodning\Gym project\stripped_jobtitles - 61020-66798 - Kopi.csv', mode='w') as separated_subjects_file:
    subjects_writer = csv.writer(separated_subjects_file, delimiter=',', lineterminator='\n')
    with open(r'C:\Users\Benjamin\Documents\Kodning\Gym project\jobtitles - 61020-66798 - Kopi.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',', lineterminator=';')
        for row in csv_reader:
            if row is not None and row != "":
                
                try:
                    subjects_writer.writerow([row[0].strip(r''' '"'''),row[1].strip(r''' '"'''),row[2].strip(r''' '"'''),row[3].strip(r''' '"'''),row[4].strip(r''' '"'''),row[5].strip(r''' '"'''),row[6].strip(r''' '"'''),row[7].strip(r''' '"'''),row[8].strip(r''' '"''')])
                except:
                    print("Error occurred at id" + str(row[0]))