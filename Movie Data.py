import pandas as pd
import requests
import matplotlib.pyplot as plt

movie_file = r"C:\Users\mferguson018\Desktop\movie_list.csv"

def getmovie(movietitle, year = None):
    #this will get a list of elements from the json data
    try:
        #blank values that are used to fill out info
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
                
        return listvalue
    
    except (ValueError, KeyError) :
       print('error - ' + movietitle + ' may not be the correct title')
    
    return listvalue

#blank lists to be filled out later to create each column of the dataframe
title_list = []
boxoffice_list = []
rating = []
year = []

def createlists(listvalue):
    try:
        #appends the list values
        title_list.append(listvalue[0])
        boxoffice_list.append(listvalue[1])
        rating.append(listvalue[2])
        year.append(listvalue[3])
    except IndexError:
        print('missing value')
        
def fillout(allmovies, num = 10):
    #this function loops over the all the movies and appends each of the blank lists
    for i in range(num):
        createlists(getmovie(allmovies[i]))
        
        
#list of the actual movie titles to be searched
movie_titles = []
csv_movie = pd.read_csv(movie_file)
titles_from_csv = csv_movie['movie_title'].tolist()

for i in range(250):
    movie_titles.append(titles_from_csv[i])

#running the function to fill out all the series
fillout(movie_titles, num = 100)
#creating the series for 
title_series = pd.Series(title_list)
boxoffice_series = pd.Series(boxoffice_list)
rating_series = pd.Series(rating)
year_series = pd.Series(year)
#create a dictionary for the dataframe
frame = {'Title': title_series, 'BoxOffice':boxoffice_series, 'Rating': rating_series, 'Year':year_series }
#here we remove the lines that have N/A from the df into a new df   
df = pd.DataFrame(frame)
df_filter_series = df['BoxOffice'] != 0
df_final = df[df_filter_series]

print(df_final.head())
df_final.describe()

df_final.plot(x='Rating', y='BoxOffice', style = 'o')
plt.title('Rating to BoxOffice')
plt.xlabel('Rating')
plt.ylabel('BoxOffice')
plt.show()


import numpy as np
from sklearn.linear_model import LinearRegression

x = df_final.iloc[:, 2].values.reshape(-1,1)
y = df_final.iloc[:,1].values.reshape(-1, 1)

linear_regressor = LinearRegression()
linear_regressor.fit(x, y)
Y_pred = linear_regressor.predict(x)


plt.scatter(x, y)
plt.plot(x, Y_pred, color='red')
plt.show()



import statsmodels.formula.api as sm

result = sm.ols(formula="BoxOffice ~ Rating", data = df_final).fit()

print(result.params)

print(result.summary())
