import requests
import csv
import re
from bs4 import BeautifulSoup
 

def find_title(url_number):
    base_url = 'https://www.gymnasiejob.dk/jobopslag/'
    url = base_url + str(url_number)

    #gets the data from the url
    reqs = requests.get(url)
    soup = BeautifulSoup(reqs.text, 'html.parser')

    #returns the title of the position from the data - nothing else
    #the [17:] removes the prefix "Gymnasiejob.dk - " that is in all titles
    for title in soup.find_all('title',limit=1):
        title = title.get_text()[17:].strip(r'"').strip(r"'").strip(" ")
        #print(title)
    return title.lower()


def find_data(url_number):
    base_url = 'https://www.gymnasiejob.dk/jobopslag/'
    url = base_url + str(url_number)

    #gets the data from the url
    reqs = requests.get(url)
    soup = BeautifulSoup(reqs.text, 'html.parser')

    #returns the title of the position from the data - nothing else
    #the [17:] removes the prefix "Gymnasiejob.dk - " that is in all titles
    for metadata in soup.find('script', type='application/ld+json'):
        #start = r'description": "&amp;lt;p&amp;gt;'
        #end = r'  "hiringOrganization'
        #description = metadata[metadata.find(start)+len(start):metadata.rfind(end)][:-5]
        #mapping =  dict.fromkeys(range(32))
        #description = str(description.translate(mapping)

        metadata = str(metadata)

        start = r'datePosted'
        end = r','
        date = metadata[metadata.find(start)+len(start)+4:][:10]

        start = r'postalCode'
        end = r','
        postal_code = metadata[metadata.find(start)+len(start)+4:][:4]

        start = r'streetAddress'
        end = r','
        address = metadata[metadata.find(start)+len(start)+4:][:45]
        address = address[:address.find('"')]
        address = address.replace("&#230;","æ")
        address = address.replace("&#248;","ø")
        address = address.replace("&#229;","å")
        address = address.replace("&#233;","é")
        address = address.replace("&#216;","Ø")
        address = address.replace("&#198;","Æ")
        address = address.replace("&#197;","Å")

        start = r'addressLocality'
        end = r','
        city = metadata[metadata.find(start)+len(start)+4:][:20]
        city = city[:city.find('"')]
        city = city.replace("&#230;","æ")
        city = city.replace("&#248;","ø")
        city = city.replace("&#229;","å")
        city = city.replace("&#233;","é")
        city = city.replace("&#216;","Ø")
        city = city.replace("&#198;","Æ")
        city = city.replace("&#197;","Å")


        start = r'addressRegion'
        end = r','
        region = metadata[metadata.find(start)+len(start)+4:][:20]
        region = region[:region.find('"')]
        region = region.replace("&#230;","æ")
        region = region.replace("&#248;","ø")
        region = region.replace("&#229;","å")
        region = region.replace("&#233;","é")
        region = region.replace("&#216;","Ø")
        region = region.replace("&#198;","Æ")
        region = region.replace("&#197;","Å")

        print(address, postal_code, city, region)

    return date, address, postal_code, city, region


def find_subjects(url_number):
    base_url = 'https://www.gymnasiejob.dk/jobopslag/'
    url = base_url + str(url_number)

    #gets the data from the url
    reqs = requests.get(url)
    soup = BeautifulSoup(reqs.text, 'html.parser')

    subjects = ""
    jobtype = ""
    for metadata in soup.find_all('li'):
        metadata = str(metadata).replace(" &amp; ", "-").lower()
        if "Undervisningsfag" in metadata:
            subjects = metadata[42:-5]
        if "Ansættelsesforhold" in metadata:
            jobtype = metadata[44:-5]
    return subjects, jobtype


def find_subjects_from_title(title):
    #naturgeografi and dans left out as a quick fix
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
    job_subjects = ""
    for subject in subjects:
        if subject in title:
            job_subjects += subject
            job_subjects += "-"
    job_subjects = job_subjects[:-1]
    print(job_subjects)
    return job_subjects

def run_script():
    with open(r'C:\Users\Benjamin\Documents\Kodning\Gym project\jobtitles.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for i in range(57000,61020):
            if i % 100 == 0:
                print(i)
            job_title = find_title(i)
            if job_title != "undet":
                try:
                    date, address, postal_code, city, region = find_data(i)
                    subjects, jobtype = find_subjects(i)

                    #if no subjects could be found directly in the html, we search for subjects in the website's title
                    if subjects == "":
                        subjects = find_subjects_from_title(job_title)
                    try:
                        writer.writerow([i, job_title,date, subjects, jobtype, address, postal_code, city, region])
                    except:
                        print("An error occurred writing data to the sheet at id " + str(i))
                except TypeError:
                    print("Type error at https://www.gymnasiejob.dk/jobopslag/" + str(i))

#find_subjects(66781)
run_script()


