import requests
import json
from bot import Bot

class pooling:
    def __init__(self, config):
        self.config = config
        self.offset = 0
        self.bot = Bot(config)
    def run(self):
        while True:
            print(f'new offset: {self.offset}')
            request_data = {"allowed_updates": self.config["bot"]["allowed_updates"], "offset": self.offset, "limit": 1}
            response = requests.post(
                url = f'http://api.telegram.org/bot{self.config["bot"]['TOKEN']}/getUpdates',
                json = request_data
            )
            if  response.status_code == 200:
                self.incoming_update(json.loads(response.text))
            else:    
                print("Error!!!")


    def incoming_update(self, update):
        print("update:")
        print(json.dumps(update))
        if update["ok"]:
            for message in update["result"]:
                if self.offset <= message["update_id"]:
                    self.offset = message["update_id"] + 1
                self.incoming_messege(message)

    def incoming_messege(self, message):
        print("message:")
        print(json.dumps(message))
        self.bot.handle(message)

    

