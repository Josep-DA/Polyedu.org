const chatlog = document.getElementById('chatlog');
const choicesContainer = document.getElementById('choicesContainer');

// Define the decision tree
const decisionTree = {
  text: "Débuter",
  response: "Souhaites-tu faire partie d'un programme nécessitant des maths avancées?",
  options: [
    {
      text: "Oui",
      response: "Préfères-tu des maths plus concrets et techniques ou abstraits et scientifiques?",
      options: [
        {
          text: "Abstrait et scientifique",
          response: "Les mathématiques Sciences Naturelles (SN) sont plus recommendés pour ton cheminement."
        },
        {
          text: "Concret et technique",
          response: "Les mathématiques Tecnico Sciences (TS) sont plus recommendés pour ton cheminement."
        }
      ]
    },
    {
      text: "Non",
      response: "Les mathématiques Culture, société et technique (CST) sont plus recommendés pour ton cheminement."
    }
  ]
};

// Display options to the user
function displayOptions(options) {
  choicesContainer.innerHTML = '';

  options.forEach((option, index) => {
    const button = document.createElement('button');
    button.textContent = option.text;
    button.addEventListener('click', () => handleOptionSelection(option));
    choicesContainer.appendChild(button);
  });
}

// Handle option selection
function handleOptionSelection(option) {
  displayMessage('user', option.text);
  displayMessage('chatbot', option.response);

  if (option.options && option.options.length > 0) {
    displayOptions(option.options);
  } else {
    displayOptions([]);
  }
}

// Display chat messages
function displayMessage(sender, message) {
  const messageElement = document.createElement('div');
  messageElement.className = sender;
  messageElement.textContent = message;
  chatlog.appendChild(messageElement);
  chatlog.scrollTop = chatlog.scrollHeight;
}

// Initialize the chat
function initializeChat() {
  displayMessage('chatbot', "Bonjour! Cette ressource interne est un outil d'exploration de carrière pouvant vous aider à savoir quels programmes choisir au secondaire et au collégial :");
  displayOptions([decisionTree]);
}

// Start the chat
initializeChat();
