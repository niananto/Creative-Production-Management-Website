# Django setup
- install python virtual environment
  ```bash
    pip install virtualenv
  ```
- create a virtual environment
  ```bash
    virtualenv ENV
  ```
- activate the virtual environment
  ```bash
    ENV\Scripts\activate
  ```
- install dependencies
  ```bash
    pip install --upgrade pip
    pip install -r requirements.txt
  ```
- run the server
  ```bash
    python manage.py runserver
  ```
- create a superuser (this is required to access the admin panel)
  ```bash
    python manage.py createsuperuser
  ```