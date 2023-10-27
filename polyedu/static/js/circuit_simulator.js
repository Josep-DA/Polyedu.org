const circuitSvg = document.getElementById('circuit-diagram');
    let components = [];
    let totalResistance = 0;
    let totalReactance = 0;

    // Array to store line elements representing connections
    let connectionLines = [];

    let simulationMode = false;

    // Add event listener to the toggle button
const sidebarToggleBtn = document.getElementById('sidebar-toggle-btn');
sidebarToggleBtn.addEventListener('click', function() {
  const sidebar = document.getElementById('sidebar');
  sidebar.classList.toggle('show');
});

// Add event listener to the radio buttons
const currentRadioButtons = document.getElementsByName('current');
currentRadioButtons.forEach(function(radioButton) {
  radioButton.addEventListener('change', function() {
    updateTotalReactance();
  });
});

const simulationToggleBtn = document.getElementById('simulation-toggle-btn');
simulationToggleBtn.addEventListener('click', function() {
  toggleSimulationMode();
});

// Add draggable functionality to components using jQuery UI
components.forEach((component) => {
      $(component.symbol).draggable({
        containment: 'parent', // Restrict dragging within the parent container
        snap: '.component', // Snap to other components
        snapMode: 'outer',
        snapTolerance: 10
      });
    });


// Function to add a component to the circuit
function addComponent(type, value) {
  if (simulationMode) {
    // Simulation mode is active, do not add components
    return;
  }


  let x = 100;
  const y = 150;

  if (components.length > 0) {
    const lastComponent = components[components.length - 1];
    const lastComponentWidth = lastComponent.type === 'resistor' ? 80 : 60;
    x = parseFloat(lastComponent.symbol.getAttribute('x')) + lastComponentWidth + 20;
  } else {
    const currentType = getCurrentType();
    const currentSymbol = createCurrentSymbol(x - 60, y, currentType);
    circuitSvg.appendChild(currentSymbol);
  }

  let symbol;
  if (type === 'resistor') {
    symbol = createResistorSymbol(x , y);
  } else if (type === 'capacitor') {
    symbol = createCapacitorSymbol(x, y);
  }

  if (symbol) {
    const component = {
      type: type,
      value: value,
      symbol: symbol, // Store the symbol element
      valueText: createComponentValueText(x, y, value, getUnit(type)), // Store the value text element
      removeBtn: createRemoveButton(x, y) // Store the remove button element
    };

    components.push(component);
    updateTotalResistance();
    updateTotalReactance();
    updateNumberOfComponents();
    showEmptyCircuitMessage(false);

    // Draw connections
    drawConnectionLine(x - 40, y);
    drawConnectionLine(x + 40, y);

    // Add the symbol, value text, and remove button to the circuit diagram
    circuitSvg.appendChild(symbol);
    circuitSvg.appendChild(component.valueText);
    circuitSvg.appendChild(component.removeBtn);

    // Attach event listener to the remove button
    component.removeBtn.addEventListener('click', function () {
      removeComponent(component);
    });

    // Update the x-coordinate for subsequent components
    components.forEach((comp, index) => {
      const compX = 100 + (index * 100);
      comp.symbol.setAttribute('x', compX);
      comp.valueText.setAttribute('x', compX);
      comp.removeBtn.setAttribute('x', compX + 20);
      comp.removeBtn.style.display = simulationMode ? 'none' : 'block';
    });

    // Set the draggable attribute of the symbol element to true
    symbol.setAttribute('draggable', 'true');

    // Add the necessary event listeners for drag and drop
    symbol.addEventListener('dragstart', dragStart);
    symbol.addEventListener('dragover', dragOver);
    symbol.addEventListener('drop', drop);
  }
}

// Add draggable attribute to components
components.forEach((component) => {
  component.symbol.setAttribute('draggable', true);
});

// Event listener for dragstart event
function dragStart(event) {
  const componentIndex = getComponentIndex(event.target);
  event.dataTransfer.setData('text/plain', componentIndex);
}

// Event listener for dragover event
function dragOver(event) {
  event.preventDefault();
}

// Event listener for drop event
function drop(event) {
  event.preventDefault();

  const componentIndex = event.dataTransfer.getData('text/plain');
  const component = components[componentIndex];

  const circuitRect = circuitSvg.getBoundingClientRect();
  const x = event.clientX - circuitRect.left;
  const y = event.clientY - circuitRect.top;

  component.symbol.setAttribute('x', x);
  component.symbol.setAttribute('y', y);

  // Update the component's position in the components array
  components.splice(componentIndex, 1);
  components.push(component);

  // Update the x-coordinate for subsequent components
  components.forEach((comp, index) => {
    const compX = 100 + index * 100;
    comp.symbol.setAttribute('x', compX);
    comp.valueText.setAttribute('x', compX);
    comp.removeBtn.setAttribute('x', compX + 20);
    comp.removeBtn.style.display = simulationMode ? 'none' : 'block';
  });
}

// Helper function to get the index of a component in the components array
function getComponentIndex(componentElement) {
      const symbol = componentElement.closest('.component-symbol');
      return components.findIndex((comp) => comp.symbol === symbol);
    }

    // Add the necessary event listeners for drag and drop
    components.forEach((component) => {
      component.symbol.setAttribute('draggable', true);
      component.symbol.addEventListener('dragstart', dragStart);
      component.symbol.addEventListener('dragover', dragOver);
      component.symbol.addEventListener('drop', drop);
    });

function toggleSimulationMode() {
  simulationMode = !simulationMode;
  const removeButtons = document.getElementsByClassName('remove-button');
  for (let i = 0; i < removeButtons.length; i++) {
    removeButtons[i].style.display = simulationMode ? 'none' : 'block';
  }
}




// Function to create a DC or AC symbol based on current type
function createCurrentSymbol(x, y, currentType) {
  const symbol = document.createElementNS('http://www.w3.org/2000/svg', 'text');
  symbol.setAttribute('x', x);
  symbol.setAttribute('y', y);
  symbol.setAttribute('text-anchor', 'middle');
  symbol.setAttribute('dominant-baseline', 'middle');
  symbol.setAttribute('class', 'component-symbol');

  if (currentType === 'dc') {
    symbol.textContent = 'DC';
  } else if (currentType === 'ac') {
    symbol.textContent = 'AC';
  }

  return symbol;
}



// Function to create the remove button
function createRemoveButton(x, y) {
  const button = document.createElementNS('http://www.w3.org/2000/svg', 'text');
  button.setAttribute('x', x + 20);
  button.setAttribute('y', y + 45);
  button.setAttribute('text-anchor', 'middle');
  button.setAttribute('class', 'remove-button');
  button.textContent = 'X';
  return button;
}

// Function to remove a component from the circuit
function removeComponent(component) {
  if (simulationMode) {
    // Simulation mode is active, do not remove components
    return;
  }
  const index = components.indexOf(component);
  if (index > -1) {
    components.splice(index, 1);
    updateTotalResistance();
    updateTotalReactance();
    updateNumberOfComponents();

    circuitSvg.removeChild(component.symbol);
    circuitSvg.removeChild(component.valueText);
    circuitSvg.removeChild(component.removeBtn);

    const associatedLines = connectionLines.filter((line) => {
      const lineX1 = parseFloat(line.getAttribute('x1'));
      const lineY1 = parseFloat(line.getAttribute('y1'));
      const lineX2 = parseFloat(line.getAttribute('x2'));
      const lineY2 = parseFloat(line.getAttribute('y2'));

      return (
        (lineX1 === parseFloat(component.symbol.getAttribute('x')) - 40 && lineY1 === parseFloat(component.symbol.getAttribute('y'))) ||
        (lineX2 === parseFloat(component.symbol.getAttribute('x')) - 40 && lineY2 === parseFloat(component.symbol.getAttribute('y'))) ||
        (lineX1 === parseFloat(component.symbol.getAttribute('x')) + 40 && lineY1 === parseFloat(component.symbol.getAttribute('y'))) ||
        (lineX2 === parseFloat(component.symbol.getAttribute('x')) + 40 && lineY2 === parseFloat(component.symbol.getAttribute('y')))
      );
    });

    associatedLines.forEach((line) => {
      circuitSvg.removeChild(line);
      connectionLines.splice(connectionLines.indexOf(line), 1);
    });

    connectionLines = connectionLines.filter((line) => !associatedLines.includes(line));
  }

  if (components.length === 0) {
    showEmptyCircuitMessage(true);
  }
}

// Function to update the symbols based on the current type (DC/AC)
function updateSymbols(currentType) {
  const currentSymbol = createCurrentSymbol(40, 150, currentType);
  circuitSvg.firstChild.replaceWith(currentSymbol);

  components.forEach((component, index) => {
    const x = 100 + (index * 100);
    component.symbol.setAttribute('x', x);
    component.valueText.setAttribute('x', x);
    component.removeBtn.setAttribute('x', x + 20);
  });
}

// Add event listener to the radio buttons
currentRadioButtons.forEach(function(radioButton) {
  radioButton.addEventListener('change', function() {
    const currentType = getCurrentType();
    updateSymbols(currentType);
    updateTotalReactance();
  });
});

function createComponentValueText(x, y, value, unit) {
  const text = document.createElementNS('http://www.w3.org/2000/svg', 'text');
  text.setAttribute('x', x + 30); // Adjust the x-coordinate
  text.setAttribute('y', y + 35);
  text.setAttribute('text-anchor', 'middle');
  text.textContent = value + ' ' + unit;
  return text;
}


// Function to get the unit for component value
function getUnit(type) {
  if (type === 'resistor') {
    return 'Ω'; // Ohms
  } else if (type === 'capacitor') {
    return 'F'; // Farads
  }
  return ''; // Default empty unit
}


    // Function to draw a connection line
    function drawConnectionLine(startX, y) {
      const endX = startX + 80;
      const line = document.createElementNS('http://www.w3.org/2000/svg', 'line');
      line.setAttribute('x1', startX);
      line.setAttribute('y1', y);
      line.setAttribute('x2', endX);
      line.setAttribute('y2', y);
      line.setAttribute('class', 'connection-line');
      circuitSvg.appendChild(line);
      return line;
    }

    // Function to create a resistor symbol
    function createResistorSymbol(x, y) {
      const resistor = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
      resistor.setAttribute('x', x - 20);
      resistor.setAttribute('y',y - 20);
      resistor.setAttribute('width', 40);
      resistor.setAttribute('height', 40);
      resistor.setAttribute('class', 'component-symbol');
      return resistor;
    }

    // Function to create a capacitor symbol
    function createCapacitorSymbol(x, y) {
      const capacitor = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
      capacitor.setAttribute('cx', x);
      capacitor.setAttribute('cy', y);
      capacitor.setAttribute('r', 20);
      capacitor.setAttribute('class', 'component-symbol');
      return capacitor;
    }

    // Function to update the total resistance
    function updateTotalResistance() {
      totalResistance = components.reduce((sum, component) => {
        if (component.type === 'resistor') {
          return sum + parseFloat(component.value);
        }
        return sum;
      }, 0);
      const totalResistanceText = document.getElementById('total-resistance');
      totalResistanceText.textContent = 'Résistance totale: ' + totalResistance.toFixed(2) + ' Ω';
    }

    // Function to update the total reactance
function updateTotalReactance() {
  const frequency = parseFloat(document.getElementById('frequency-input').value);
  const currentType = getCurrentType();

  totalReactance = components.reduce((sum, component) => {
    if (component.type === 'capacitor') {
      const reactance = calculateCapacitiveReactance(component.value, frequency, currentType);
      return sum - reactance;
    }
    return sum;
  }, 0);

  const totalReactanceText = document.getElementById('total-reactance');
  totalReactanceText.textContent = 'Réactance totale: ' + totalReactance.toFixed(2) + ' Ω';
}

// Function to calculate the capacitive reactance based on current type
function calculateCapacitiveReactance(value, frequency, currentType) {
  if (currentType === 'ac') {
    const reactance = 1 / (2 * Math.PI * frequency * parseFloat(value));
    if (value.endsWith('u')) {
      // Convert microfarads (uF) to farads (F)
      return reactance * 1e-6;
    } else if (value.endsWith('n')) {
      // Convert nanofarads (nF) to farads (F)
      return reactance * 1e-9;
    } else {
      return reactance;
    }
  }
  return 0; // For DC, reactance is zero
}

// Function to get the selected current type
function getCurrentType() {
  const currentRadioButtons = document.getElementsByName('current');
  for (let i = 0; i < currentRadioButtons.length; i++) {
    if (currentRadioButtons[i].checked) {
      return currentRadioButtons[i].value;
    }
  }
  return 'dc'; // Default to DC if no selection is made
}





    // Function to update the number of components
    function updateNumberOfComponents() {
      const numberOfComponentsText = document.getElementById('number-of-components');
      numberOfComponentsText.textContent = 'Nombre de composantes: ' + components.length;
    }

    // Function to show/hide the empty circuit message
    function showEmptyCircuitMessage(show) {
      const emptyCircuitMessage = document.getElementById('empty-circuit-message');
      emptyCircuitMessage.style.display = show ? 'block' : 'none';
    }

    // Add component button click event
    const addComponentBtn = document.getElementById('add-component-btn');
    addComponentBtn.addEventListener('click', function() {
      const componentSelect = document.getElementById('component-select');
      const componentValue = document.getElementById('component-value');
      const type = componentSelect.value;
      const value = componentValue.value;

      if (value) {
        addComponent(type, value);
        componentValue.value = '';
      }
    });

    // Calculate button click event
    const calculateBtn = document.getElementById('calculate-btn');
    calculateBtn.addEventListener('click', function() {
      toggleSimulationMode(); // Start of simulation
      const voltageInput = document.getElementById('voltage-input');
      const frequencyInput = document.getElementById('frequency-input');

      const voltage = parseFloat(voltageInput.value);
      const frequency = parseFloat(frequencyInput.value);

      if (!isNaN(voltage) && !isNaN(frequency)) {
        const current = voltage / (Math.sqrt(Math.pow(totalResistance, 2) + Math.pow(totalReactance, 2)));
        const power = voltage * current;
        const currentUnit = 'A';
        const powerUnit = 'W';

        const resultContent = document.getElementById('result-content');
        resultContent.innerHTML = 'Intensité: ' + current.toFixed(2) + ' ' + currentUnit + '<br>' +
                                  'Puissance: ' + power.toFixed(2) + ' ' + powerUnit;

        const totalResistanceText = document.getElementById('total-resistance');
        totalResistanceText.textContent = 'Résistance totale: ' + totalResistance.toFixed(2)+ ' Ω';

        updateTotalReactance(); // Calculate the total reactance

        const totalReactanceText = document.getElementById('total-reactance');
        totalReactanceText.textContent = 'Réactance totale: ' + totalReactance.toFixed(2) + ' Ω';

        const numberOfComponentsText = document.getElementById('number-of-components');
        numberOfComponentsText.textContent = 'Nombre de composantes: ' + components.length;

        const emptyCircuitMessage = document.getElementById('empty-circuit-message');
        emptyCircuitMessage.style.display = components.length === 0 ? 'block' : 'none';
      } else {
        alert('Veuillez inscrire une bonne valeur de tension et de fréquence.');
      }
      toggleSimulationMode(); // End of simulation
    });