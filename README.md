# La Biblioteca

A library app created with Python/Django

This project was created by @ecarlos09 and @roselynle as our first attempt to create a Django app

## Installation and usage
To run the code:
1. Fork and clone this repo
2. cd into repo
3. Create a .env file in the root directory and add the following into the file SECRET_KEY = "XYZ", where XYZ can be any string containing a mixture of numbers, letters, and symbols
4. Install requirements (optional)
   - `pipenv install -r requirements.txt`
5. Activate your virtual environment
   - `pipenv shell`
6. Run the following scripts to for different purposes
   - Run server: `pipenv run dev` or `cd borrowers` then `python manage.py runserver` 
   - Run all tests: `pipenv run test` or `cd borrowers` then `python manage.py test borrowers`
   - Run individual app tests:
      - Library: `pipenv run testlib` or `cd borrowers` then `python manage.py testlib`
      - Users: `pipenv run testusers` or `cd borrowers` then `python manage.py testusers`
   - Run coverage:
      - Initialise: `pipenv run initcov`
      - View report: `pipenv run viewcov`
7. See the app in action at
   - `http://localhost:8000/`

## Task Requiements
1. Getting Started
   - [x] Create a Django project with one app, 'library'
   - [x] Add generic custom 404 for page not found
   - [x] Add views and templates for a home and books show page (`/` and `/books/<id>`)
   - [x] The home page will list all the book titles
      - [x] We have decided to display our books list on a separate page (which requires authentication)
   - [x] The show page will list the chosen book title and author
   - [x] Show a custom 404 if book is not found
   - [x] Use dummy data for now:
      - [x] We skipped this step!
```python
[
    { 'id': 1, 'title': 'Life, the Universe and Everything', 'author': 'Douglas Adams'},
    { 'id': 2, 'title': 'The Meaning of Liff' 'author': 'Douglas Adams'},
    { 'id': 3, 'title': 'The No. 1 Ladies\' Detective Agency' 'author': 'Alexander McCall Smith'}
]
```

2. Add database and models
   - [x] Setup a 'library' database (your choice of db) 
   - [x] Create models for Book and Author
     - [x] Authors have a name
     - [x] Books have a title and a Foreign Key for author
   - [x] Make and run migrations
   - [x] Add your models to your admin dashboard and create some records in the GUI
   - [x] Update your views to take data from the database instead of the dummy data list

3. Add User authentication
   - [x] Create register, login and logout routes
   - [x] Use the UserCreationForm to complete your templates
   - [x] Register some new users via your registration form
   - [x] Make the book show route only available to logged in users
   - [x] Add a new field of 'borrower' to the Book model as a Foreign Key to User
   - [x] In your admin dashboard, assign some books a borrower
   - [x] Update your book show template to show if it is available to loan or not
  
4. Add UI forms
   - [x] Create a new book form accessible at `books/new`
   - [x] On success, the form redirects to the new book's show page
   - [x] Create a button on the book show page
   - [x] If the book is available, on clicking the button, the current User becomes the borrower of that book
   - [x] If the book is on loan by another User, current User sees disabled button
   - [x] If the book is on loan by the current User, on clicking the button, the book is returned

## Wins & Challenges

### Wins


### Challenges


## Bugs

