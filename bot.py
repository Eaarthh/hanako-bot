try:
    import telebot
except ImportError as e:
    print(f"Error importando telebot: {e}")
    print("Intentando instalar pyTelegramBotAPI...")
    import os
    os.system('pip install pyTelegramBotAPI==3.8.0')
    import telebot

import random
from datetime import datetime
import time

# Token del bot
BOT_TOKEN = '7681441356:AAEHRJrZXmr6i1IHY7KNe_RW8GrhI5wF-Ow'
bot = telebot.TeleBot(BOT_TOKEN)

# Control de usos del comando ship
ship_uses = {}

# Mensajes divertidos para el comando gay
GAY_MESSAGES = {
    'alto': [
        "¡Bienvenido al club del arcoíris! 🌈",
        "¡Las puertas del pride están abiertas para ti! 🏳️‍🌈",
        "¡Eres más gay que un unicornio en una fiesta de purpurina! ✨"
    ],
    'medio': [
        "Estás en el camino del arcoíris 🌈",
        "Ni de aquí ni de allá, ¡pero con estilo! 😎",
        "¡Medio gay, medio hetero, 100% fabuloso! ✨"
    ],
    'bajo': [
        "Apenas y rozas el arcoíris 🌈",
        "Tan hetero que duele 😂",
        "¡Necesitas más purpurina en tu vida! ✨"
    ]
}

# GIFs de anime según porcentaje
GAY_GIFS = {
    'alto': [
        'https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExMjJ2YWoxOGw4ZnQyM3ZkcnE4aW5mZzh2Z2NvNnpweDI4MmR0djZxaiZlcD12MV9pbnRlcm5hbF9naWZzX2dpZklkJmN0PWc/LOcPt9gfuNOSI/giphy.gif',
        'https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExcTdwbWd4eW94NnAwOWF1NHJxdDg2M3J4ZWM4OWVnYnR2NnRvd3NpbyZlcD12MV9pbnRlcm5hbF9naWZzX2dpZklkJmN0PWc/KztT2c8u8QQQo/giphy.gif',
        'https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNmRqYWZjdmg5NWJ0M2UyaWFxcXhzY2o2bXc4YmFyMmN1cW9jN3RtdyZlcD12MV9pbnRlcm5hbF9naWZzX2dpZklkJmN0PWc/euMGLvWFJ0eKQ/giphy.gif'
    ],
    'medio': [
        'https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExeXVheGl2ZWNvN3N5enBxbzF2Zm02ZGNzOWgxbDg5dXh6bTNnbmMzciZlcD12MV9pbnRlcm5hbF9naWZzX2dpZklkJmN0PWc/FjeGBljESVAzu/giphy.gif',
        'https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOHZkdXNkNnZqZWF4dXFrYWQ0Ym5xbm9jNzFxbDh6aHcxcWh1ZTRzaCZlcD12MV9pbnRlcm5hbF9naWZzX2dpZklkJmN0PWc/SKGo6OYe24EBG/giphy.gif',
        'https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExcXcyeHM1aTYwajkyY2VlMjJlM3YyZXM1ZWsxZGlxdmh5ZzhoeXV2eCZlcD12MV9pbnRlcm5hbF9naWZzX2dpZklkJmN0PWc/5bdhq6YF0szPaCEk9Y/giphy.gif'
    ],
    'bajo': [
        'https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExMXF5Y3VkdnZxODZ1ZmsxbHNyNzFxeXhkbHJ5cXc2aHR5ZWs2dW9xdyZlcD12MV9pbnRlcm5hbF9naWZzX2dpZklkJmN0PWc/l4FGpP4lxGGf782yU/giphy.gif',
        'https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExcDRtcWwzY2JzZnBsbDMzYXZhbXM2Y2ZtcGpnbTYzcmNwdXV0cHIwcSZlcD12MV9pbnRlcm5hbF9naWZzX2dpZklkJmN0PWc/gZEBpuOkPuydi/giphy.gif',
        'https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExdWIyZzFqeXptOWM4cWIyZXZzcWt6Y3Y2aWVqbGNzNGFodGxxZnQybyZlcD12MV9pbnRlcm5hbF9naWZzX2dpZklkJmN0PWc/1gbQIeNzZxcSk/giphy.gif'
    ]
}

# GIFs para el comando ship (escenas románticas de anime)
SHIP_GIFS = [
    'https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExYnZiend6YTZlbDdxeWFqcm50NWxlYmF5YTY4ZHR2OWh3ZmJ2Y3B2eCZlcD12MV9pbnRlcm5hbF9naWZzX2dpZklkJmN0PWc/bMLGNRoAy0Yko/giphy.gif',
    'https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExdXFva2YyYnJnb3YyYmFqcnBxdG04ZmZyM3RjOHVlZTFjZzM5Nm02diZlcD12MV9pbnRlcm5hbF9naWZzX2dpZklkJmN0PWc/N0CIxD9IxAJfq/giphy.gif',
    'https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExZjJ4Y3h5bHY1MmRkdnZtbDVnZ3B6ZmVmcmJ0Z3QwN2h5NzBnYTl5ZSZlcD12MV9pbnRlcm5hbF9naWZzX2dpZklkJmN0PWc/FjxgL7lawVuWQ/giphy.gif',
    'https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExcnFlZWt5d3BwYTI1bTdteHoyY3QxOGN6NWwwdmxjcDR1NzE1dWp5aCZlcD12MV9pbnRlcm5hbF9naWZzX2dpZklkJmN0PWc/kU586ictpGb0Q/giphy.gif',
    'https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExMmh6ZDN2cWZ5MXB6bDZ1ZjhnNDQxbXlmZmFoZmZ5YXI0Ym9pM2Q1eiZlcD12MV9pbnRlcm5hbF9naWZzX2dpZklkJmN0PWc/QNFhOolVeCzPQ6q9jn/giphy.gif'
]

@bot.message_handler(commands=['start'])
def send_welcome(message):
    welcome_text = "Hola soy Hanako y soy un bot para poner un poco de fantasmasiversion al grupo.\nPara más información pon /help"
    bot.reply_to(message, welcome_text)

@bot.message_handler(commands=['help'])
def send_help(message):
    help_text = """
🌟 Comandos disponibles:

/gay - Descubre qué tan gay eres hoy 🌈
/ship - Encuentra el ship del día (3 usos diarios) 💕

¡Diviértete! 👻
    """
    bot.reply_to(message, help_text)

@bot.message_handler(commands=['gay'])
def gay_command(message):
    percentage = random.randint(0, 100)
    
    if percentage >= 70:
        level = 'alto'
    elif percentage >= 30:
        level = 'medio'
    else:
        level = 'bajo'
    
    gif = random.choice(GAY_GIFS[level])
    message_text = f"@{message.from_user.username} eres {percentage}% gay\n{random.choice(GAY_MESSAGES[level])}"
    
    try:
        bot.send_animation(message.chat.id, gif, caption=message_text)
    except Exception as e:
        print(f"Error enviando GIF: {e}")
        bot.reply_to(message, message_text)

@bot.message_handler(commands=['ship'])
def ship_command(message):
    chat_id = str(message.chat.id)
    current_date = datetime.now().date()
    
    if chat_id not in ship_uses or ship_uses[chat_id]['date'] != current_date:
        ship_uses[chat_id] = {'date': current_date, 'count': 0}
    
    if ship_uses[chat_id]['count'] >= 3:
        bot.reply_to(message, "¡Ya se usaron los 3 ships del día! Vuelve mañana 💕")
        return
    
    users = message.text.split()[1:]
    if len(users) < 2 or len(users) > 4:
        bot.reply_to(message, "¡Menciona entre 2 y 4 personas! Ejemplo: /ship @user1 @user2")
        return
    
    ship_uses[chat_id]['count'] += 1
    gif = random.choice(SHIP_GIFS)
    ship_text = f"💘 ¡Ship del día #{ship_uses[chat_id]['count']}!\n{' + '.join(users)}\n¡El amor está en el aire! 💕"
    
    try:
        bot.send_animation(message.chat.id, gif, caption=ship_text)
    except Exception as e:
        print(f"Error enviando GIF: {e}")
        bot.reply_to(message, ship_text)

print("Bot iniciado...")
bot.polling(none_stop=True)