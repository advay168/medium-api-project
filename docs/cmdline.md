# Command line API Documentation
> Note: The documentation refers to the application as `app.pyz`
## Basics
### Running the app
````bash
python app.pyz
````
### Viewing the help for commands
To view help for the whole app:
````bash
python app.pyz --help
````
To view help for a particular command:
````bash
python app.pyz mycommand --help
````
## Commands
### List Tags
**Command**: `python app.pyz list-tags`
#### Arguments
No arguments
#### Options
No options
#### Info
Lists the top tags from medium.com

### Trending
**Command**: `python app.pyz trending`
#### Arguments
No arguments
#### Options
`--limit`: Number of articles to request
#### Info
Display {limit} trending articles from the homepage of medium.com

### Trending By Tag
**Command**: `python app.pyz tag TAG`
#### Arguments
`TAG`: Name of tag
#### Options
`--limit`: Number of articles to request
#### Info
Display {limit} trending articles for a particular {tag}.  
List top tags with the `list-tags` command
