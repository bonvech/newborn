import telebot
import config
import time
from datetime import datetime
import socket


global logfilename


##  ----------------------------------------------------------------
## Write to log file with time
##  ----------------------------------------------------------------
def write_log(text):
    # get time
    timenow = datetime.now()
    timenow = str(timenow)
    text = timenow + ": " + text 

    # write to logfile
    logfilename = "newborn.log"
    flog = open(logfilename, 'a') 
    flog.write(text + '\n')
    flog.close()
    print(text)
    

def write_bot(text):
    try:
        bot = telebot.TeleBot(config.token, parse_mode=None)
        bot.send_message(config.channel, text)
    except Exception as err:
        ##  напечатать строку ошибки
        text = f": ERROR in writing to bot: {err}"
        write_log(text)  ## write to log file

 
def get_local_ip():
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    return hostname, local_ip



if __name__ == "__main__":
    
    time.sleep(600) # Сон в 10 минут
    
    hostname, local_ip = get_local_ip()
    text = f"Компьютер {hostname} ({local_ip}) перезагружен!"
    write_log(text)
    write_bot(text)
	