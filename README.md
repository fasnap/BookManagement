# **BOOK MANAGEMENT SYSTEM**
Book Management System is a web application built with Django, allowing users to manage a collection of books. It provides a simple and intuitive interface for adding, updating, and deleting books. User authentication is implemented to secure the application.

####  PREREQUISITES
Before you begin, ensure you have the following installed:

- Create a Virtual Environment:
	- python -m venv env_name
- Activate the virtual environment:
	- On Windows: venv\Scripts\activate
	- On macOS and Linux: source venv/bin/activate
- Install Django:
	- pip install django
- Install Django REST Framework:
	- pip install djangorestframework
- Install Django REST Framework Simple JWT:
	- pip install djangorestframework-simplejwt

Include 'rest_framework' and 'rest_framework_simplejwt' in installed apps in settings.py.

#### **GETTING STARTED**
- Apply Migrations:
	- python manage.py migrate
- Create a Superuser (Optional):
	- python manage.py createsuperuser
- Run the Development Server:
	- python manage.py runserver
	
Access the application at http://localhost:8000/.

#### **AUTHENTICATION**
To access the API endpoints, you need to obtain a JSON Web Token (JWT) by sending a POST request to /api/token/ with your username and password. Include the obtained token in the Authorization header of your requests using the format: Authorization: Bearer (your_access_token_here).

**OBTAIN JWT TOKEN**
Example Authentication Request (Postman):
	- Open Postman.
	- Select POST as the HTTP method.
	- Enter the URL: http://localhost:8000/api/token/
	- Set Content-Type to application/json.
	- In the Body tab, select raw and enter your JSON payload:

	{
   	  "username": "your_username",
  	   "password": "your_password"
	 }
Click Send.
In the response, copy the access token.
Example Response:

	{
    "access": "your_access_token",
    "refresh": "your_refresh_token"
	}
**API ENDPOINTS**
- List Books:
Endpoint: GET /api/books/
Description: Get a list of all books.
Example Request (Postman):
		- Set GET as the HTTP method.
		- Enter the URL: http://localhost:8000/api/books/
		- Add Authorization header with the value Bearer your_access_token.
		- Click Send.
- Retrieve Book
 Endpoint: GET /api/books/<id>/
Description: Get details of a specific book by its ID.
Example Request (Postman):
		- Set GET as the HTTP method.
		- Enter the URL: http://localhost:8000/api/books/<id>/
		- Add Authorization header with the value Bearer your_access_token.
		- Click Send.
- Create Book
Endpoint: POST /api/books/
 Description: Add a new book.
Example Request (Postman):
		- Set POST as the HTTP method.
		- Enter the URL: http://localhost:8000/api/books/
		- Add Authorization header with the value Bearer your_access_token.
		- Set Content-Type to application/json.
		- In the Body tab, select raw and enter your JSON payload for the new book.
		- Click Send.
- Update Book
 Endpoint: PUT /api/books/<id>/
Description: Update an existing book by its ID.
 Example Request (Postman):
		- Set PUT as the HTTP method.
		- Enter the URL: http://localhost:8000/api/books/<id>/
		- Add Authorization header with the value Bearer your_access_token.
		- Set Content-Type to application/json.
		- In the Body tab, select raw and enter your JSON payload with the 	--updated book details.
		- Click Send.
- Delete Book
Endpoint: DELETE /api/books/<id>/
 Description: Delete a book by its ID.
 Example Request (Postman):
		- Set DELETE as the HTTP method.
		- Enter the URL: http://localhost:8000/api/books/<id>/
		- Add Authorization header with the value Bearer your_access_token.
		- Click Send.

**Thank you for using Book Management System!** 📚✨
