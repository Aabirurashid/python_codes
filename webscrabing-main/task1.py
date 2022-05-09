import requests
from bs4 import BeautifulSoup
import json
# def adventure_movie():
#     url="https://www.rottentomatoes.com/top/bestofrt/top_100_action__adventure_movies/"
#     page=requests.get(url)
#     htmlcont=page.content
#     soup=BeautifulSoup(htmlcont,"html.parser")
#     table_tab=soup.find("table",class_="table")
#     tr=table_tab=soup.find_all()
#     list1=[]
#     serial_number=1
#     for i in tr:
#         movie_rank=i.find_all("td",class_="bold")
#         for j in movie_rank:
#             rank=j.get_text()
#         movie_rating=i.find_all("span",class_="tMeterScore")
#         for rate in movie_rating:
#             rating=rate.get_text().strip()
#         movie_name=i.find_all("a",class_="unstyled articlelink")
#         for name in movie_name:
#             movie1=name.get_text().strip()
#             list=movie1.split()
#             # print(list)
#             year=list[-1][1:5]
#             # print(year)
#             year1=int(year)
#             name_length=len(list)-1
#             name1=""
#             for t in range(name_length):
#                 name1+=""
#                 name+=list[t]
#             MovieName=name
#         movie_Reviews=i.find_all("td",class_="right hidden-xs")
#         for rev in movie_Reviews:
#             reviews=rev.get_text()
#             # print(reviews)
#         url=i.find_all("a",class_="unstyled articlelink")
#         for i in url:
#             link=i["href"]
#             movie_link="https://www.rottentomatoes.com"+link
#             details={"Movie Rank":"","Movie Rating":"","Movie Name":"","Movie Reviews":"","Movie Url":"","Year":""}
#             details["Movie Rank"]=rank
#             details["Movie Rating"]=rating
#             details["Movie Name"]=MovieName
#             details["Movie Reviews"]=reviews
#             details["Movie Url]"]=movie_link
#             details["Year"]=year1
#             list1.append(details.copy())
#     with open("list1.json","w")as file:
#         json.dump(list1,file,indent=4)
#     return list1
# scrapped=adventure_movie()




# def scrape_top_list():
#     url = "https://www.imdb.com/india/top-rated-indian-movies/"
#     page = requests.get(url)
#     htmlc=page.content
#     soup = BeautifulSoup(htmlc,"html.parser")
#     # print(soup)
#     div=soup.find("div",class_="lister")
#     s=div.find("tbody",class_="lister-list")
#     name=s.find_all("tr")
#     top_movie=[]
#     searial_number=1
#     for i in name:
#         details={}
#         movie_name=i.find("td",class_="titleColumn").a.get_text()
#         year=i.find("td",class_="titleColumn").span.get_text()
#         rating=i.find("td",class_="ratingColumn imdbRating").strong.get_text()
#         url=i.find("td",class_="titleColumn").a["href"]
#         movie_url="https://www.imdb.com"+url
#         details={"Position":searial_number,"Name":movie_name,"Year":int(year[1:5]),"Rating":float(rating),"URL":movie_url}
#         searial_number+=1
#         top_movie.append(details.copy())
#         with open("task_1.json","w") as file:
#             json.dump(top_movie,file,indent=2)
#     return top_movie
# scrape_top_list()
# scrapped=scrape_top_list()
# # print(scrapped)
# def scrape_top_list_1(movies):
#     years=[]
#     for i in movies:
#         # print(i['Year'])
#         year = i["Year"]
#         if year not in years:
#             years.append(year)
#     movie_dict={i:[]for i in years}
#     for i in movies:
#         year=i ["Year"]
#         for x in movie_dict:
#             if str(x)==str(year):
#                 movie_dict[x].append(i)
#     with open("Year.json","w")as f:
#         json.dump(movie_dict,f,indent=4)
#     return movie_dict

# scrape_top_list_1(scrapped)

import requests
from bs4 import BeautifulSoup
import json
def adventure_movie() :
    adventure_url="https://www.rottentomatoes.com/top/bestofrt/top_100_action__adventure_movies/"
    adventure_api=requests.get(adventure_url)
    htmlcontent = adventure_api.content
    soup = BeautifulSoup(htmlcontent,"html.parser")
    table_tag = soup.find("table", class_="table")
    tr = table_tag.find_all("tr")        
    top_movie=[]
    searial_number=1
    for i in tr:
        movie_rank=i.find_all("td",class_="bold")
        for j in movie_rank:
            rank=j.get_text()
        movie_rating=i.find_all("span",class_="tMeterScore")
        for rate in movie_rating:
            rating=rate.get_text().strip()
        movie_name = i.find_all("a",class_="unstyled articleLink")
        for name in movie_name:
            title=name.get_text().strip()
            list=title.split()
            year=list[-1][1:5]
            year1=int(year)
            name_lenght=len(list)-1
            name=""
            for l in range(name_lenght):
                name+=" "
                name+=list[l]
            MovieName=name
        movie_Reviews = i.find_all("td",class_="right hidden-xs")
        for rev in  movie_Reviews:
            reviews=rev.get_text()
        url=i.find_all("a",class_="unstyled articleLink") 
        for i in url: 
            link=i["href"]
            movie_link="https://www.rottentomatoes.com"+link
            details={"Movie Rank":"","Movie Rating":"","Movie Name":"","Movie Reviews":"","Movie URL":"","Year":""}
            details["Movie Rank"]=rank
            details["Movie Rating"]=rating
            details["Movie Name"]=MovieName
            details["Movie Reviews"]=reviews
            details["Movie URL"]=movie_link
            details["Year"]=year1
            top_movie.append(details.copy())
    with open("top_movie_1.json","w") as file:
        json.dump(top_movie,file,indent=3)
    return top_movie                    
screpped=adventure_movie()
# scrapped=ad()
# print(scrapped)
