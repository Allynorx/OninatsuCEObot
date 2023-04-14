from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, Updater
from typing import Final
import tracemalloc
import random 
import os
import schedule
import time 
import logging

tracemalloc.start()


logging.basicConfig(
    level = logging.INFO, format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s,"
)
logger = logging.getLogger()


# Ruta de la carpeta donde tienes las imágenes
ruta_carpeta_imagenes = 'C:\\Users\\Francisco\\Desktop\\TelegramBOT\\Images\\liellas'
ruta_carpeta_akane = 'C:\\Users\\Francisco\\Desktop\\TelegramBOT\\Images\\liellas\\akane'
ruta_carpeta_emori = 'C:\\Users\\Francisco\\Desktop\\TelegramBOT\\Images\\liellas\\emori'
ruta_carpeta_liellitas = 'C:\\Users\\Francisco\\Desktop\\TelegramBOT\\Images\\liellas\\liellitas'
ruta_carpeta_liyuu = 'C:\\Users\\Francisco\\Desktop\\TelegramBOT\\Images\\liellas\\liyuu'
ruta_carpeta_nagi = 'C:\\Users\\Francisco\\Desktop\\TelegramBOT\\Images\\liellas\\nagi'
ruta_carpeta_nako = 'C:\\Users\\Francisco\\Desktop\\TelegramBOT\\Images\\liellas\\nako'
ruta_carpeta_non = 'C:\\Users\\Francisco\\Desktop\\TelegramBOT\\Images\\liellas\\non'
ruta_carpeta_kuma = 'C:\\Users\\Francisco\\Desktop\\TelegramBOT\\Images\\liellas\\kuma'
ruta_carpeta_paychan = 'C:\\Users\\Francisco\\Desktop\\TelegramBOT\\Images\\liellas\\paychan'
ruta_carpeta_sayuri = 'C:\\Users\\Francisco\\Desktop\\TelegramBOT\\Images\\liellas\\sayuri'
ruta_carpeta_yuina = 'C:\\Users\\Francisco\\Desktop\\TelegramBOT\\Images\\liellas\\yuina'

print('Preparando a la besto liella...')

TOKEN: Final = '5904726995:AAE-a-4RX0rGm05650GC1qSzRfCHSY8xPD4'
BOT_USERNAME: Final = '@your_bot_user'

updater = Updater('TOKEN', update_queue=update_queue)


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
 
def enviarNon(update, context: ContextTypes.DEFAULT_TYPE)-> str:
     # Obtiene una lista de todas las imágenes en la carpeta
    lista_imagenes = os.listdir(ruta_carpeta_non)
    # Selecciona una imagen al azar de la lista
    imagen_aleatoria = random.choice(lista_imagenes)
    # Envía la imagen al chat de Telegram
    return context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(ruta_carpeta_imagenes + '/' + imagen_aleatoria, 'rb'))

 
    
def non(update, context):
    bot = context.bot
    updateMsg = getattr(update, 'message', None)
    messageId = updateMsg.message_id #obtiene el ide del mensaje
    chatId = update.message.chat_id
    userName = update.effective_user['first_name']
    text = update.message.text #obtener el texto que envió el usuario al chat
    logger.info(f'El usuario {userName} ha enviado un nuevo mensaje al grupo {chatId}')

    liellaWord = 'non'

    if liellaWord in text:
        llamarNon = non
        chatId = update.message.chat_id
        enviarNon(update, context)
    

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
    
    if 'te quiero' in processed:
        return 'Natsumi tambien te quiere fanatico promedio c:'
    #return 'No entiendo :c... dame tiempo a que aprenda y mas adelante Natsumi podra ayudarte c:'




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

 
#Def del schedule de Chika   
def chika(update, context):
    context.job_queue.run_repeating(send_images, interval=604800, first=0)
    
    

# Log errors
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')


# Run the program
if __name__ == '__main__':
    app = Application.builder().token(TOKEN).build()
#updated se conecta y recibe los mensajes
updater = Updater(BOT_USERNAME.token, use_context = True)

    # Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))
    app.add_handler(CommandHandler('enviarlovelive', enviar_love_live_command))
    

    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))
    app.add_handler(MessageHandler(filters.TEXT, non))
    
    # Log all errors
    app.add_error_handler(error)

    print('Polling...')
    # Run the bot
    app.run_polling(poll_interval=5)
      
#Dispatcher
dp = updater.dispatcher



# Función para enviar las imágenes
async def send_images(update, context: ContextTypes.DEFAULT_TYPE):
    # Obtenemos la lista de imágenes
    images = os.listdir('images/lunesdechika')
    # Seleccionamos una imagen aleatoria
    image = random.choice(images)
    # Enviamos la imagen al chat
    chat_id = '-1001789487336'
    await context.bot.send_photo(chat_id=chat_id, photo=open(os.path.join('images/lunesdechika', image), 'rb'))

# Programamos el envío de imágenes todos los lunes a las 10:00 AM
schedule.every().wednesday.at('10:00').do(send_images)

dispatcher = updater.dispatcher
job_queue = updater.job_queue
# Mantenemos el bot en ejecución
while True:
    schedule.run_pending()
    time.sleep(1)
    
    

    

    
    
        




