import requests

class Messanger:
    def __init__(self,config):
        self.config = config

    def transact(self, action, data = None, chat = None):
        url = f'https://api.telegram.org/bot{self.config["bot"]["TOKEN"]}/{action}'
        if data == None:
            data = {}
        if chat is not None:
            data["chat_id"] = chat
        return requests.post(url, json=data)
    
    def reply_message(self, message, text):
        reply_parameters = {"message_id": message["message_id"], 
                            "chat_id": message["chat"]["id"], 
                            "quote": message["text"][:10], 
                            "allow_sending_without_reply": False
                            }
        data = {"text": text, 
                "parse_mode": "HTML", 
                "reply_parameters": reply_parameters
                }
        return self.transact("sendMessage", data = data, chat = message["chat"]["id"])
    

