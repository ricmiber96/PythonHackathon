from telegram.ext import Updater, CommandHandler


def main():
    #Instanciar updater"""
    #updater = Update(token=open("./bot_token").read(), use_context=True)
    updater = Updater(token="1238512296:AAG_DBXQbmYoCGYP2LazBiRWF2ZH-RIi9W0",use_context=True)
    
    #Añadiendo un manejador al comando /start
    updater.dispatcher.add_handler(CommandHandler("start", start))
    
    #Añadiendo un manejador al comando /repite
    updater.dispatcher.add_handler(CommandHandler("repite", repite))
    
    #Añadiendo un manejador al comando /sumar
    updater.dispatcher.add_handler(CommandHandler("suma", suma))
    
    #Preguntar constantemente por notificaciones"""
    updater.start_polling()
    #Liberar recursos de memoria si cerramos el bot"""
    updater.idle()


def start(update, context):
    update.message.reply_text("Hola soy un bot")
    pass


def repite(update,context):
    update.message.reply_text(update.message.text)


def suma(update,context):
    resultado = int(context.args[0]) + int(context.args[1])
    resultado = str(resultado)
    update.message.reply_text("El resultado es: "+ resultado)

main()