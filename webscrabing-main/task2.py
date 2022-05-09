
# import requests
# from bs4 import BeautifulSoup
# import json
# def adventure_movie() :
#     adventure_url="https://www.rottentomatoes.com/top/bestofrt/top_100_action__adventure_movies/"
#     adventure_api=requests.get(adventure_url)
#     htmlcontent = adventure_api.content
#     soup = BeautifulSoup(htmlcontent,"html.parser")
#     table_tag = soup.find("table", class_="table")
#     tr = table_tag.find_all("tr")        
#     top_movie=[]
#     searial_number=1
#     for i in tr:
#         movie_rank=i.find_all("td",class_="bold")
#         for j in movie_rank:
#             rank=j.get_text()
#         movie_rating=i.find_all("span",class_="tMeterScore")
#         for rate in movie_rating:
#             rating=rate.get_text().strip()
#         movie_name = i.find_all("a",class_="unstyled articleLink")
#         for name in movie_name:
#             title=name.get_text().strip()
#             list=title.split()
#             year=list[-1][1:5]
#             year1=int(year)
#             name_lenght=len(list)-1
#             name=""
#             for l in range(name_lenght):
#                 name+=" "
#                 name+=list[l]
#             MovieName=name
#         movie_Reviews = i.find_all("td",class_="right hidden-xs")
#         for rev in  movie_Reviews:
#             reviews=rev.get_text()
#         url=i.find_all("a",class_="unstyled articleLink") 
#         for i in url: 
#             link=i["href"]
#             movie_link="https://www.rottentomatoes.com"+link
#             details={"Movie Rank":"","Movie Rating":"","Movie Name":"","Movie Reviews":"","Movie URL":"","Year":""}
#             details["Movie Rank"]=rank
#             details["Movie Rating"]=rating
#             details["Movie Name"]=MovieName
#             details["Movie Reviews"]=reviews
#             details["Movie URL"]=movie_link
#             details["Year"]=year1
#             top_movie.append(details.copy())
#     with open("top_movie_1.json","w") as file:
#         json.dump(top_movie,file,indent=3)
#     return top_movie                    
# screpped=adventure_movie()
# scrapped=ad()
# print(scrapped)
from task1 import adventure_movie
Aabiru=adventure_movie()
import json
def scrape_top_list_1(movie):
    years=[]
    for i in movie:
        # print(i['Year'])
        year = i["Year"]
        if year not in years:
            years.append(year)
    movie_dict={i:[]for i in years}
    for i in movie:
        year=i ["Year"]
        for x in movie_dict:
            if str(x)==str(year):
                movie_dict[x].append(i)
    with open("Aabiru.json","w")as f:
        json.dump(movie_dict,f,indent=4)
    return movie_dict
scrape_top_list_1(Aabiru)