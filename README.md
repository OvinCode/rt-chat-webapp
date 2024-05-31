## Setup

#### - Create Virtual Environment
###### # Mac
```
python3 -m venv venv
source venv/bin/activate
```

###### # Windows
```
pip install virtualenv 
virtualenv venv 
venv\Scripts\activate.bat 
```

<br>

#### - Install dependencies
```
pip install --upgrade pip
pip install -r requirements.txt
```

<br>

#### - Migrate to database
```
python manage.py migrate
python manage.py createsuperuser
```

<br>

#### - Run application
```
python manage.py runserver
```

<br>

#### - Get Secret Key ( ! Important for deployment ! )
```
python manage.py shell
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
exit()
```

** This APP is for Education and Practise Purpose Only **

![RT_chatDemo](https://github.com/OvinCode/rt-chat-webapp/assets/86512052/c9c959f7-ed2a-47b1-a5e6-9db0c54f4dd8)

