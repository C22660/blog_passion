<p align="center">
<img class=""
    src="./static/images/plume.png" 
    alt="logo_plume" 
    width="50" 
/>
</p>

![](frontend/public/images/logo_technos_readme.png)

# My blog passion and its API

**BLOG**

* Page articles
* Page events
* Page contact form

**API**


|	#	|	Endpoints	|	HTTP methods	|	URL	|
|	-----	|	-----------------------------	|	--------------	|	--------------------------------------------------------	|
|	1.	|	SignUp new user	|	POST	|	api/signup/	|
|	2.	|	Get all articles for visitors	|	GET	|	/api/articles	|
|	3.	|	Get an article for visitors via its id	|	GET	|	/api/articles/{id}/	|
|	4.	|	Get all articles for user authenticated	|	GET	|	/api/articles_admin	|
|	4.	|	Create a new article	|	POST	|	/api/articles_admin/	|
|	5.	|	Get an article for user authenticated via its id	|	GET	|	/api/articles_admin/{id}/	|
|	6.	|	Update an article for user authenticated via its id	|	PUT	|	/api/articles_admin/{id}/	|
|	7.	|	Destroy an article for user authenticated via its id	|	DELETE	|	/api/articles_admin/{id}/	|
|	8.	|	Get all events for visitors	|	GET	|	/api/events	|
|	9.	|	Get an event for visitors via its id	|	GET	|	/api/events/{id}/	|
|	10.	|	Get all events for user authenticated	|	GET	|	/api/events_admin	|
|	11.	|	Create a new event	|	POST	|	/api/events_admin/	|
|	12.	|	Get an event for user authenticated via its id	|	GET	|	/api/events_admin/{id}/	|
|	13.	|	Update an event for user authenticated via its id	|	PUT	|	/api/events_admin/{id}/	|
|	14.	|	Destroy an event for user authenticated via its id	|	DELETE	|	/api/events_admin/{id}/	|
|	15.	|	Send a message	|	POST	|	/api/contact/	|


**Setup and execution of the project**

1- Installation:
- Clone this repository with the command: `$ git clone https://github.com/C22660/blog_passion.git`
- From a terminal at the root of the repository blog_passion with the command `$ cd blog_passion`
- If you don't have pipenv, you can install it with pip or pipx on unix/macOS `$ python3 -m pip install pipenv` and for windows ou `$ pip install --user pipenv`.
- Installing packages with  `$ pipenv install` for windows or Mac os/linux.
- Activate the environment with `$ pipenv shell`

2- When the installation is done:
- Apply the migrations in the data base:
from the terminal > `$ python manage.py migrate`
- Creating an admin user:
from the terminal > `$ python manage.py createsuperuser` and enter Username, Email, and password

3- Start the development server:
from the terminal > `$ python manage.py runserver`

4- Now, open a web browser and go to “/admin/” on your local domain – e.g., http://127.0.0.1:8000/admin/.

5- Go to your local domain – e.g., http://127.0.0.1:8000/admin/ follow by the endpoint to access to the API.

6- API documentation via local domain – e.g., http://127.0.0.1:8000/swagger/

## Technologies to date
Python 3.1  
Main package added : Django 5.0.7, djangorestframework 3.15.2 ; djangorestframework-simplejwt 5.3.1 ; drf-yasg 1.21.7
Front-end : Tailwind CSS via CDN,  Alpine JS via CDN

## Author
Cédric M
