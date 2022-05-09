from bs4 import BeautifulSoup
from task1 import adventure_movie
import requests
import json
screpped=adventure_movie()

def main_fun(screpped):
    # print(data)
    def scrap(link,Mname):
        # print(link)
    # print(data1)
        d1={}
        link_data=requests.get(link)
        # print(link_data)
        soup=BeautifulSoup(link_data.text,'html.parser')
        # print(soup)
        d1["name"]=Mname
        movie_bio=soup.find("div",class_="movie_synopsis clamp clamp-6 js-clamp").get_text().strip()
        # print(movie_bio)
        d1["Bio"]=movie_bio
        title=soup.find_all("div",class_="meta-label subtle")
        # print(title)
        value=soup.find_all("div",class_="meta-value")
        # print(value)
        for i in range(len(title)):
            d1[str(title[i].get_text().strip())[:-1]]=value[i].get_text().strip()

        return d1
    movie_details=[]   
 
    for i in screpped:
        # print(i)
        for j in i:
            Mname=i['Movie Name']
            if j=="Movie URL":
                # print(i[j])
                movie_dic=scrap(i[j],Mname)
                movie_details.append(movie_dic)
    # print(movie_details)     

    with open("file1.json","w") as f:  
        json.dump(movie_details,f,indent=4)
    return movie_details

var=main_fun(screpped)

