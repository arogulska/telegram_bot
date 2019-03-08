from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
#import library, then define function
import logging
import settings

logging.basicConfig(format = '%(asctime)s - %(levelname)s - %(message)s', 
                    level = logging.INFO, 
                    filename = 'bot.log'
                    )

def greet_user(bot, update):
    text = "bot started"
    print (text)
    update.message.reply_text(text)

#def talk_to_me(bot, update):
    user_text = update.message.text
    print (update.message)
    update.message.reply_text(user_text)
#bot replies with the same text that user entered

def talk_to_me(bot, update):
    user_text = "Hi {}! You wrote: {}".format(update.message.chat.first_name, update.message.text)
    logging.info("User: %s, Chat id: %s, Message: %s", update.message.chat.username, 
                update.message.chat.id, update.message.text)
    update.message.reply_text(user_text)

def main():
    mybot = Updater(settings.API_KEY)
    #a variable with token to access the Telegram bot API (from BotFather)
    
    logging.info("Bot is starting")

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))


    mybot.start_polling()
    #start goint to Telegram and checking new messages
    mybot.idle()
    #bot will be working infinitely
     
#and run the defined function:
main()


