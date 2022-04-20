# gnews-api
GNews API for Healthjump

## Requirements:
- [x] Fetching N news articles
- [ ] Finding a news article with a specific topic
- [ ] Finding a news article with a specific start or end date
- [x] Searching by keywords
- [x] Include a cache

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
| q | None | Filter for articles that match keywords. If using this, it will search all of GNews's articles and not just the top articles |
