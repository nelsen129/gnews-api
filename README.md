# gnews-api
GNews API for Healthjump

## Setup
To setup, first add an API key for GNews to `.env`. The `.env` file should look like
```
API_KEY=<api_key>
```
Then, install requirements using
```
pip install -r requirements.txt
```
*Note: this has only been tested using Python 3.7*

Run server using
```
python3 backend.py
```
You will then be able to make requests


## Documentation:
### Articles Endpoint
This endpoint selects the top articles from GNews's top headlines. Articles are sorted by the most recent publish date first.

#### HTTP Request
```
GET http://127.0.0.1:5000/articles?
```

#### Query Parameters

| **Parameter** | **Default** | **Description** |
| --- | --- | --- |
| num | 10 | Number of articles to return. **100** is the maximum value | 
| topic | None | Set the articles topic. Must be one of **breaking-news**, **world**, **nation**, **business**, **technology**, **entertainment**, **sports**, **science**, or **health**. |
| q | None | Filter for articles that match keywords. If using this and not `topic`, it will search all of GNews's articles and not just the top articles |
| from | None | Keep articles with a publication date greater than or equal to the given date. ISO 8601 format (e.g. 2022-04-19T00:41:28Z) |
| to | None | Keep articles with a publication date less than or equal to the given date. ISO 8601 format (e.g. 2022-04-19T00:41:28Z) |


## Requirements:
- [x] Fetching N news articles
- [x] Finding a news article with a specific topic
- [x] Finding a news article with a specific start or end date
- [x] Searching by keywords
- [x] Include a cache
- [x] Documentation