# Capstone-Project

This project is mainly designed for users to record their favourite movie reviews. Their are three types of privacy for selection: private, 
friends only or public. Users can rate, put comments, add picture, add title and add author for each movie record, and we might add a new 
functionality "make friends" in the future.

# To run the program:

# first in Capstone-Project run

    pip install -r requirements.txt
  
    python3 manage.py runserver

# if unable to make the server run do so try the following

    python3 manage.py makemigrations Capstone_Project2
  
    python3 manage.py makemigrations users
  
    python3 manage.py migrate
  
    python3 manage.py runserver


# to run the front end vue

    cd capstone_project_vue

    npm install
  
    npm run serve
    
# webpage
    http://localhost:8080/#/login

#current users

    username: user1@gmail.com
    password: user1
    
    username: user2@gmail.com
    password: user2


