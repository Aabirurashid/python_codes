
# from bs4 import BeautifulStoneSoup
# from task1 import adventure_movie
# from task4 import scrap_movie_details
# from task5 import main_fun
# def cashing(top_movies):
#     for i in top_movies:
#         url1=i["url"]
#         id=url1[27:36]
        # print(url1)
        # random_sleep=random.randint(1,3)
        
#         # link=movie_detail_scrap(url1)
#         # with open(id+".json","w") as f:
#         #     dum=json.dump(link,f,indent=4)

#         file_exist=os.path.exists(id+".json")
#         if file_exist==True:
#             with open(id+".json","r") as file1:
#                 data=file1.read()
#                 print( data)
        
#         elif file_exist==False:
#             time.sleep(random_sleep)
#             page=requests.get(url1)
#             soup=BeautifulSoup(page.text,"html.parser")
#             #here We scrap movie name
#             tittle_div=soup.find('div',class_="title_wrapper").h1.get_text()
#             movie_name=''
#             for i in tittle_div:
#                 if "(" not in i:
#                     movie_name=(movie_name + i).strip()
#                 else:
#                     break    
#             #for run time and gener
#             sub_div=soup.find('div',class_="subtext")
#             #this is for runtime
#             run_time=sub_div.find('time').get_text().strip()
#             runtime_hours=int(run_time[0])*60
#             if "min" in sub_div:
#                 runtime_minutes=int(run_time[3:]).strip('min')
#                 movie_runtime=runtime_hours+runtime_minutes
#             else:
#                 movie_runtime=runtime_hours

#             #Movie gener
#             gener=sub_div.find_all("a")
#             gener.pop()
#             movie_gener=[i.get_text() for i in gener]
#             summary=soup.find('div',class_="plot_summary")
#             #this is for movie bio and movie director
#             movie_bio=summary.find('div',class_="summary_text").get_text().strip()
#             #here i scrap the director name
#             director=summary.find('div',class_="credit_summary_item")
#             director_list=director.find_all('a')
#             movie_director=[i.get_text().strip() for i in director_list]

#             #language details
#             extra_details=soup.find('div',attrs={"class":"article","id":"titleDetails"})
#             lists_of_divs=extra_details.find_all('div')
#             for div in lists_of_divs:
#                 tag_h4=div.find_all('h4')
#                 for text in tag_h4:
#                     if 'Language:' in text:
#                         tag_anchor=div.find_all('a')
#                         movie_language=[language.get_text() for language in tag_anchor]
    
#             #find the poster 
#             movie_poster_link=soup.find('div',class_="poster").a['href']
#             movie_poster="https://www.imdb.com"+movie_poster_link
    
#             #created dic for all
#             movie_detail_dic={"name":" ","director":" ","bio":" ","runtime":" ","gener":" ","language":" ","poster_link":" "}
#             movie_detail_dic["name"]=movie_name
#             movie_detail_dic["director"]=movie_director
#             movie_detail_dic["bio"]=movie_bio
#             movie_detail_dic["runtime"]=movie_runtime
#             movie_detail_dic["gener"]=movie_gener
#             movie_detail_dic["language"]=movie_language
    
#             movie_detail_dic["poster_link"]=movie_poster

#             with open(id+".json","w") as f:
#                 raw=json.dumps(movie_detail_dic,indent=4)
#                 # print(raw)
#                 f.write(raw)

            
#                 print (movie_detail_dic)






# top_movies = scrape_top_list()
# # movies_detail_list = get_movie_list_detail(top_movies[:10]) #  dekho kaise humne slicing ka use karke humne sirf pehli 10 movies input di. Yeh karna yaad rakhna :)
# a=cashing(top_movies[:3]) # dekho kaise get_movie_list_details ki return value humne analyse_movies_language function mein de di 
# print(a)


import requests
from bs4 import BeautifulSoup
import pprint
import json
import os
import random
import time
from task1 import adventure_movie
from task5 import main_fun
task1=adventure_movie()
url_list=[]
for i in task1:
    url_list.append(i['Movie URL'])
def scrape_movie(movie_url_list):
    random_sleep = random.randint(1,3)
    for i in movie_url_list:
        id=i[:34]
        file_name = id+".json"
        if os.path.exists(file_name):
            fil1=("file_name.json","r")
            h=json.load(fil1)
            print(h)
        else:
            time.sleep(random_sleep)
            page=requests.get(i)
            soup=BeautifulSoup(page.text,"html.parser")
            d={}
            main_div=soup.find("ul",class_="content-meta info")
            sub_div=main_div.find_all("li",class_="meta-row clearfix")
            for i in (sub_div):
                d[i.find("div",class_="meta-label subtle").text]=i.find("div",class_="meta-value").text
            pprint.pprint(d)
            with open("file_name.json","w")as fil:
                json.dump(d,fil,indent=2)
pprint(scrape_movie(url_list))
