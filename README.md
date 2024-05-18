## Djangolio Setup App

This project is a part of a group of project that I have developed
allong side with the newboston tutorial series for full stack django app
deploiyment .

## Titorial 1 : Setup

To just make every thing clear and easy to understand. I want to save all the setup process of this project in here, So when I came back or if I want to start a new project I can do so without any problems and I can refer to it whenever I need.

### Step 1: folders structure

Create a new project using django admin command .
Run this :
```sh
django-admin startproject project
```
* change the name of the main folder to your project name .
* Rename the project folder into a "core".
* create the gitignore file and add the next lines : "check the current git ignore on this project".
* Create the readme.rst file .
* make the core above the manage.py file so now the main project folder that contains " settings.py and all our main project files will be under PROJECT_NAME/core/project .






### Step 2: install needed packages

* Install poetry "https://python-poetry.org/" using pip :

```sh
pip install poetry
```

* Create a new poetry project :

```sh
poetry init
```
* Add the next lines to the pyproject.toml file : "check the current pyproject.toml on this project".
* Run poetry install.
* create the venv file using this command :
 ```sh
 python -m venv myenv
```


### Step 3 : project setup

* Now lets create first the make.ps1 script file that runs the powershell command to make our life easier with poetry " see the current make.ps1 file "
* Now lets modify on the settings.py so it can run the project.
    + create a folder called settings (create __init__.py inside it so it will become a python package).
    + create a folder called templates inside this settings folder (create __init__.py inside it).
    + Inside settings create the base.py that is a copy of the main settings.py file.
    + Now delete the settings.py file.
    + cut the BAS_DIR variable initialisation into the __init__.py file of the settings package and make sure it references the base dir adding ".parent" declaration.
    + Make sure ROOT_URLCONF is correct .
    + At this moment don't forget to install django-split-setttings package .
    + Now inside settings/templates create a new settings.dev.py that will contain the two variables like so :

    `
    SECRET_KEY = 'django-insecure-...'`
    `DEBUG = True
    `
    + But in the base file we modify these parameters to be like this :

    `
    SECRET_KEY = NotImplemented `
    `DEBUG = False
    `
    + At this stage lets create the local folder and copy the settings.dev.py into it :
    ```
    mkdir -p local
    cp .\core\project\settings\templates\settings.dev.py .\local\
    ```

* We have created our new settings behavior , but we stil need some utiliies functions to complete this for that we have to follow this steps :
    + Under PROJECT_NAME/core we must create a new python package named general
    + Inside this package another package called utils
    + and inside this last one we create two python files : collections.py, misc.py .
    + Now we need to create the settings.py for this utilities package.

Theses settings.py inside utilities folder is to create and automate the hole process of setting up the project environement virables from Docker environement variables automaticaly for example.

* Create the get_settings_from_environement() function inside the utils/settings.py file : this function basicly will take the environement variables and create a dictionary with the key and value of the environement variables.


### Step 4 : More custom settings

* On settings folder lets modify it by adding
    the included settings files and the two main project variables which are :
    + ENV_VAR_SETTINGS_PREFIX = "CORESETTINGS_"
    + LOCAL_SETTINGS_PATH = "local/settings.dev.py"

* Add custom.py setting file which include all the settings that arn't django specific settings .
* Add envars.py which runs the deep_merge() function to merge the system environement variables into our project environement variables.

* Create the docker.py settings that will be used to set up the docker environement variables.

At this point every thing is set for a basic django well set up project.
```sh
.\make.ps1 run-server
```
## Tutorial 2 - EditorConfig, Flake8, and pre-commit

### Step 1 : EditorConfig
EditorConfig helps maintain consistent coding styles for multiple developers working on the same project across various editors and IDEs. The EditorConfig project consists of a file format for defining coding styles and a collection of text editor plugins that enable editors to read the file format and adhere to defined styles. EditorConfig files are easily readable and they work nicely with version control systems.

* Create a.editorconfig file in the root of the project.
* Add the following content to the.editorconfig file:
    ```
    [*.{html,py}] # apply these editor settings on html and python files
    charset = utf-8
    indent_size = 8
    indent_style = space
    max_line_length = 120
    ```
### Step 2 : Flake8
Flake8 is a tool for checking the style and quality of Python code. It checks for issues such as coding style violations, programming errors, and the use of unsafe constructs. If you are using Flake8 and you encounter a situation where you want to ignore specific lines or types of errors, you can use inline comments to tell Flake8 to ignore them.

Run this command to install Flake8 on your dev poetry dependencies :  ```poetry add -D flake8```

check if it works : ```poetry run flake8 --help```

Use it to check the code style of the project : ```poetry run flake8 .\core\manage.py```

+ Lets make the flake8 configuration to ignore some folders and files :
    + create a .flake8 file in the root of the project
    + After filing our the .flake8 file, we will run this command ```poetry run flake8```

### Step 3 : pre commit
pre-commit is a framework for managing and maintaining multi-language pre-commit hooks. It is a tool that runs a set of checks on your staged files before you commit them.

hooks are a bunch of scripts that are run before you commit your code and checks for some issues that you might have in your code.
__You can create your own custom hooks__.

+ Install pre-commit : ```poetry add --group dev pre-commit```
+ Create the .pre-commit-config.yaml file in the root of the project
+ run this command to generate a sample code for the.pre-commit-config.yaml file : ```poetry run pre-commit sample-config```
+ copy the output sample hooks configuration and paste it in the.pre-commit-config.yaml file
+ run this command to install the hooks : ```poetry run pre-commit install```
+ run this command to check the hooks : ```poetry run pre-commit run --all-files```
+ now we need to configure ou pyproject.toml file to use the pre-commit hooks. Example of isort tool :
```
[tool.isort]
multi_line_output = 5
line_length = 119
```
+ add these commands to our make.ps1 file .


## Tutorial 3 - Logging

Django uses pthon logging module to log the messages.
Check this out for more infos https://docs.python.org/3/library/logging.config.html .
+ first lets create the logging .py .
+ Create the log formatter : Formatters define the structure and content of the log messages. They specify how the log record should be formatted, including the date, time, log level, logger name, and the actual log message. Formatters ensure that the log output is consistent and readable, making it easier to analyze and debug.
+ Create the log handlers : Handlers determine where the log messages are sent. They can direct log messages to various destinations such as the console, files, or external systems. Each handler can have its own level and formatter. Handlers are added to loggers to manage the output and distribution of log records.
+ Create the loggers : Loggers are the primary entities in the logging configuration. They are responsible for capturing log messages generated by the application. Each logger is identified by a name and has a level that determines the minimum severity of messages it will handle. Loggers can be organized in a hierarchy, allowing for granular control over logging output.
+ The loggin levels from lower to higher :
    DEBUG, INFO, WARNING, ERROR, CRITICAL.

+ Adding the log styling package called : colorlog .
    + To well apply our styling to our logs we need to add these lines in our local/settings.py file :
    ```
    LOGGING['formatters']['colored'] = {  # type: ignore
    '()': 'colorlog.ColoredFormatter',
    'format': '%(log_color)s%(asctime)s %(levelname)s %(name)s %(bold_white)s%(message)s',
    }
    LOGGING['loggers']['core']['level'] = 'DEBUG'  # type: ignore
    LOGGING['handlers']['console']['level'] = 'DEBUG'  # type: ignore
    LOGGING['handlers']['console']['formatter'] = 'colored'  # type: ignore
    ```
    + with all set we must see our logs colored now.


## Tutorial 4 - Docker

Before start dockerizing lets clone the Coocking core project from github :
+ link one : https://github.com/thenewboston-developers/Cooking-Core
+ link two :

#### Key notes :
* Delete the db.sqlite3 file
* install the python postgress package : __psycopg2__ .

+ docker-compose.yml file : is a file that contains all the configuration of the services of our app . For example in our case we have a postgres service "db" and a django service "app".

+ **db** service : is a service that contains the postgres database.
    ```
    db:
    image: postgres:16.3-alpine
    restart: unless-stopped
    ports:
      - '5432:5432'
    environment:
      POSTGRES_DB: cooking_core
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postDB
    volumes:
      - postgresql-data:/var/lib/postgresql/data
      ```
the image
+ **app** service : is a service that contains the django app.
```
app:
    build: .
    restart: unless-stopped
    ports:
      - '8000:8000'
    depends_on:
      - db
    environment:
      COOKING_CORE_SETTING_DATABASES: '{"default":{"HOST":"db"}}'
      COOKING_CORE_SETTING_LOCAL_SETTINGS_PATH: 'local/settings.prod.py'

volumes:
  postgresql-data:
    driver: local
```

## Tutorial 5 - Deploying the Backend

### Step 1 : new user on Amazon

+ Create an new user on Amazon and give him the right to create administrate the S3 bucket whichi is the permission called "AmazonS3FullAccess" .
+ Add to this user the Access Key credentials.

### Step 2 : Create the S3 Bucket

+ Create a new S3 bucket.
+ Give it a name "firstapp-backend".
+ Disable the option "Block all public access".
+ Add these lines on the permissions of the bucket, more specifically on the "Cross-origin resource sharing (CORS)" :
```
[
  {
    "AllowedHeaders": ["*"],
    "AllowedMethods": ["GET"],
    "AllowedOrigins": ["*"],
    "ExposeHeaders": []
  }
]
```
