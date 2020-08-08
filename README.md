# Django Portfolio App

This a portfolio project using Django, MySql database and Bootstrap for styling

It is still under active development.

## Setup
1.Clone the project or download as zip

2.change into folder `cd django-portfolio`

3.Create a virtual environment `python -m venv env`

4.Activate the virtual environment `source activate`

5.create a .env file using the example provided and add a secret key entry. `cp .env.example .env `
example `SECRET_KEY=supersecretkey`


OR

manually edit the settings.py file and add the secret key(don't commit this to a public repo) 

6.Add your mysql credentials under Databases in `.env` file
Alternatively use a sqlite databases by changing the database driver in `settings.py`

7.Run the database migrations `python manage.py makemigrations` 
`python manage.py migrate `

8.Run the project `python manage.py runserver`

9.To enable the password reset function enter your mailgun[mailgun.com] credentials in the `.env` file 

10.Open a browser and go to localhost:8000/projects

