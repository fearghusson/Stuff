import requests
import datetime

def search_news_today(search_term, max_results = 5):
    url = r"https://newsapi.org/v2/everything?q="+search_term+"&from="+str(datetime.date.today())+"&to="+str(datetime.date.today())+"&sortBy=popularity&pageSize="+str(max_results)+"&apiKey=88b2fe182ea34f34a58b9e67a835695f"
    response = requests.get(url)
    json_data = response.json()
    just_articles = json_data['articles']
    
    num = 0
    
    for i in range(len(just_articles)):
        print(str(num) + ' ' + just_articles[i].get('title'))
        print('URL-' + just_articles[i].get('url'))
        print('\n')
        num = num + 1

def current_news(max_results = 5):
    url = r"https://newsapi.org/v2/top-headlines?country=us&pageSize=" + str(max_results) + "&apiKey=88b2fe182ea34f34a58b9e67a835695f"
    response = requests.get(url)
    json_data = response.json()
    just_articles = json_data['articles']
    
    num = 0
    
    for i in range(len(just_articles)):
        print(str(num) + ' ' + just_articles[i].get('title'))
        print('URL-' + just_articles[i].get('url'))
        print('\n')
        num = num + 1
        
print('get current top news?')
question1 = input()

if question1 == 'yes':
    current_news()
else:
    print('what do you want to search?')
    question2 = input()
    search_news_today(question2)
