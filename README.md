# django-rest-school-api


## Project Overview;

1. This is a small rest-api app for management of schools and its students. 
2. You can perform CRUD operations on schools and students and each student belongs to a school, so a student cannot exist without a school.
3. Deployed on Heroku so you can test it

## Api Reference:

This api supports : get, post, put, path, delete for schools and students along with nested operations for students belonging to schools.

=> Urls (to test with browser):
You can visit this main url which will guide you further with 

https://school-app-imran.herokuapp.com/


## Urls (to test with postman) 

1. https://school-app-imran.herokuapp.com/schools/
2. https://school-app-imran.herokuapp.com/students/
3. https://school-app-imran.herokuapp.com/schools/school_id/students/
4. https://school-app-imran.herokuapp.com/schools/school_id/students/student_id/

## Api Features:

1. Perform CRUD operations for schools    
     
          desciption: create school object  
          URL: https://school-app-imran.herokuapp.com/schools/  
          method: POST  
          Form Data Fields:  
           "school_name": "Test School Name"  
           "maximum_number_of_students": 15 (not required, default is 50)  
    
2. Perform CRUD operations for students

          desciption: create student object  
          URL: https://school-app-imran.herokuapp.com/students/  
          method: POST  
          Form Data Fields:  
          "first_name": "Test first name"  
          "last_name": "test last name"  
          "school": "school id"  

3. Perform searching, filtering and ordering of both schools and studnets.  
  
          Example:  
          GET https://school-app-imran.herokuapp.com/schools/search?=school_name  

          School:  
          filter fields =  'school_name'  
          ordering fields = 'school_name', 'id'  
          search fields = 'school_name', 'id'  

          Student:  
          filter fields = 'first_name'  
          search fields = 'first_name', 'id'  

4. Perform Nested CRUD operations for students (belonging to schools)

          desciption: create student object for a school  
          URL: https://school-app-imran.herokuapp.com/schools/<school_id>/students/<student_id>/    
          method: POST  
          Form Data Fields:  
          "first_name": "Test first name"  
          "last_name": "test last name"    
    
**NOTE: Only form form data is accepted into requests (from postman) text/plain data is not unsupported!  
  
## Authorization:
1. This api features users creation with token based (which has an expiry as well) authentication, meaning with registering/login a token will be provided. 
2. The token need to be placed into headers of the request with the key "Authorization" and value as Token "token_value"
3. Auth applies for non-safe methods of schools/students i:e post/put/patch

### Auth Urls:
1. https://school-app-imran.herokuapp.com/auth/login/
2. https://school-app-imran.herokuapp.com/auth/register/
3. https://school-app-imran.herokuapp.com/auth/logout/

          Example for register:  
          URL: https://school-app-imran.herokuapp.com/schools/  
          method: POST  
          form_data:  
          "email": "imran@getnada.com",  
          "username": "imran@getnada.com",  
          "password": "123"  

          Example for login  
          URL: https://school-app-imran.herokuapp.com/auth/login/  
          method: POST  
          form data fields:  
          "email": "imran@getnada.com",  
          "username": "imran@getnada.com",  
          "password": "123"  


## Time taken in project
1. project setup/settings with postgress and installing depedencies (2 - 3 hours)
2. architechture design with keys and relations (1 hour)
3. django models and serializers (1 hour)
4. schools/students views (2 - 3 hours)
5. nested routers (0.5 - 1 hour)
6. authentication setup/models/views (1 hour)
7. deploying on heroku (1 hour)
