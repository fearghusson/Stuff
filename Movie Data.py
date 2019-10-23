import pandas as pd
import requests

def getmovie(movietitle, year = None):
    #this will get a list of elements from the json data
   
    #blank values
    boxoffice_string = ''
    listvalue = []
   
    #if statement to determine if year is used
    if year == None:
        url = 'http://www.omdbapi.com/?apikey=d42d26d9&' + 't=' + movietitle
    else:
        url =  'http://www.omdbapi.com/?apikey=d42d26d9&' + 't=' + movietitle + '&y=' +str(year)
   
    #requesting info from omdb and storing it to r
    r = requests.get(url)
    #pulling the json data
    json_data = r.json()
   
    #create if/else to determine whether the boxoffice is na or not. if it is
    #not it will put put the number
    if json_data['BoxOffice'] != 'N/A':
        #if the boxoffice isn't NA then it will use regex to get all the digits
        import re
        #define the regex to get just digits
        regex = re.compile(r'(\d)')
        digit = regex.findall(json_data['BoxOffice'])
        #loop to put all the number strings into
        for i in digit:
            boxoffice_string += i
        #convert the string into a number
        boxoffice_int = int(boxoffice_string)
        #final value to return
        listvalue = [json_data['Title'], boxoffice_int, int(json_data['Metascore']),
                 int(json_data['Year'])]
    else:
        listvalue = [json_data['Title'], 0, int(json_data['Metascore']),
                 int(json_data['Year'])]
        #returns the value
    return listvalue

#blank lists to be filled out later to create each column of the dataframe
title_list = []
boxoffice_list = []
rating = []
year = []

def createlists(listvalue):
    #appends the list values
    title_list.append(listvalue[0])
    boxoffice_list.append(listvalue[1])
    rating.append(listvalue[2])
    year.append(listvalue[3])

def fillout(allmovies):
    #this function loops over the all the movies and appends each of the blank lists
    for i in allmovies:
        listmovie = getmovie(i)
        createlists(listmovie)
        
#list of the actual movie titles to be searched
movie_titles =  ['batman', 'spider-man']

#running the function to fill out all the series
fillout(movie_titles)

title_series = pd.Series(title_list)
boxoffice_series = pd.Series(boxoffice_list)
rating_series = pd.Series(rating)
year_series = pd.Series(year)

#create a dictionary for the dataframe
frame = {'Title': title_series, 'BoxOffice':boxoffice_series, 'Rating': rating_series, 'Year':year_series }
        
df = pd.DataFrame(frame)

print(df)
