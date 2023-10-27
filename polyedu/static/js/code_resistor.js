document.querySelector('#resistor-form').addEventListener('submit', function(event) {
    event.preventDefault();

    // Retrieve the selected values
    const resistorType = document.querySelector('#resistor-type').value;
    const band1Color = document.querySelector('#band1-color').value;
    const band2Color = document.querySelector('#band2-color').value;
    const band3Color = document.querySelector('#band3-color').value;
    const band4Color = document.querySelector('#band4-color').value;
    const band5Color = resistorType === '5-band' ? document.querySelector('#band5-color').value : null;

    // Calculate the resistance based on the selected values
    let result = null;
    if (resistorType === '4-band') {
      result = calculateResistance4Band(band1Color, band2Color, band3Color, band4Color);
    } else if (resistorType === '5-band') {
      result = calculateResistance5Band(band1Color, band2Color, band3Color, band4Color, band5Color);
    }

    // Display the result
    let resultText = `Resistance: ${result.resistance} Ohms`;
    if (result.tolerance !== null) {
      resultText += ` (Tolerance: ${result.tolerance}%)`;
    }
    document.querySelector('#result').textContent = resultText;

    // Update the visual representation of the resistor
    updateResistorVisual(band1Color, band2Color, band3Color, band4Color, band5Color);
  });

  function calculateResistance4Band(band1Color, band2Color, band3Color, band4Color) {
    const colorCode = {
      black: 0,
      brown: 1,
      red: 2,
      orange: 3,
      yellow: 4,
      green: 5,
      blue: 6,
      violet: 7,
      gray: 8,
      white: 9,
      gold: -1,
      silver: -2,
    };

    const significantFigure = (colorCode[band1Color] * 10) + colorCode[band2Color];
    const multiplier = Math.pow(10, colorCode[band3Color]);
    const tolerance = calculateTolerance(band4Color);

    const resistance = significantFigure * multiplier;
    return { resistance, tolerance };
  }

  function calculateResistance5Band(band1Color, band2Color, band3Color, band4Color, band5Color) {
    const colorCode = {
      black: 0,
      brown: 1,
      red: 2,
      orange: 3,
      yellow: 4,
      green: 5,
      blue: 6,
      violet: 7,
      gray: 8,
      white: 9,
    };

    const significantFigure = (colorCode[band1Color] * 100) + (colorCode[band2Color] * 10) + colorCode[band3Color];
    const multiplier = Math.pow(10, colorCode[band4Color]);
    const tolerance = calculateTolerance(band5Color);

    const resistance = significantFigure * multiplier;
    return { resistance, tolerance };
  }

  function calculateTolerance(bandColor) {
    const toleranceValues = {
      brown: 1,
      red: 2,
      green: 0.5,
      blue: 0.25,
      violet: 0.1,
      gray: 0.05,
      gold: 5,
      silver: 10,
      // Add more color codes and their corresponding tolerance values...
    };

    const tolerance = toleranceValues[bandColor];
    return tolerance;
  }

  // Hide the fifth band select initially
  const band5ColorSelect = document.querySelector('#band5-color');
  const band5ColorSelectLabel = document.querySelector('#band5-color-label');
  band5ColorSelect.style.display = 'none';
  band5ColorSelectLabel.style.display = 'none';

  // Show or hide the fifth band select based on the selected resistor type
  document.querySelector('#resistor-type').addEventListener('change', function() {
    const resistorType = this.value;

    if (resistorType === '5-band') {
      band5ColorSelect.style.display = 'inline-block';
      band5ColorSelectLabel.style.display = 'inline-block';
    } else {
      band5ColorSelect.style.display = 'none';
      band5ColorSelectLabel.style.display = 'none';
    }
  });

  function updateResistorVisual(band1Color, band2Color, band3Color, band4Color, band5Color) {
    const bandColors = [band1Color, band2Color, band3Color, band4Color, band5Color];
    const bandElements = document.querySelectorAll('.band');

    for (let i = 0; i < bandElements.length; i++) {
      const bandElement = bandElements[i];
      const bandColor = bandColors[i];

      bandElement.style.backgroundColor = bandColor;
    }
  }