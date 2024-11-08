# myapp/consumers.py

import json
from channels.generic.websocket import AsyncWebsocketConsumer

class MyConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print('web socket connect')
        await self.accept()  # 클라이언트의 연결 수락

    async def disconnect(self, close_code):
        print('web socket disconnect')
        pass  # 연결 종료 시 처리

    async def receive_json(self, text_data):
        print(text_data)
        data = json.loads(text_data)
        print(data)
        message = data['message']  # 클라이언트로부터 받은 메시지
        print(message)

        # 클라이언트에게 메시지 전송
        await self.send(text_data=json.dumps({
            'message': message
        }))
