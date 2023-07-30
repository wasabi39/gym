import csv
#input is a file with subjects
#output is a count of each subject

subjects =  ["afsætning","arabisk","astronomi","billedkunst","biologi","bioteknologi",
             "dansk","dansk som andet sprog","datalogi","design","dramatik","engelsk",
             "erhvervsjura","erhvervsøkonomi","filosofi","finansiering","fransk","fysik","færøsk",
             "geografi","geovidenskab","græsk","grønlandsk","historie","idehistorie",
             "idræt","informatik","innovation","international teknologi & kultur","international økonomi",
             "it & kommunikation","italiensk","japansk","kemi","kinesisk",
             "kulturforståelse","latin","markedskommunikation","matematik","materialeteknologi","mediefag",
             "multimedier","musik","naturfag","oldtidskundskab","organisation",
             "programmering","psykologi","religion","retorik","russisk","samfundsfag","spansk",
             "statik","statistik","teknikfag","teknologi","tyrkisk","tysk","virksomhedsøkonomi"]

subject_dict = {}

for i in subjects:
    subject_dict[i] = 0

with open(r'C:\Users\Benjamin\Documents\Kodning\Gym project\subject_count_61020_666799.csv', mode='w') as separated_subjects_file:
    subjects_writer = csv.writer(separated_subjects_file, delimiter=',', lineterminator='\n')
    with open(r"C:\Users\Benjamin\Documents\Kodning\Gym project\split_subjects_61020_666799.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            try:
                subject = row[3]
                if subject != "":
                    subject_dict[subject] += 1       
            except:
                print("Error occurred at id" + str(row[0]))
    total_count = 0
    for i in subjects:
        subjects_writer.writerow([i,subject_dict[i]])
        total_count += subject_dict[i]
    subjects_writer.writerow(["total",total_count])
    