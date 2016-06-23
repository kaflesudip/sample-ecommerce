Installing and Testing Locally
==============================

1. Create a new virtualenv under Python 3.
2. Clone this repository into your local computer.
3. Activate the virtualenv.
4. Run `pip install -r requirements/local.txt`
5. Make sure that you have created a postgresql database for this project
6. Edit `env.example` file with you database credentials and save it as `.env`.
7. Migrate your database using `python manage.py migate`
8. Load the fixtures (i.e. Data I have copied obtained using script from Magento.)
	- ` python manage.py loaddata ecommerce/apps/catalogue/fixtures/fixtures.json`
	- `python manage.py loaddata ecommerce/users/fixtures/user_fixtures.json`
9. Run the server using `python manage.py runserver`
10. Create superuser using `python manage.py createsuperuser` and then you can login to `/admin/` page to add products, update them.

This project is created using [Django Cookiecutter](https://github.com/pydanny/cookiecutter-django) template. Refer to its documentation on more infomation on setting up environment, running locally and on production.
