from django.shortcuts import render
from newsapi import NewsApiClient



def index(request):
    newsApi = NewsApiClient(api_key = '483b04da5f7243438b5dd5cf07819eb7')
    headLines = newsApi.get_top_headlines(sources = 'bbc-news')
    articles = headLines['articles']
    desc = []
    news = []
    img = []
    url = []

    for i in range(len(articles)):
        article = articles[i]
        desc.append(article['description'])
        news.append(article['title'])
        img.append(article['urlToImage'])
        url.append(article['url'])
    mylist = zip(news, desc, img, url)

    return render(request, 'index.html', context={'mylist':mylist})