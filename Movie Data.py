'''superhero regression project 
the idea is to see to what extent rating has on boxoffice from 2007 to 2019'''

import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
import requests
import csv
#the location of the movie list
file = r"C:\Users\mferguson018\Desktop\movielist.csv"
#This is to get the list of movies from the CSV file
with open(file) as csvfile:
    readCSV = csv.reader(csvfile)
    movielist = []
    for row in readCSV:
        movielist.append(row[0])

def getmovie(title, year = None):
    #this will get a list of elements from the json data
    try:
        #blank values that are used to fill out info
        boxoffice_string = ''
        listvalue = []
   
        #if statement to determine if year is used
        if year == None:
            url = 'http://www.omdbapi.com/?apikey=d42d26d9&t=' + str(title)
        else:
            url =  'http://www.omdbapi.com/?apikey=d42d26d9&t=' + str(title) + '&y=' +str(year)
   
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
                
        return listvalue
    
    except (ValueError, KeyError) :
       print('error - ' + title + ' may not be the correct title')
    
    #return listvalue

#blank lists to be filled out later to create each column of the dataframe
title_list = []
boxoffice_list = []
rating = []
year = []

#def function to append the list from getmovie into 4 different lists
def createlists(listvalue):
    try:
        #appends the list values
        title_list.append(listvalue[0])
        boxoffice_list.append(listvalue[1])
        rating.append(listvalue[2])
        year.append(listvalue[3])
    except (IndexError,TypeError):
        print('missing value')
        
#Combo of createlist and getmovie functions        
def fillout(movielist, num = len(movielist)):
    #this function loops over the all the movies and appends each of the blank lists
    for i in range(num):
        createlists(getmovie(movielist[i]))
        
#running the function to fill out all the series
fillout(movielist)
#defining the basic frame of the dataframe from a dictionary
frame = {'Title': title_list, 'BoxOffice':boxoffice_list, 'Rating': rating, 'Year':year}

allmovie_df = pd.DataFrame(frame)

#filtering to get rid of values that are 0 for box office
filter_value = allmovie_df['BoxOffice'] != 0
#final dataframe for all the movies and ratings
final_movie_df = allmovie_df[filter_value]

#the basic OLS regression
results = smf.ols('BoxOffice ~ Rating', data=final_movie_df).fit()
print(results.summary())






















