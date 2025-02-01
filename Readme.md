# FAQ Management System


A robust **FAQ Management System** built using **Django**, **Django REST Framework**, **Redis**, and **CKEditor** for rich text editing. This system allows you to manage FAQs with multilingual support for Hindi (hi) and Bengali (bn), with dynamic translation capabilities for unsupported languages using Google Translate API. It comes with a fully functional REST API for easy integration, caching for performance, and an intuitive admin interface for ease of use.


## Features

✨ **Multilingual Support**  
- FAQs are translatable into **Hindi** (hi) and **Bengali** (bn).  
- If the requested language isn't supported, FAQs are dynamically translated using the **Google Translate API**.

✍️ **WYSIWYG Editor**  
- Rich text editing for FAQ answers using **django-ckeditor**.

⚡ **Caching with Redis**  
- Redis caching ensures faster responses for frequently accessed FAQs.

🔗 **REST API**  
- Complete API for managing FAQs:  
  - List, create, update, retrieve, and delete FAQs.

🌐 **Dynamic Translation**  
- Unsupported languages automatically translated via Google Translate.

🖥️ **Admin Interface**  
- Simple and user-friendly admin panel to manage FAQs.

---

## Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.9 or higher**
- **Redis** (for caching)
- **A modern web browser**
- **Git** (optional, for cloning the repository)

---

## Installation

### Step 1: Clone the Repository
Clone the project repository to your local machine:

```
git clone https://github.com/AneeshRijhwani25/Multilingual-FAQs.git
cd Multilingual-FAQs
```

### Step 2: Set Up a Virtual Environment
Create and activate a virtual environment to isolate dependencies:

```
python -m venv venv
venv\Scripts\activate
```

### Step 3: Install Dependencies
Install all required dependencies from `requirements.txt`:

```
pip install -r requirements.txt
```

### Step 4: Configure Environment Variables
Create a `.env` file in the project root directory and add the following variables:

```
SECRET_KEY=your-secret-key-here
REDIS_URL=redis://127.0.0.1:6379/1
```

**Note**: Replace `your-secret-key-here` with a secure secret key.

### Step 5: Run Migrations
Apply database migrations to set up the database schema:

```
python manage.py makemigrations
python manage.py migrate
```

### Step 6: Start Redis Server
Start the Redis server for caching:

```
redis-server
```

If Redis is not installed, download and install it from [here](https://redis.io/download).

### Step 7: Run the Development Server
Start the Django development server:

```
python manage.py runserver
```

The application will be accessible at `http://localhost:8000/`.


## API Usage

### List FAQs
Retrieve a list of FAQs with optional language selection:

```
GET /api/faqs/?lang=en
```

Example Response:

```
[
  {
    "id": 1,
    "question": "What is your name?",
    "answer": "<p>My name is Aneesh.</p>"
  },
  {
    "id": 2,
    "question": "How old are you?",
    "answer": "<p>I am 23 years old.</p>"
  }
]
```

### Create a New FAQ
Add a new FAQ:

```
POST /api/faqs/
Content-Type: application/json

{
  "question": "What is your favorite color?",
  "answer": "<p>My favorite color is blue.</p>"
}
```

Response:

```
{
  "id": 3,
  "question": "What is your favorite color?",
  "answer": "<p>My favorite color is blue.</p>"
}
```

### Retrieve a Single FAQ
Get a single FAQ with optional language translation:

```
GET /api/faqs/1/?lang=hi
```

Example Response:

```
{
  "id": 1,
  "question": "आपका नाम क्या है?",
  "answer": "<p>मेरा नाम अनीश है।</p>"
}
```

### Update an FAQ
Update an existing FAQ:

```
PUT /api/faqs/1/
Content-Type: application/json

{
  "question": "Updated question?",
  "answer": "<p>Updated answer.</p>"
}
```

Response:

```
{
  "id": 1,
  "question": "Updated question?",
  "answer": "<p>Updated answer.</p>"
}
```

### Delete an FAQ
Delete an FAQ:

```
DELETE /api/faqs/1/
```

Response:

Status Code: **204 No Content**


## Admin Panel

Access the admin panel to manage FAQs:

1. **Create a superuser**:

```
python manage.py createsuperuser
```

2. **Log in** to the admin site at [http://localhost:8000/admin/](http://localhost:8000/admin/).


## Testing

Run unit tests to ensure everything works as expected:

```
pytest
```




