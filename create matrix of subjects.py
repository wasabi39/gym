import csv
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from datasets import Dataset


matrix = [[0 for _ in range(26)] for _ in range(26)]

subjects = ["matematik","biologi","kemi","fysik","geografi","idræt",
             "dansk","engelsk","tysk","fransk","spansk",
             "latin","oldtidskundskab","historie","samfundsfag",
             
             
             "erhvervsøkonomi","psykologi",
             
             
             
             
             "musik","religion",
             "billedkunst","dramatik","mediefag","filosofi","italiensk","kinesisk","informatik"]

subject_dict = {}

#key is the subject name, value is the position in the matrix
for i in list(zip(list(range(26)),subjects)):
    subject_dict[i[1]] = i[0]
    print(i[1],i[0])


print(matrix)
print(list(zip(list(range(26)),subjects)))


with open(r'C:\Users\Benjamin\Documents\Kodning\Gym project\raw data\jobtitles_61020_66799.csv', mode='r') as input_file:
    csv_reader = csv.reader(input_file, delimiter=',')
    for row in csv_reader:
        try:
            row_subjects = row[3].split('-')
            for i in row_subjects:
                for j in row_subjects:
                    if i != j:
                        try: 
                            i_index = subject_dict[i]
                            j_index = subject_dict[j]
                            matrix[i_index][j_index] += 1
                        except:
                            print("error, could not find " + str(i) + " or " + str(j) + " in dictionary.")
        except:
            print("empty line")


subject_count = [0 for _ in range(26)]

for i in range(26):
    for j in range(26):
        subject_count[j] += matrix[i][j]
print(subject_count)

for i in range(26):
    for j in range(26):
        matrix[i][j] = matrix[i][j] / (subject_count[j] + subject_count[i])

data = pd.DataFrame([x if isinstance(x, list) else [x] for x in matrix]).rename(columns = lambda x: subjects[x], index = lambda x: subjects[x])

print(data)

hmap = sns.heatmap(data, xticklabels=True, yticklabels=True,vmax=0.1)

plt.gcf().subplots_adjust(bottom=0.30,left=0.30)

hmap.figure.savefig(r"C:\Users\Benjamin\Documents\Kodning\Gym project\website\subject_heatmap2.png",
                    format='png',
                    dpi=450)


plt.show()