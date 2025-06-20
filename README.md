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

## 📸 Screenshots

### 🌐 Public API
Accessed via /api/public/ — returns a simple public message.
<img src="https://github.com/user-attachments/assets/ac8369ba-7301-4bad-8966-6cb5f3db0c20" alt="Public API" width="600"/>

### 📤 Sending Email
API endpoint to send a test email using Celery.
<img src="https://github.com/user-attachments/assets/5751ba2b-099e-4863-8c61-cb152576c262" alt="Sending Email" width="600" height="400"/>

### 🔁 Redis Server Running
Redis is set up as the Celery broker and ready to handle tasks.
<img src="https://github.com/user-attachments/assets/2dc44d13-0dcf-4e60-b1a1-18077779688f" alt="Redis server" width="600"/>

### ✅ Celery Task Success
Displays the success message after the email is queued and sent.
<img src="https://github.com/user-attachments/assets/9bf22799-9684-40d8-9006-73df4b209b0d" alt="success" width="600"/>

### ✉️ Mail Sent (Gmail Preview)
Confirms the user has received a test email.
<img src="https://github.com/user-attachments/assets/23aec2d0-0da6-47ed-9bc4-fc500ee4210d" alt="Mail sent" width="600/>

### 🤖 Telegram Bot Integration
Shows /start, /profile, and /help commands in action for user registration and info.
<img src="https://github.com/user-attachments/assets/b10fb70e-b3bf-4030-be87-87a0f2727dc4" alt="Telegram Bot" width="600"/>

---

## 👤 Author
- Developed by Pichika Parimala Durga Srivalli as part of an assignment.
