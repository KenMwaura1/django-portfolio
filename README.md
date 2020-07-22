# Django Portfolio App

This a portfolio project using Django, MySql database and Bootstrap for styling

It is still under active development.

## Setup
1.Clone the project or download as zip

2.change into folder `cd django-portfolio`

3.Create a virtual environment `python -m venv env`

4.Activate the virtual environment `source activate`

5.create a .env file and add a secreat key entry. `touch .env `
example `SECRET_KEY = 'supersecretkey`

OR

manually edit the settings.py file and add the secret key(don't commit this to a public repo) 

6.Add your mysql credentials under Databases in `settings.py`
Alternatively use a sqlite databases by changing the database driver

7.Run the database migrations `python manage.py makemigrations` 
`python manage.py migrate `

8.Run the project `python manage.py runserver`

9.Open a browser and go to localhost:8000/projects

