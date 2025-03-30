import telebot
import random

bot = telebot.TeleBot("7723644745:AAGITtudzBOYKKo5-FY9qTLJsqZp7QACQqk")

# خوندن لیست کلمات از فایل
with open("words.txt", "r") as file:
    bip39_words = file.read().splitlines()

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "سلام! من یه رباتم که عبارت 12 کلمه‌ای تولید می‌کنم. /generate رو بزن!")

@bot.message_handler(commands=['generate'])
def generate_seed(message):
    seed = " ".join(random.sample(bip39_words, 12))
    bot.reply_to(message, f"عبارت 12 کلمه‌ای:\n{seed}")

bot.polling()