import os
import django
import asyncio

from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    CommandHandler,
)
from asgiref.sync import sync_to_async

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from core.models import TelegramUser

@sync_to_async
def save_user(user_data):
    user, created = TelegramUser.objects.get_or_create(
        telegram_id=user_data["id"],
        defaults={
            "username": user_data.get("username"),
            "first_name": user_data.get("first_name"),
            "last_name": user_data.get("last_name"),
        }
    )
    return user, created

@sync_to_async
def get_user(telegram_id):
    return TelegramUser.objects.filter(telegram_id=telegram_id).first()


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    data = {
        "id": user.id,
        "username": user.username,
        "first_name": user.first_name,
        "last_name": user.last_name,
    }
    user_obj, created = await save_user(data)

    if created:
        await update.message.reply_text(f"👋 Hello {user.first_name}, you are now registered!")
    else:
        await update.message.reply_text(f"👋 Welcome back {user.first_name}!")


async def profile(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = await get_user(update.effective_user.id)
    if user:
        await update.message.reply_text(
            f"🧾 Your Profile:\n"
            f"ID: {user.telegram_id}\n"
            f"Name: {user.first_name or ''} {user.last_name or ''}\n"
            f"Username: @{user.username if user.username else 'N/A'}"
        )
    else:
        await update.message.reply_text("❌ You are not registered. Use /start.")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📌 Available commands:\n"
        "/start - Register yourself\n"
        "/profile - Show your Telegram user info\n"
        "/help - Show this help message"
    )

async def main():
    bot_token = "REPLACE WITH YOUR BOT TOKEN"
    app = ApplicationBuilder().token(bot_token).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("profile", profile))
    app.add_handler(CommandHandler("help", help_command))

    print("✅ Bot is running...")
    await app.run_polling()

if __name__ == "__main__":
    import sys
    import nest_asyncio
    import asyncio

    if sys.platform.startswith('win'):
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    nest_asyncio.apply()
    asyncio.get_event_loop().run_until_complete(main())
