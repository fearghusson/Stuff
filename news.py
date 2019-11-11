import datetime
import requests

date_object = datetime.date.today()
print(date_object)
type(str(date_object))

date = str(date_object)
search = input()

urlnew = r"https://newsapi.org/v2/everything?q='" + search_term+ "&from=" + date_object + "&to=" + date_object + "&sortBy=popularity&pageSize=5&apiKey=88b2fe182ea34f34a58b9e67a835695f"

url = r'https://newsapi.org/v2/top-headlines?country=us&q=' + search + '&apiKey=88b2fe182ea34f34a58b9e67a835695f'
response = requests.get(url)
json_data = response.json()
print(json_data)

just_articles = json_data['articles']

dict1 = just_articles[0]

dict1.get('url')

just_articles[0].get('url')

for i in range(len(just_articles)):
    print(just_articles[i].get('title'))
    print(just_articles[i].get('url'))


def news(search_term, max_results = 5):
    import requests
    url = r"https://newsapi.org/v2/everything?q="+search_term+"&from="+str(date_object)+"&to="+str(date_object)+"&sortBy=popularity&pageSize="+str(max_results)+"&apiKey=88b2fe182ea34f34a58b9e67a835695f"
    response = requests.get(url)
    json_data = response.json()
    just_articles = json_data['articles']
    
    for i in range(len(just_articles)):
        print(just_articles[i].get('title'))
        print('URL-' + just_articles[i].get('url'))
        print('\n')
        
        
news('bolton', 5)

import webbrowser

webbrowser.open(r"https://news.yahoo.com/ukrainians-contacted-u-officials-may-233114100.html", new = 1)

