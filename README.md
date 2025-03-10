# python-thenewsapi
A python wrapper for https://thenewsapi.com

All params from their website are supported in the functions

You can install by using:
````bash
pip install python-thenewsapi
````
Or build it your self using `setup.py`

## Functions

#### Top Stories
````python
import thenewsapi

tna = thenewsapi.TheNewsAPIClient('API_KEY')
    
top_stories = tna.get_top_stories()
    
print(top_stories)
````
#### All News
````python
import thenewsapi

tna = thenewsapi.TheNewsAPIClient(API_KEY)
    
all_news = tna.get_all_news()
    
print(all_news)
````
#### Similar News
````python
import thenewsapi

tna = thenewsapi.TheNewsAPIClient(API_KEY)
    
similar_news = tna.get_similar_news(NEWS_UUID)
    
print(similar_news)
````
#### News By UUID
````python
import thenewsapi

tna = thenewsapi.TheNewsAPIClient(API_KEY)
    
news_by_uuid = tna.get_news_by_uuid(NEWS_UUID)
    
print(news_by_uuid)
````
#### Sources
````python
import thenewsapi

tna = thenewsapi.TheNewsAPIClient(API_KEY)
    
sources = tna.get_sources()
    
print(sources)
````
#### Headlines (Standard+ tier needed)
````python
import thenewsapi

tna = thenewsapi.TheNewsAPIClient(API_KEY)
    
headlines = tna.get_headlines()
    
print(headlines)
````
If you want to use multiple values for one param, I suggest you use lists to make it more relateable, like:
````python
tna.get_top_stories(locale=['ae','ar'])
````
