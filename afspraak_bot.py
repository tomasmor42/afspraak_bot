import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

from get_data import get_data

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print("Start")
    await update.message.reply_text("Hi! We'll send you a message when there is an afspraak")

async def set_reminder(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print("Reminder is set")
    chat_id = update.effective_message.chat_id
    context.job_queue.run_repeating(reminder, 900, chat_id=chat_id)
 
async def reminder(context: ContextTypes.DEFAULT_TYPE) -> None:
    job = context.job
    print("Reminder has started")
    city = get_data()
    if city:
        await context.bot.send_message(job.chat_id, text=f"Alarm! there is a spot in {city}")


def main() -> None:
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler(["start"], start))
    application.add_handler(CommandHandler("set", set_reminder))
    application.run_polling()


if __name__ == "__main__":
    main()