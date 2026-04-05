
import os
import logging
from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Application, ContextTypes, MessageHandler, filters, CommandHandler, CallbackQueryHandler
import components.globals as globals
import components.tokens as tokens
import components.database_byd as database_byd

#importamos el token de telegram

#telegram_token=os.getenv("TOKEN")
telegram_token=tokens.personal_token

#menu inicio con las opciones de turno

async def start_command(update,context):
    markup = ReplyKeyboardMarkup(globals.reply_keyboard, one_time_keyboard=False, resize_keyboard=True)
    #configuramos el comando start para escribir una respuesta
    await update.message.reply_text(
        globals.texto_start,
        reply_markup=markup
    )

async def help_command(update,context):
    #configuramos el comando help para escribir una respuesta
    
    await update.message.reply_text(globals.help_text)



#detecta fotos enviadas
async def photo_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('¡Gracias por la foto!')

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    markup = ReplyKeyboardMarkup(globals.reply_keyboard, one_time_keyboard=False, resize_keyboard=True)
    markup_totales = ReplyKeyboardMarkup(globals.total_keyboard, one_time_keyboard=False, resize_keyboard=True)
    
    if text == "📄 Totales" or text.lower() == "totales":
        await update.message.reply_text(globals.text_continue_help, reply_markup=markup_totales)
    elif text == "kilometros" or text.lower() == "kilometros":
        await update.message.reply_text(globals.text_km_total) 
        await update.message.reply_text(globals.text_continue_help, reply_markup=markup)
    elif text == "gasolina" or text.lower() == "gasolina":
        await update.message.reply_text(globals.text_fuel_total) 
        await update.message.reply_text(globals.text_continue_help, reply_markup=markup)
    elif text == "electricidad" or text.lower() == "electricidad":
        await update.message.reply_text(globals.text_elec_total) 
        await update.message.reply_text(globals.text_continue_help, reply_markup=markup)
    elif text == "❓ Help":
        await help_command(update, context)
    else:
        await update.message.reply_text("Lo siento, todavía no sé hacer eso. ", reply_markup=markup)

async def db_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    document = update.message.document
    
    # Comprobamos que el archivo se llame exactamente EC_Database.db
    if document.file_name == 'EC_database.db' or document.file_name == 'EC_database.jpg':
        # Nos aseguramos de que la carpeta data exista y guardamos la ruta
        os.makedirs('./data', exist_ok=True)
        if document.file_name == 'EC_database.db':
            file_path = os.path.join('./data', 'EC_database.db')
        else:
            file_path = os.path.join('./data', 'EC_database.jpg')
            os.replace(file_path, './data/EC_database.db') 
        # Obtenemos el archivo de los servidores de Telegram
        new_file = await context.bot.get_file(document.file_id)
        # Lo descargamos (reemplazará el anterior si existe)
        await new_file.download_to_drive(file_path)
        
        await update.message.reply_text(f'¡Base de datos {document.file_name} recibida, guardada y actualizada con éxito.')
    else:
        await update.message.reply_text(f'Archivo ignorado. Por favor, envía un archivo llamado exactamente "EC_Database.db" o "EC_Database.jpg". Recibido: {document.file_name}')
#
#configuramos el logging para que muestre los errores
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.WARNING)
logger = logging.getLogger(__name__)
def error_callback(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    bot = Application.builder().token(telegram_token).build()
    #funcion que responde al usuario con echo
    bot.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    bot.add_handler(CommandHandler("start", start_command))
    bot.add_handler(CommandHandler("help", help_command))
    bot.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, start_command))
    bot.add_handler(MessageHandler(filters.PHOTO, photo_handler))
    bot.add_handler(MessageHandler(filters.Document.ALL, db_handler))
    bot.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()




