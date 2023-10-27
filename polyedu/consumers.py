from channels.generic.websocket import AsyncWebsocketConsumer
import json

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Perform any necessary setup or validation for the connection
        # For example, you can check if the user is authenticated or authorized to access the chat

        # Accept the WebSocket connection
        await self.accept()

    async def disconnect(self, close_code):
        # Perform any cleanup or additional actions when the connection is closed
        # For example, you can remove the user from the chat room or update their status

        # Close the WebSocket connection
        await self.close()

    async def receive(self, text_data):
        # Get the message content
        content = json.loads(text_data)
        message = content['message']

        # Send the received message to all connected clients
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )


    async def send_message(self, message):
        # Send messages to WebSocket clients
        # You can define how to format and send messages to the connected clients

        # Example: Broadcast the message to all connected clients
        await self.send(text_data=json.dumps({'message': message}))

    async def chat_message(self, event):
        # Send the received message to the WebSocket
        await self.send(text_data=json.dumps({
            'message': event['message']
        }))

@property
def room_group_name(self):
    # Return the room group name based on the URL parameter
    return self.scope['url_route']['kwargs']['room_name']
