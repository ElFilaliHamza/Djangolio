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

- change the name of the main folder to your project name .
- Rename the project folder into a "core".
- create the gitignore file and add the next lines : "check the current git ignore on this project".
- Create the readme.rst file .
- make the core above the manage.py file so now the main project folder that contains " settings.py and all our main project files will be under PROJECT_NAME/core/project .

### Step 2: install needed packages

- Install poetry "https://python-poetry.org/" using pip :

```sh
pip install poetry
```

- Create a new poetry project :

```sh
poetry init
```

- Add the next lines to the pyproject.toml file : "check the current pyproject.toml on this project".
- Run poetry install.
- create the venv file using this command :

```sh
python -m venv myenv
```

### Step 3 : project setup

- Now lets create first the make.ps1 script file that runs the powershell command to make our life easier with poetry " see the current make.ps1 file "
- Now lets modify on the settings.py so it can run the project.

  - create a folder called settings (create **init**.py inside it so it will become a python package).
  - create a folder called templates inside this settings folder (create **init**.py inside it).
  - Inside settings create the base.py that is a copy of the main settings.py file.
  - Now delete the settings.py file.
  - cut the BAS_DIR variable initialisation into the **init**.py file of the settings package and make sure it references the base dir adding ".parent" declaration.
  - Make sure ROOT_URLCONF is correct .
  - At this moment don't forget to install django-split-setttings package .
  - Now inside settings/templates create a new settings.dev.py that will contain the two variables like so :

  `
  SECRET_KEY = 'django-insecure-...'`
  `DEBUG = True
  `

  - But in the base file we modify these parameters to be like this :

  `  SECRET_KEY = NotImplemented`
  `DEBUG = False
  `

  - At this stage lets create the local folder and copy the settings.dev.py into it :

  ```
  mkdir -p local
  cp .\core\project\settings\templates\settings.dev.py .\local\
  ```

- We have created our new settings behavior , but we stil need some utiliies functions to complete this for that we have to follow this steps :
  - Under PROJECT_NAME/core we must create a new python package named general
  - Inside this package another package called utils
  - and inside this last one we create two python files : collections.py, misc.py .
  - Now we need to create the settings.py for this utilities package.

Theses settings.py inside utilities folder is to create and automate the hole process of setting up the project environement virables from Docker environement variables automaticaly for example.

- Create the get_settings_from_environement() function inside the utils/settings.py file : this function basicly will take the environement variables and create a dictionary with the key and value of the environement variables.

### Step 4 : More custom settings

- On settings folder lets modify it by adding
  the included settings files and the two main project variables which are :

  > ENV*VAR_SETTINGS_PREFIX = "CORESETTINGS*"
  > LOCAL_SETTINGS_PATH = "local/settings.dev.py"

- Add custom.py setting file which include all the settings that arn't django specific settings .
- Add envars.py which runs the deep_merge() function to merge the system environement variables into our project environement variables.

- Create the docker.py settings that will be used to set up the docker environement variables.

At this point every thing is set for a basic django well set up project.

```sh
.\make.ps1 run-server
```

## Tutorial 2 - EditorConfig, Flake8, and pre-commit

### Step 1 : EditorConfig

EditorConfig helps maintain consistent coding styles for multiple developers working on the same project across various editors and IDEs. The EditorConfig project consists of a file format for defining coding styles and a collection of text editor plugins that enable editors to read the file format and adhere to defined styles. EditorConfig files are easily readable and they work nicely with version control systems.

- Create a.editorconfig file in the root of the project.
- Add the following content to the.editorconfig file:
  ```
  [*.{html,py}] # apply these editor settings on html and python files
  charset = utf-8
  indent_size = 8
  indent_style = space
  max_line_length = 120
  ```

### Step 2 : Flake8

Flake8 is a tool for checking the style and quality of Python code. It checks for issues such as coding style violations, programming errors, and the use of unsafe constructs. If you are using Flake8 and you encounter a situation where you want to ignore specific lines or types of errors, you can use inline comments to tell Flake8 to ignore them.

Run this command to install Flake8 on your dev poetry dependencies : `poetry add -D flake8`

check if it works : `poetry run flake8 --help`

Use it to check the code style of the project : `poetry run flake8 .\core\manage.py`

- Lets make the flake8 configuration to ignore some folders and files :
  > create a .flake8 file in the root of the project
  > After filing our the .flake8 file, we will run this command `poetry run flake8`

### Step 3 : pre commit

pre-commit is a framework for managing and maintaining multi-language pre-commit hooks. It is a tool that runs a set of checks on your staged files before you commit them.

hooks are a bunch of scripts that are run before you commit your code and checks for some issues that you might have in your code.
**You can create your own custom hooks**.

- Install pre-commit : `poetry add --group dev pre-commit`
- Create the .pre-commit-config.yaml file in the root of the project
- run this command to generate a sample code for the.pre-commit-config.yaml file : `poetry run pre-commit sample-config`
- copy the output sample hooks configuration and paste it in the.pre-commit-config.yaml file
- run this command to install the hooks : `poetry run pre-commit install`
- run this command to check the hooks : `poetry run pre-commit run --all-files`
- now we need to configure ou pyproject.toml file to use the pre-commit hooks. Example of isort tool :

```
[tool.isort]
multi_line_output = 5
line_length = 119
```

- add these commands to our make.ps1 file .

## Tutorial 3 - Logging

Django uses pthon logging module to log the messages.
Check this out for more infos https://docs.python.org/3/library/logging.config.html .

- first lets create the logging .py .
- Create the log formatter : Formatters define the structure and content of the log messages. They specify how the log record should be formatted, including the date, time, log level, logger name, and the actual log message. Formatters ensure that the log output is consistent and readable, making it easier to analyze and debug.
- Create the log handlers : Handlers determine where the log messages are sent. They can direct log messages to various destinations such as the console, files, or external systems. Each handler can have its own level and formatter. Handlers are added to loggers to manage the output and distribution of log records.
- Create the loggers : Loggers are the primary entities in the logging configuration. They are responsible for capturing log messages generated by the application. Each logger is identified by a name and has a level that determines the minimum severity of messages it will handle. Loggers can be organized in a hierarchy, allowing for granular control over logging output.
- The loggin levels from lower to higher :
  DEBUG, INFO, WARNING, ERROR, CRITICAL.

- Adding the log styling package called : colorlog .
  - To well apply our styling to our logs we need to add these lines in our local/settings.py file :
  ```
  LOGGING['formatters']['colored'] = {  # type: ignore
  '()': 'colorlog.ColoredFormatter',
  'format': '%(log_color)s%(asctime)s %(levelname)s %(name)s %(bold_white)s%(message)s',
  }
  LOGGING['loggers']['core']['level'] = 'DEBUG'  # type: ignore
  LOGGING['handlers']['console']['level'] = 'DEBUG'  # type: ignore
  LOGGING['handlers']['console']['formatter'] = 'colored'  # type: ignore
  ```
  - with all set we must see our logs colored now.

## Tutorial 4 - Docker

Before start dockerizing lets clone the Coocking core project from github :

- link one : https://github.com/thenewboston-developers/Cooking-Core
- link two :

#### Key notes :

- Delete the db.sqlite3 file
- install the python postgress package : **psycopg2** .

* docker-compose.yml file : is a file that contains all the configuration of the services of our app . For example in our case we have a postgres service "db" and a django service "app".

* **db** service : is a service that contains the postgres database.
  `    db:
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
     `
  the image
* **app** service : is a service that contains the django app.

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

- Create an new user on Amazon and give him the right to create administrate the S3 bucket whichi is the permission called "AmazonS3FullAccess" .
- Add to this user the Access Key credentials.

### Step 2 : Create the S3 Bucket

- Create a new S3 bucket.
- Give it a name "firstapp-backend".
- Disable the option "Block all public access".
- Add these lines on the permissions of the bucket, more specifically on the "Cross-origin resource sharing (CORS)" :

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

### Step 3 : Create and configure the EC2 instance

- Create a new EC2 instance.
- Choose the "Ubuntu Server 22.00 LTS (HVM), SSD Volume Type - ami-00216466666666666" image.
- Choose the "t2.micro" instance type "The free tier eligible one".
- Choose the "Create a new key pair" option (if you don't have one already).
- Give it a name "firstapp-keypaire".
- The key private key pair saved on this repo on the directory "firstapp-keypaire.pem".
- Choose the "Create a new security group" option.
- Add the following rules on the security group :
  > Allow SSH trafic from anywhere.
  > Allow HTTP trafic from anywhere (we want to allow the Http is to be able to configure the https using the http request at the beginning ) .
  > Allow HTTPS trafic from anywhere.

At this step our EC2 is ready we can click "Launch instance" button.

- Wait until the instance is running.
- Connect and configure the instance using ssh commands (before running these commands head over the private key file and remove all the permissions from all other users) :
  - Connect to the ubuntu sys using ssh :
    `ssh -i .\firstapp-keypair.pem ubuntu@50.19.58.239`
  - After you are connected to the instance you can run the following commands :
    - Update the ubuntu os packages :
      `sudo apt update -y && sudo apt upgrade -y`
    - Install all systme requirements :
      ```
      sudo apt install -y apt-transport-https ca-certificates curl software-properties-common git nginx certbot python3-certbot-nginx
      ```

#### Setup docker on the Ec2 instance

Download docker gpg "GNU Privacy Guard" key used to verify the authenticity of docker packages during the installation :

> `curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg`

**Verifying Authenticity and Integrity: The downloaded packages are signed with Docker's GPG key. The package manager uses the GPG key stored in /usr/share/keyrings/docker-archive-keyring.gpg to verify the signature on the packages. If the signature is valid, it means that the packages were indeed created by Docker and have not been altered since they were signed. If the signature verification fails, the package manager will reject the packages, preventing installation.**

- Add the docker repository to the apt sources list "so the apt package manager could recognize it when installing docker from docker officiale source" :
  ```
  echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
  ```
- Update the ubuntu os packages again :
  `sudo apt update -y && sudo apt upgrade -y`
- Install docker :
  `sudo apt install -y docker-ce docker-ce-cli containerd.io`
- Install docker-compose :
  `sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose`
- Make the docker-compose binary executable :
  `sudo chmod +x /usr/local/bin/docker-compose`
- Add my user to the docker group :
  `sudo usermod -aG docker $USER`
- Logout and login again to apply the changes :
  `exit`
  `login`
- Check if docker is installed :
  `docker --version`
- Check if docker-compose is installed :
  `docker-compose --version`
- Check if python3 is installed :
  `python3 --version`
- Check if git is installed :
  `git --version`

#### Setup the project :

With all set, lets start configuring our project :

- clone the project from github :
  ```
  git clone https://github.com/ElFilaliHamza/Cooking-core.git
  ```
- Go to the project directory .
- create the "local" directory for the production environement :
  > `mkdir -p local`
  - Create the settings.prod.py file `sudo nano local/settings.prod.py` and type these configurations :
    ```
    DEBUG = False
    SECRET_KEY = '_u81u$mo@u!=v(esb8k9_gvo-vrlf&llb0e&f@+c&bzim&c2s_'
    CSRF_TRUSTED_ORIGINS = ['https://domain-name', 'https://www.domain-name']
    AWS_ACCESS_KEY_ID = 'AKIA26J6J6QJELVLCMFX'  # So our aws user can access the aws services
    AWS_SECRET_ACCESS_KEY = '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'
    AWS_STORAGE_BUCKET_NAME = 'firstapp-backend'
    ```
  - Now we can run : `docker-compose build` .
  - And then : `docker-compose up -d` ( -d used to run the docker on demon mode "on background").
  - type 'docker ps' to see the running containers.
  - After this we can create our superuser using this command : `docker exec -it de332cfd1371  /bin/bash` .
    > And then in the exec mode of docker container run : `make superuser`
  - And then we need to run these commands :
    > `make shell ` = `poetry run python -m cooking_core.manage shell`
    - In the django app python shell type these commands :
      > `from cooking_core.config.models import Config` > `Config.objects.create(owner=None, transaction_fee=1)` > `exit()`

#### Setup the nginx configuration :

First we need to remove the nginx default config file : `sudo rm /etc/nginx/sites-enabled/default`

- Add the new nginx configuration default file : `sudo nano /etc/nginx/sites-available/default`
- Add the following configuration :

```
server {
    listen 80;
    server_name localhost;

    location / {
        proxy_pass http://localhost:8000;

        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";

        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

- Test the new configuration : `sudo nginx -t`
- Restart the nginx service : `sudo systemctl restart nginx`
- Allow nginx throw firewall : `sudo ufw allow 'Nginx Full'`

#### Set up the Elastic IP address

The Ec2 instance ip is not static, so we need to set up an Elastic IP address.

- Go to the EC2 service and create a new Elastic IP address from the Elastic IP page .
- After creating an Elastic IP select it and click on actions > associate address.
- Choose the instance and associate the Elastic IP address.
- After this we need to head over the Rout 53 service and create a new record set.
- Select the domain name and the type as A and the value as the Elastic IP address.
- Save the record set.

#### Set up the ssl certificate

(if you have a domain name unless you can access your backend using the Elastic public IP address)

After having the domain record up and running check "https://domainschecker.org/"

- Go to the server terminal and type this command : `sudo certbot --nginx`, "This command will ask for the domain name and the email address".
- Now run a dry run : `sudo certbot --nginx --dry-run` which will check the auto renew of the certificate is setup .
- Another time we need to remove the default config file : `sudo rm /etc/nginx/sites-enabled/default`
- Now we need to create a new config file : `sudo nano /etc/nginx/sites-available/domain.com`
- Copy the following code and paste it in the file :

```
server {
    listen 80 default_server;
    return 301 https://$host$request_uri;
}

server {
    listen 443 ssl default_server;
    ssl_certificate /etc/letsencrypt/live/{domain-name}/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/{domain-name}/privkey.pem;

    ssl_session_cache shared:le_nginx_SSL:10m;
    ssl_session_timeout 1440m;
    ssl_session_tickets off;
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_prefer_server_ciphers off;

    client_max_body_size 20M;

    location / {
    proxy_pass http://localhost:8000/;

    proxy_http_version 1.1;
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection "upgrade";

    proxy_redirect off;
    proxy_buffering off;

    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;
    proxy_set_header X-Forwarded-Host $http_host;
  }
}
```

## Tutorial 6 - Deploying the Frontend

### Step 1 - Configure Coocking-frontend

- ```
  git clone https://github.com/thenewboston-developers/Cooking-Frontend.git
  ```
- Install packages : `npm install`
- Build the frontend app : `npm run build`
- Install the serve package : `npm install -g serve`
- Run the frontend app : `serve -s build`

### Step 2 - Configure the S3 bucket to hold our built project

- At this step we will be using the AWS CLI to configure the S3 bucket.
- Create a bucket with the name `cooking-frontend-bucket`
- Configure the bucket as a static website hosting bucket.
  > Go to the bucket properties and click on the `Static website hosting` tab.
  > Set the index document to `index.html` and the error document to `index.html`.
  > Click on `Save`.
- After this upload all the existing file in the `build` folder to the bucket.

  > Go to the bucket hit upload and drop all the files in there .

- Configure the bucket to be publicly accessible.
- Create a
- Upload the contents of the `build` folder inside the bucket.
- Configure the bucket to be publicly accessible.
  > In Block public access settings, uncheck the block all public access settings.
  > Click on `Save`.
- Update the bucket policy to allow public access.
  > Go to the bucket properties and click on the `Permissions` tab.
  > Click on `Bucket Policy` and paste the following policy:
  ```
    {
    "Version": "2012-10-17",
    "Statement": [
        {
          "Sid": "PublicReadGetObject",
          "Effect": "Allow",
          "Principal": "*",
          "Action": "s3:GetObject",
          "Resource": "arn:aws:s3:::{bucket-name}/*"
        }
      ]
    }
  ```

### Step 3 - Configure CloudFront to serve our static website

- Create a CloudFront distribution.
  > Go to the CloudFront service and click on `Create Distribution`.
  > Select the


## Tutorial 7 - pytest

### Step 1 - install dependencies

lets install our dependencies first :
```
poetry add pytest pytest-xdist pytest-django model-bakery
```
1. pytest :
pytest is a mature full-featured Python testing tool that helps you write better programs. It provides a simple and scalable way to write small tests, yet supports complex functional testing for applications. With pytest, you can create test cases that are more readable and efficient.

2. pytest-xdist :
pytest-xdist is a plugin for pytest that allows you to execute tests in parallel, speeding up the testing process. This is particularly useful for large test suites that take a long time to execute sequentially. It can also be used to run tests in multiple CPUs and across multiple nodes.

3. pytest-django :
pytest-django is a plugin for pytest that provides a set of useful tools for testing Django applications. It allows you to use pytest's features with Django projects and makes it easier to test Django applications. It handles creating a test database, and can reuse the existing test database from Django’s standard test command, which speeds up the tests.

4. model-bakery :
model-bakery (formerly known as model_mommy) is a library for Django that simplifies the creation of instances of Django models. It can automatically generate instances of Django model classes, which is very useful in tests and anywhere else you need to generate model instances with filled fields according to the field types.


### Step 2 - tests and fixtures

In python a fixture is a function that is used to setup the environment for a test.

> First setup the pytest configurations in the pyproject.toml file, by adding __[tool.pytest.ini_options]__ section.

+ Create the fixture called accounts.py in the tests package under the fixtures package {Note you have to create both of these packages manually} in Accounts folder on the project direcory "/cooking-core".
+ After creating our fixtures we must create the conftest.py which is a file used by pytest to load the fixtures.
+ In conftest.py we will import the fixtures we created in the fixtures folder.
+ Now we will create our first test file called test_api.py . And run the test file using pytest command.
```sh
poetry run pytest -v -rs -n auto --show-capture=no
```


## Tutorial 8 - GitHub Actions and Workflows

### Step 1 : setup github workflow

+ Create the .github directory .
+ Create the workflows directory .
+ And voilla!! start typing your workflows as a .yml file extension.

+ On the workflow we can use theses key words :
```yml
name: {user-friendly-name}
on: [pull_request, workflow_call] # thses are the events that will execute our workflow .

jobs: # in here we specfy the jobs we will running and their steps which are just some bunch of commands.
  {job-name}:
    name: {job-user-friendly-name}
    runs-on: ubuntu-latest
    container: python:3.10.4-buster # this must be equivilent to the one in the Dockerfile.

    services: # the services that we must run on the workflow.
      db:
        image: postgres:14.2-alpine
        env:
          POSTGRES_DB: cooking_core
          POSTGRES_USER: postgres
          POSTGRES_PASSWORD: postDB

    steps: # each step represent an action that will be executed in the workflow.
      - uses: actions/checkout@v2 # this is a builtin step in github .

      - name: Install Poetry
        uses: abatilo/actions-poetry@v2.0.0 # this is also a built in action by a person called abatilo
        with:
          poetry-version: 1.8.3

      - name: Install Dependencies
        run: make install && make install-pre-commit

      - name: Lint
        run: make lint

      - name: Test
        run: make test
        env:
          COOKING_CORE_SETTING_DATABASES: '{"default":{"HOST":"db"}}'
          COOKING_CORE_SETTING_LOCAL_SETTINGS_PATH: './cooking_core/project/settings/templates/settings.github.py'
```

> Don't forget to make sure that in the workflow that the db user and pwd is correct as in the docker-compose file .

- After all these setup we can now push in a new branch then we can accept and compare the pull request which will triger our workflow automatically .



## Tutorial 9 - CI/CD

Last but not least we will setup a CI/CD pipeline using github actions. Which is the reason why I started typing and configuraing all these stuf for . Without further to do let's jump in!

### Step 1 : setup ssh comminication between our server and the github repo .

+ First let's generate an ssh key using this command on the powershell :
```sh
C:\Windows\System32\OpenSSH\ssh-keygen.exe -t rsa -b 4096 -f ./{github_ssh_key_name}
```

> Make sure you don't include a password on this ssh key to don't break the workflow automation and CI/CD things.

+ Now lets configure our github to hold the private key :
  + Go to your github account and click on the settings icon on the top right corner.
  + Then click on the "Secrets and variables" tab
  + Choose "actions" tab .
  + And create new secret with the name "SSH_PRIVATE_KEY" and paste the content of the private key file generated with the command right above.

+ Now lets store the generated public key on our Ec2 instance server :
```sh
sudo nano ~/.ssh/authorized_keys
```
> In this file we must add the public key generated with the command above.

+ We need two more variables which are the SSH_HOST and the SSH_USER :
  + SSH_HOST : the ip address of the ec2 instance server.
  + SSH_USER : the username of the ec2 instance server "ubuntu".


### Step 2 : write the CI/CD workflow

+ For this end we need to configure a new workflow .yml file that will mostly contains the next configurations :
```yml
name: {workflow_name}

on: # means that we will execute the workflow whenever we merge on the master branch a new thing.
  push:
    branches:
      - master

concurrency: # whenever we pushes a new thing right before the previous one is done, we will cancel the previous one and run another CI/CD workflow instead.
  group: master
  cancel-in-progress: true

jobs:
  quality-assurance: # run the quality assurance before deploying "Testing before deploying"
    name: Quality Assurance
    uses: ./.github/workflows/pr.yml

  deploy: # deployment steps .
    name: Deploy
    needs: quality-assurance # means we need to succed in the quality workflow before deploying.
    runs-on: ubuntu-latest
    steps: # we have two main steps the first one is configuring the connection and the second one is updating and rebuilding the existing app.
      - name: Configure SSH
        env: # reference all the environement variables stored on github .
          SSH_PRIVATE_KEY: ${{ secrets.SSH_PRIVATE_KEY }}
          SSH_HOST: ${{ secrets.SSH_HOST }}
          SSH_USER: ${{ secrets.SSH_USER }}
        # Now lets run the connection commands
        # because we are running in a blank ubuntu instance to
        # connect to our server we need to make the ssh directory
        # and add the ssh private key to it from the env variables.
        run: |
          mkdir -p ~/.ssh/
          echo "$SSH_PRIVATE_KEY" > ~/.ssh/github
          chmod 600 ~/.ssh/github
          cat >>~/.ssh/config <<END
          Host target
            HostName $SSH_HOST
            User $SSH_USER
            IdentityFile ~/.ssh/github
            LogLevel ERROR
            StrictHostKeyChecking no
          END
      - name: Run deploy
      # Now lets run the deployment :
      # first ssh into the target "Ec2 server" .
      # secondly bring down the containers .
      # then pull the latest code from the repo.
      # then rebuild the containers.
      # then bring up the containers with a forced recreation tag.
        run: |
          ssh target "cd Cooking-Core/ && docker-compose down && git pull && docker-compose build && docker-compose up -d --force-recreate"
```

+ After the workflow on github is seted up you can juste push your code and it's done , check your server it's updated automatically .



## Conclusion

As a junior web developper and a data scientist that aims to deploy my own solutions I needed this tutorial so much , I want to say thanks to thenewboston youtube channel team . I am very gratefull for this full explained and step by step tutorial . Now at least I have a blueprint to start with and a full working example to follow .
Along side with a lot of best practices advice . I write this repo for me and for any other person who is interested in these such great technologies .
If you have any questions don't hesitate to contact me on instagrame or linkedin .

insta: https://www.instagram.com/hamza_fun_games/

linkedin:  linkedin.com/in/hamza-el-filali-ma

As we say always : "__Don't give me the fish but teach me how to fish__".
