# CIEX
Training project for CI. API based on tornado. 

# How to install 


- With docker:
   1) If it need - change env in ```src/environ.env``` (By default it for Docker)
   2) run ```docker-compose build```
   3) run ```docker-compose up```

- Without docker:
   1) Change env in ```src/environ.env```
   2) ```cd src```
   3) run ```python3 main.py```
   
# Tests

- With docker:
   1) ```docker-compose exec ciex ./runtests.sh``` 
   2) for report ```coverage report```

- Without docker:
   1) ```cd src```
   2) ```.\runtests.sh```
   3) for report ```coverage report```
# Project Goals

The code is written for CI educational purposes. 