import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import cluster as sklearn_cluster
from mplcursors import cursor

job_data = pd.read_csv('https://raw.githubusercontent.com/wasabi39/gym/main/subject_subjectcount_KU2022_AU2022_percentageteaching2019.csv', usecols = ['subject', 'jobs', 'ku_degrees','au_degrees','percentage_teaching'])
job_data["job_applicant_ratio"] = (job_data["jobs"] * 100) / (job_data["percentage_teaching"] * 7 * (job_data["au_degrees"] + job_data["ku_degrees"]))
job_data["degrees"] = job_data["au_degrees"] + job_data["ku_degrees"]
print(job_data.head())



job_data_2 = pd.read_csv('https://raw.githubusercontent.com/wasabi39/gym/main/subject_subjectcount_KU2022_AU2022_percentageteaching2019.csv', usecols = ['jobs'])
job_data_2["job_applicant_ratio"] = job_data["job_applicant_ratio"] * 100


Kmean = sklearn_cluster.KMeans(n_clusters=4,n_init=50)
Kmean.fit(job_data_2)
clusters = Kmean.predict(job_data_2)
print(Kmean.cluster_centers_)
print(clusters)

label_color_map = {0 : 'r',
                   1 : 'k',
                   2 : 'b',
                   3 : 'g',
                   4 : 'y'
                   }

label_color = [label_color_map[l] for l in clusters]


sns.scatterplot(data = job_data, x = 'jobs', y = 'job_applicant_ratio',c=label_color)
cursor(hover=True)
plt.show()
