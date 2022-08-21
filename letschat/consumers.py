import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

class Consumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        #Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self,close_code):
        #Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    #Receive message from websocket
    def receive(self,text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        #send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type':'chat_message',
                'message': message
            }
        )

    #receive message from room group
    def chat_aessage(self,event):
        message = event['message']

        #send message to websocket
        self.send(text_data=json.dumps({
            'message':message
        }))