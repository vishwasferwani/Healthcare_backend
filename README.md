
# Healthcare Backend (Django - DRF - JWT)
This project fulfills all assignment requirements using Django, Django REST Framework, and PostgreSQL. It features JWT authentication, fully structured RESTful CRUD APIs, robust data validation, and comprehensive testing support with Postman.

#### Tech Stack
- Django  
- Django REST Framework  
- SimpleJWT  
- PostgreSQL

#### project structure
- ```healthcare_backend/accounts``` for custom user model and auth
- ```healthcare_backend/patients``` for patient CRUD
- ```healthcare_backend/doctors``` for doctor CRUD
- ```healthcare_backend/mappings``` for patient‑doctor mappings

### Environment Setup
 Create a ```.env``` file in the project root(You can copy ```.env```)

 ``` cp .env .env ```

Update value in .env
```
SECRET_KEY=Any random string
DEBUG=True
DB_NAME=healthcare_db
DB_USER=postgres
DB_PASSWORD= YOUR_PASSWORD
DB_HOST=localhost
DB_PORT=5432
```

## Setup Process

``` clone Repository 
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
Configure PostgreSQL
cd healtchcare_backend
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

#### Server URL
``` http://127.0.0.1:8000/ ```

#### Json format for login
```
{
  "email": "JohnDoe@gmail.com",
  "password": "12345"
}
```

#### Login response
```
{
  "access": "your_access_token",
  "refresh": "your_refresh_token"
}
```

### authentication: (JWT) 
```api/auth/login/``` returns access and refresh tokens. Use the access token on every protected request

#### Copy the access value from the response, then set the environment variable token.
Use this header for all protected (Auth Required) requests
``` Header: Authorization: Bearer {{token}} ```



## API Endpoints

#### Auth APIs


| Method | Endpoints   | Description                |
| :-------- | :------- | :------------------------- |
| `POST` | `/api/auth/register/` | Register a new user |
| `POST` | `/api/auth/login/` | Log in and get JWT tokens |

#### Patient APIs

| Method | Endpoints   | Description                |
| :-------- | :------- | :------------------------- |
| `POST` | `/api/patients/` | Create a patient **(auth required)** |
| `GET` | `/api/patients/` | List your patients **(auth required)** |
| `GET` | `/api/patients/<id>/` | Get a patient detail **(auth required)** |
| `PUT` | `/api/patients/<id>/ `| Update a patient **(auth required)** |
| `DELETE` | `	/api/patients/<id>/` | Delete a patient **(auth required)** |

#### Doctor APIs

| Method | Endpoints   | Description                |
| :-------- | :------- | :------------------------- |
| `POST` | `/api/doctors/` | Create a doctor **(auth required)** |
| `GET` | `/api/doctors/` | List doctors **(auth required)** |
| `GET` | `/api/doctors/<id>/` | Get a doctor detail **(auth required)** |
| `PUT` | `/api/doctors/<id>/ `| Update a doctor **(auth required)** |
| `DELETE` | `/api/doctors/<id>/` | Delete a doctor **(auth required)** |


#### Mappings APIs

| Method | Endpoints   | Description                |
| :-------- | :------- | :------------------------- |
| `POST` | `/api/mappings/` | Assign doctor to patient  **(auth required)** |
| `GET` | `/api/mappings/` | List all Doctor-Patient mappings **(auth required)** |
| `GET` | `/api/mappings/<patient_id>/` | List doctors for a patient  **(auth required)** |
| `DELETE` | `/api/mappings/<id>/` | Remove a mapping  **(auth required)** |


Validation & Error Handling

- Duplicate email on register returns 400.
- Invalid credentials return 400.
- Missing/invalid token returns 401.
- Deleting another user’s patient returns 403.
- Duplicate patient‑doctor mapping returns 400.
- No doctors for a patient returns 404.


## Data Models
#### USER

| Field | Type | Description |
| :-------- | :------- | :------------------------- |
| `id` | Integer | Primary key |
| `name` | CharField | User full name |
| `email` | EmailField | Unique email address used for login |
| `password` | String | Hashed password managed by Django |

#### Doctor

| Field | Type | Description |
| :-------- | :------- | :------------------------- |
| `id` | Integer | Primary key |
| `name` | CharField | Doctor full name |
| `specialization` | CharField | Medical specialization |
| `experience` | PositiveIntegerField | Years of experience |
| `phone` | CharField | Contact number (optional) |
| `email` | EmailField | Unique email address |
| `created_at` | DateTimeField | Automatically stores record creation time |

#### Patient
| Field | Type | Description |
| :-------- | :------- | :------------------------- |
| `id` | Integer | Primary key |
| `owner` | ForeignKey | Automatically Reference to authenticated user who created the patient |
| `name` | CharField | Patient full name |
| `age` | PositiveIntegerField | Patient age |
| `gender` | CharField | Gender (`Male`, `Female`, `Other`) |
| `disease` | CharField | Diagnosed disease or condition |
| `phone` | CharField | Contact number (optional) |
| `address` | TextField | Residential address (optional) |
| `created_at` | DateTimeField | Automatically stores record creation time |

#### Mappings
| Field | Type | Description |
| :-------- | :------- | :------------------------- |
| `id` | Integer | Primary key |
| `patient` | ForeignKey | Reference to assigned patient |
| `doctor` | ForeignKey | Reference to assigned doctor |
| `assigned_at` | DateTimeField | Automatically stores assignment creation time |

## Testing with Postman

A Postman collection is included to simplify API testing.

### Steps to Use
```
1. Open Postman  
2. Click Import  
3. Select the collection file - postman_collection.json:
```
Ensure the Django server is running:

```python manage.py runserver```

#### Recommended Testing Order
- Authentication - Register
 - Authentication - Login
- Copy access token from login response
- Set token variable at collection variables
- Test protected APIs:
- Patients
- Doctors 
- Mapping 

## License

This project was developed for assignment purposes.
