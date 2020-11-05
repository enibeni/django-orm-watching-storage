# Bank security console

This based on Djanogo framework website provides tools to keep a log of bank reservoir visitors

### How to install

To use this script you should provide keys to establish connection with bank database in .env file:
- DB_ENGIN
- DB_HOST
- DB_PORT
- DB_NAME
- DB_USER
- DB_PASSWORD

Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```

# Quickstart

to start website locally just run this command
```bash
$ python3 main.py
```

The website will be available in browser at http://0.0.0.0:8000/

### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).