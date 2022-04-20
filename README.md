# gnews-api
GNews API for Healthjump

## Requirements:
- [x] Fetching N news articles
- [ ] Finding a news article with a specific title
- [ ] Finding a news article with a specific author
- [ ] Searching by keywords
- [ ] Include a cache

## Documentation:
### Articles Endpoint
This endpoint selects the top articles from GNews's top headlines. Articles are sorted by the most recent publish date first.

**HTTP Request**
```
GET http://127.0.0.1:5000/articles?
```

**Query Parameters**

| **Parameter** | **Default** | **Description** |
| --- | --- | --- |
| num | 10 | Number of articles to return. **100** is the maximum value | 