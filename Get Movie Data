def getmovie(movietitle, year = None):
    #this will get a list of elements from the json data
   
    #blank values
    boxoffice_string = ''
    listvalue = []
    #importing the package
    import requests
   
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
        listvalue = [json_data['Title'], 'N/A', int(json_data['Metascore']),
                 int(json_data['Year'])]
        #returns the value
    return listvalue

print(getmovie('batman'))
