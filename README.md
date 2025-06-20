# Django Telegram Bot

This is a Django-based backend assignment demonstrating API development, authentication, Celery task queue integration, and Telegram bot integration.

---

## 🚀 Features
- Django REST Framework (DRF)
- Token Authentication
- Celery with Redis
- Telegram Bot integration
- Code management best practices

---

## 🔧 Setup Instructions

1. **Clone the Repository**

```bash
git clone https://github.com/<Srivalli13204>/<Django-Telegram-Bot>.git
cd <Django-Telegram-Bot>
```

2. **Create a Virtual Environment**

```bash
python -m venv Django
Django\Scripts\activate
```

3. **Install Dependencies**

```bash
pip install -r requirements.txt
```

4. **Apply migrations**

```bash
python manage.py make migrations
python manage.py migrate
```

5. **Run Development Server**

```bash
python manage.py runserver
```

---

## 🔐 Environment Variables

Create a .env file with the following:

```bash
SECRET_KEY=your_django_secret_key
DEBUG=False
DATABASE_URL=your_db_url
REDIS_URL=redis://localhost:6379
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
```

---

## 🔌 How to Run Locally

1. Start Redis Server:

```bash
redis-server
```

2. Run Celery worker:

```bash
celery -A config worker --loglevel=info --pool=solo
```

3. Start Django Server:

```bash
python manage.py runserver
```

---

## 📮 API Endpoints

| Method | Endpoint        | Access     | Description                  |
| ------ | --------------- | ---------- | ---------------------------- |
| GET    | `/api/public/`  | Public     | Public test endpoint         |
| GET    | `/api/private/` | Token Only | Authenticated access only    |
| POST   | `/api/login/`   | Public     | Login with username/password |

---

## 🤖 Telegram Bot

- Start your bot by messaging /start
- The bot collects your Telegram username
- Data is saved to the TelegramUser model

## 📧 Email ( Celery )
- When a user registers, a welcome email is sent via Celery
- Make sure your email credentials are set in .env

---

## ✅ Tech Stack
- Python
- Django
- Django REST Framework
- Celery + Redis
- Telegram Bot API

---

## 📂 Folder Structure
django-project/

├── core/                  # Your app

├── telegram_bot.py        # Bot logic

├── manage.py

├── .env.example

├── requirements.txt

└── README.md

---

## 👤 Author
- Developed by Pichika Parimala Durga Srivalli as part of an assignment.
