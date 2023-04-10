from typing import Final

# pip install python-telegram-bot
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import tracemalloc
import random 
import os

tracemalloc.start()

# Ruta de la carpeta donde tienes las imágenes
ruta_carpeta_imagenes = 'C:\\Users\\Francisco\\Desktop\\TelegramBOT\\Images\\liellas'

print('Preparando a la besto liella...')

TOKEN: Final = '5904726995:AAE-a-4RX0rGm05650GC1qSzRfCHSY8xPD4'
BOT_USERNAME: Final = '@your_bot_user'


# Lets us use the /start command
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Natsumi Onitsuka conectada y lista para traer el mejor contenido!')


# Lets us use the /help command
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Quieres decirme algo? No seas timido!')


# Lets us use the /custom command
async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Este es un comando personalizable.')
    
    
async def enviar_love_live_command(update, context: ContextTypes.DEFAULT_TYPE): 
     # Obtiene una lista de todas las imágenes en la carpeta
    lista_imagenes = os.listdir(ruta_carpeta_imagenes)
    # Selecciona una imagen al azar de la lista
    imagen_aleatoria = random.choice(lista_imagenes)
    # Envía la imagen al chat de Telegram
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(ruta_carpeta_imagenes + '/' + imagen_aleatoria, 'rb'))


def handle_response(text: str) -> str:
    # Create your own response logic
    processed: str = text.lower()

    if 'hola' in processed:
        return 'Tu Natsuestrella favorita esta aqui!'

    if 'como estas?' in processed:
        return 'Muy bien, gracias por preguntar.'

    if 'me gusta python' in processed:
        return 'A mi tambien me gusta Paychan, pero no se lo digas a Sumire!'
    
    if 'cual es la mejor liella?' in processed:
        return 'Obviamente su servidora, pero no puedo decir eso al public... digo todas tienen lo suyo'
    
    if 'hentai' in processed:
        return 'Lo siento Natsumi no puede hablar de eso. Mi creador me impide mandar ese tipo de contenido. Busquese otra pervertido.'

    return 'No entiendo :c...'


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Get basic info of the incoming message
    message_type: str = update.message.chat.type
    text: str = update.message.text

    # Print a log for debugging
    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

    # React to group messages only if users mention the bot directly
    if message_type == 'group':
        # Replace with your bot username
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return  # We don't want the bot respond if it's not mentioned in the group
    else:
        response: str = handle_response(text)

    # Reply normal if the message is in private
    print('Bot:', response)
    await update.message.reply_text(response)


# Log errors
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')


# Run the program
if __name__ == '__main__':
    app = Application.builder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))
    app.add_handler(CommandHandler('enviarlovelive', enviar_love_live_command))

    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Log all errors
    app.add_error_handler(error)

    print('Polling...')
    # Run the bot
    app.run_polling(poll_interval=5)
    
    

    

    
    
        




