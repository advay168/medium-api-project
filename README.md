# Medium API Project
This project provides an API to explore trending articles on Medium.  
Visit the website at [https://medium-api-project.herokuapp.com/](https://medium-api-project.herokuapp.com/)  


https://user-images.githubusercontent.com/23453652/170811434-b3c490e8-642e-465c-89de-1cef2894e8fd.mp4



## Table of Contents
1. [Instructions for running locally](#local)
   1. [Prerequisites](#prerequisites)
   2. [Web API](#web-api)
   3. [Command Line Interface](#cli)
      * [Prebuilt app](#prebuilt-app)
      * [Run from source](#run-src)
      * [Build app](#build)
2. [Technology used](#stack)
3. [API Reference](#api-reference)

## Instructions for running locally <a name="local"></a>
### Prerequisites
* Install [git](https://git-scm.com/downloads) and [python](https://www.python.org/downloads/)
* Clone the repository
````bash
git clone https://github.com/advay168/medium-api-project.git
````
* Change working directory
````bash
cd medium-api-project
````
> Note: all further instructions assume you have changed to the correct directory (/path/to/dir/medium-api-project)
* Create virtual environment
````bash
python -m venv .venv
````
* Activate virtual environment
````bash
./.venv/Scripts/activate
````
* Install requirements
````bash
pip install -r requirements.txt
````
### Web API
* Run the server
````bash
uvicorn src.webapi:main --port 8000
````
* Visit the site at `http://127.0.0.1:8000/`
### Command Line Interface <a name="cli"></a>
#### Prebuilt app
* Download `app.pyz` from the [releases](https://github.com/advay168/medium-api-project/releases/latest)
* Run the app
````bash
python app.pyz
````
#### Run from source <a name="run-src"></a>
* Run the app
````bash
python -m src.cli
````
#### Building the app from source  <a name="build"></a>
* Run the script made for creating a build directory, installing all requirements and creating the zipapp
````bash
python create_application.py
````
* (Optional) delete the build directory
````bash
rm -r ./build/
````
## Technology used: <a name="stack"></a>
* Python 3.9
    * fastapi
    * uvicorn
    * pydantic
    * aiohttp
    * regex
    * mypy
    * flake8
    * typer
    * rich
    * zipapp

## API Reference
The API reference for the webapi is available at [/docs/web.md](/docs/web.md)
The API reference for the CLI is available at [/docs/cli.md](/docs/cli.md)
