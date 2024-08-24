from Messanger import Messanger

class Bot:
    def __init__(self, config):
        self.messager = Messanger(config)
        self.config = config
    
    def reply_message(self, message):
        text = message.get("text")
        if text:
            self.messager.reply_message(message, f'Да да, я вас слушаю')
        
    def handle(self, message):
        if "message" in message:
            self.reply_message(message["message"])

