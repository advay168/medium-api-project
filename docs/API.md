# API Documentation
## Routes
### Tags
**URL**: `/tags`

**Method**: `GET`

#### Parameters:
No parameters
#### Response:
**Code**: `200 OK`

**Schema**: `[string]`

**Example Body:**
````json
[
  "tag1",
  "tag2"
]
````
### Trending articles
**URL**: `/hot/{limit}`

**Method**: `GET`

#### Parameters:
##### Path parameters:
`limit`: Number of articles to request
#### Response:
**Code**: `200 OK`

**Schema**: [[Article](#article)]

**Example Body:**
````json
[
    {
        "author": "example_author",
        "title": "example_title",
        "blurb": "example_blurb",
        "time": "example_time",
        "thumbnail": "example_thumbnail",
        "link": "example_link"
    }
]
````
### Trending articles by tag
**URL**: `/hot/tag/{tag_name}/{limit}`

**Method**: `GET`

#### Parameters:
##### Path parameters:
`tag_name`: Name of tag to view articles of  
`limit`: Number of articles to request
#### Response:
**Code**: `200 OK`

**Schema**: [[Article](#article)]

**Example Body:**
````json
[
    {
        "author": "example_author",
        "title": "example_title",
        "blurb": "example_blurb",
        "time": "example_time",
        "thumbnail": "example_thumbnail",
        "link": "example_link"
    }
]
````
## Schemas
### Article
#### Example Data
````json
{
    "author": "example_author",
    "title": "example_title",
    "blurb": "example_blurb",
    "time": "example_time",
    "thumbnail": "example_thumbnail",
    "link": "example_link"
}
````
#### Fields
`author` : Author of the article  
`title` : Title of the article  
`blurb` : Short description of the article  
`time` : Average time to read the article  
`thumbnail` : Link to thumnail of the article  
`link` : Link to the article  
