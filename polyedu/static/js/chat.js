// chat.js
document.addEventListener('DOMContentLoaded', function() {
    const roomName = 'my_room'; // Replace with your chat room name

    const messageContainer = document.getElementById('message-container');
    const messageForm = document.getElementById('message-form');
    const messageInput = document.getElementById('message-input');

    // Establish WebSocket connection

    const socket = new WebSocket(`ws://${window.location.host}/ws/chat/${roomName}/`);

// Rest of your WebSocket code...
const chatSocket = new WebSocket(`ws://${window.location.host}/ws/chat/${roomName}/`);


    // Event listener for WebSocket connection open
    socket.onopen = function(event) {
        console.log('WebSocket connection opened');
    };

    // Event listener for WebSocket message received
    socket.onmessage = function(event) {
        const message = JSON.parse(event.data);
        displayMessage(message);
    };

    // Event listener for WebSocket connection closed
    socket.onclose = function(event) {
        console.log('WebSocket connection closed');
    };

    // Event listener for message form submission
    messageForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const message = messageInput.value;
        sendMessage(message);
        messageInput.value = '';
    });

    // Function to send a message via WebSocket
    function sendMessage(message) {
        const data = {
            'message': message
        };
        socket.send(JSON.stringify(data));
    }

    // Function to display a message in the chat interface
    function displayMessage(message) {
        const messageElement = document.createElement('div');
        messageElement.innerText = message;
        messageContainer.appendChild(messageElement);
    }
});
