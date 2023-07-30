import csv


with open(r'C:\Users\Benjamin\Documents\Kodning\Gym project\split_subjects_61020_666799.csv', mode='w') as separated_subjects_file:
    subjects_writer = csv.writer(separated_subjects_file, delimiter=',', lineterminator='\n')
    with open(r"C:\Users\Benjamin\Documents\Kodning\Gym project\jobtitles_61020_66799.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            try:
                subjects = row[3]
                if subjects != "":
                    subjects = subjects.split("-")
                    for subject in subjects:
                        subjects_writer.writerow([row[0],row[1],row[2],subject,row[4],row[5],row[6],row[7],row[8]])
            except:
                print("Error occurred at id" + str(row[0]))