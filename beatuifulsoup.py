from bs4 import BeautifulSoup
import requests
import csv
key=input('enter you job role : ')
url=f"https://m.timesjobs.com/mobile/jobs-search-result.html?txtKeywords={key}&cboWorkExp1=-1&txtLocation="
scarp=requests.get(url).text
soup=BeautifulSoup(scarp,'html.parser')
box=soup.find_all('div',class_='srp-listing  clearfix')
job=soup.find_all('div',class_='srp-job-heading') 
skills=soup.find_all('div',class_='srp-keyskills')
com_detailes=soup.find_all('div',class_='clearfix exp-loc')
full_skill=[]
detailes=soup.find_all('div',class_='srp-listing')
with open (r'C:\Users\Lenovo\OneDrive\Desktop\webscraping\jobtacker.csv','w')as f :
            f1=csv.writer(f)
            f1.writerow(['Job','Company Name','Skills','Location' ,'experance','Posted Date', 'detailes'])
            title=[i.find('h3').a.text for i in job]
            company=[i.find('span',class_='srp-comp-name').text for i in job]
            location=[j.find('div',class_='srp-loc').text for  j in com_detailes]
            exp=[j.find('div',class_='srp-exp').text for j in com_detailes]
            post_date=[i.find('span',class_='posting-time').text for i in job]
            full_det=[i.find('a')['href'] for i in detailes]
            for i in skills:
                skill=i.find_all('a',class_='srphglt')
                full_skill.append([j.text for j in skill])
            i=0
            while i<len(company):
                f1.writerow([title[i],company[i],full_skill[i],location[i],exp[i],post_date[i],full_det[i]])
                i+=1
            
