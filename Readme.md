# Install
### Python 설치  
> version 3.9.x [Python](https://www.python.org/downloads/)
```terminal
$ pip3 --version
pip 20.2.3 from /Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pip (python 3.9)
```
### 가상 환경 셋업
> 개발 프로젝트 별 pyton version과 모듈 및 패키지 충돌을 해결하기 위해서 가상 환경 구성
```zsh
$ pip3 install virtualenv
$ virtualenv --version
virtualenv 20.2.2 from /Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/virtualenv/__init__.py
$ virtualenv --python=python3 devenv
(created...)
$ source ./devenv/bin/activate
$ pip --version
pip 20.3.1 from /Users/yungwoolee/Bitbucket/python/devenv/lib/python3.9/site-packages/pip (python 3.9)
```
## New App
```zsh
$ python manage.py startapp youtube
```
## Init project
### django install
```zsh
$ pip install django
(installing)
Successfully installed ...
```

### django-admin install
```zsh
$ django-admin startproject mainApp
$ cd mainApp
```
### Server start
> default port 는 8000
```zsh
$ python manage.py runserver 3200
```

# SSL(For Mac)
> Finder 에서 "Install Certificates.command" 실행
>> Folder 경로 /Applications/Python 3.9 로 이동  
>> "Install Certificates.command" 실행