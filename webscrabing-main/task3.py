# from task1 import adventure_movie
# from task2 import adventure_movie
# import json
# Aabiru_data=adventure_movie()
# movie_bye_year=adventure_movie()
# # print(movie_bye_year)
# def scrape_top_list_2(movies):
#      moviedec={}
#      list1=[]
#      for year in movies:
#           mod=year%10
#           decade=year-mod
#           # print(i)
#           if decade not in list1:
#                list1.append(decade)
#                print(list1)
#           list1.sort
#      for i in list1:
#           moviedec[i]=[]
#      for i in moviedec:
#           decade=i+9
#           for x in movies:
#                if x<=decade and x>=i:
#                     for j in movies[x]:
#                          moviedec[i].append(j)
#                          with open("moomin.json","w")as data:
#                               json.dump(moviedec,data,indent=4)
# #                          return moviedec
# # scrape_top_list_2(movie_bye_year)


# from task1 import adventure_movie
# from task2 import scrape_top_list_1
# import json

# scrapped_data=adventure_movie()
# movie_bye_year=scrape_top_list_1(scrapped_data)
# def scrape_top_list_2(movie):
#     moviedec={}
#     list1=[]
#     for year in movie:
#         mod=year%10
#         decade=year-mod
#         if decade not in list1:
#             list.append(decade)
#     list1.sort()
#     for i in list1:
#         dec10=i+9
#         for x in movie:
#             if x<=dec10 and x>=i:
#                 for v in movie[x]:
#                     moviedec[i].append(v)
#         with open("task_3.json","w") as file:
#             json.dump(moviedec,file,indent=4)
#             return moviedec
#     scrape_top_list_2(movie_bye_year)



from task1 import adventure_movie
import json
name=adventure_movie()
def group_by_decade(movise):
    movisedec={}
    list1=[]
    for index in movise:
        mod=index["Year"]%10
        decode=index["Year"]-mod
        if decode not in list1:
            list1.append(decode)
    print(list1)    
    list1.sort()
    # print(list1) 
    for i in list1:
        movise_list=[]
        # movisedec[i]=[]
        # print(movisedec)  
        # for i in movisedec:
            # dec10=i+9
        for x in movise:
                # if x["Year"]<=dec10 and x["Year"]:
            if x["Year"]>=i and x["Year"]<=i+10:
                movise_list.append(x)
                movisedec[i]=movise_list
                    # for v in movise[x]:
                    #     movisedec[i].append(v)
                with open("Aabiru.json","w")as file:
                        json.dump(movisedec,file,indent=3)
               #  print(movisedec)    
#     print(movisedec)                    
group_by_decade(name)
