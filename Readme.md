# Install
### 1. Python 설치  
> version 3.9.x [Python](https://www.python.org/downloads/)
```terminal
$ pip3 --version
pip 20.2.3 from /Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pip (python 3.9)
```
### 2. Project initial setup
#### Install shell
> virtualenv(가상환경 생성) 및 가상환경 활성화(activate) 후 필요 외부 module 설치
```zsh
$ pip3 install virtualenv
$ sh ./install
```

> ref. 가상 환경 셋업  
>> 개발 프로젝트 별 pyton version과 모듈 및 패키지 충돌을 해결하기 위해서 가상 환경 구성  
>> ```zsh
>> $ pip3 install virtualenv
>> $ virtualenv --version
>> virtualenv 20.2.2 from /Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/virtualenv/__init__.py
>> $ virtualenv --python=python3 devenv
>> (created...)
>> $ source ./devenv/bin/activate
>> $ pip --version
>> pip 20.3.1 from /Users/yungwoolee/Bitbucket/python/devenv/lib/python3.9/site-packages/pip  
>> (python 3.9)
>> ```
>> <br>

<br>

# Application Enviroment
> [python-dotenv]('https://pypi.org/project/python-dotenv/') 를 사용하여 .env 파일에 실행 변수 관리함.
```yaml
# [.env] 파일
LOG_LEVEL=DEBUG
```

<br>

# Start Server
> start shell 실행 하며 port 는 3200 으로 설정함.
```zsh
$ sh ./start
```

<br>

# Docker
## 1. Docker build
> docker build 시 "python:3.9" 이미지를 사용함.
```zsh
$ docker build --tag mainapp . 
```

<br>

## 2. Docker run
```zsh
$ docker run -d -p 3200:3200 --name mainapp mainapp:latest
```

<br>

# New App(e.g. add "youtube" app)
```zsh
$ python manage.py startapp youtube
```

<br>

# Ref. Init project(프로젝트 최초 생성시)
## django install
```zsh
$ pip3 install django
(installing)
Successfully installed ...
```

## django-admin install
```zsh
$ django-admin startproject mainApp
$ cd mainApp
```
<br/>

# SSL(For Mac)
> Finder 에서 "Install Certificates.command" 실행
>> Folder 경로 /Applications/Python 3.9 로 이동  
>> "Install Certificates.command" 실행