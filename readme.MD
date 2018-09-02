# CIEX
Training project for CI. API based on tornado. 

# How to install 


- With docker:
   - If it need - change env in ```src/environ.env``` (By default it for Docker)
   - run ```docker-compose build```
   - run ```docker-compose up```

- Without docker:
   - Change env in ```src/environ.env```
   - ```cd src```
   - run ```python3 main.py```
   
# Tests

- With docker:
   - ```docker-compose exec ciex ./runtests.sh``` 
   2) for report ```coverage report```

- Without docker:
   - ```cd src```
   - ```./runtests.sh```
   - for report ```coverage report```
# Project Goals

The code is written educational purposes. 
