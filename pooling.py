import requests
import json

class pooling:
    def __init__(self, config):
        self.config = config
        self.offset = 0

    def run(self):
        while True:
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
        if update["ok"]:
            for message in update["result"]:
                if self.offset <= message["update_id"]:
                    self.offset = message["update_id"] + 1
                    if "message" in message and "text" in message['message']:
                        print(f'Получил сообщение!, id: {message["update_id"]}')
                        print(f'Получил сообщение!, id: {message["update_id"]}, text: {message["message"]["text"]}')

    

