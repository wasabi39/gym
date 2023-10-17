# About the project
Although many rumours exist about the job market for gymnasium teachers in Denmark, little data exists. This project seeks to change that by analyzing web scraped data from gymnasiejob.dk and other sources.

An outline of the project:
- I webscraped 7 years worth of job ads from gymnasiejob.dk. (DONE)
- This data was cleaned up, processed and visualized using Python, Seaborn, Pandas and Matplotlib. (DONE)
- A machine learning based analysis of the web scraped data and additional data from the Danish Ministry of Education was conducted using Python, Scikit-learn, Vega and Javascript. This resulted in the development of a model which identified 4 clusters of subjects, each of which have significantly different job opportunities. (DONE)
- A website presenting the results was developed using Javascript, HTML, CSS, D3.js and Vega (PARTLY DONE, not hosted online yet).
- The development of a generative AI model which is able to generate fictive job ads based off the webscraped data was attempted in Python but the results were not satisfactory due to the low quantity of available job ads (DONE).
- A heatmap showing the overlap in what subjects schools tend to request in the same job ad was developed using Python, Pandas, Seaborn, Numpy and Matplotlib. This showed that traditional subject combinations like maths/physics or Danish/English were slightly more common but the difference was not so significant that these combinations of subjects have better job opportunities than untraditional subject combinations (DONE).

The main result of the project is that subjects can be divided into 4 clusters depending on the job opportunities for teachers in those subjects:
- Cluster 1: Maths. This is the only subject characterized by a very high demand and low competition for jobs.
- Cluster 2: Social studies, Latin, classical studies, French, German and geography. These subjects have moderate demand and very few applicants per job. This makes the job opportunities decent for teachers in these subjects.
- Cluster 3: Chemistry, physics, biology, PE, Danish, English. These subjects have moderate demand and moderate to high competition in the job market.
- Cluster 4: Art, Spanish, Italian, Chinese, religion, history, music, philosophy and drama. These subjects are in very low demand. 
