function startWave() {
    var waveType = document.getElementById('waveType').value;
    var wavelength = document.getElementById('wavelength').value;
    var frequency = document.getElementById('frequency').value;
    var amplitude = document.getElementById('amplitude').value;
    var period = document.getElementById('period').value;

    var waveElement = document.getElementById('wave');
    waveElement.innerHTML = '';

    if (waveType === 'transverse') {
        waveElement.classList.add('transverse');
        waveElement.classList.remove('longitudinal');
        createTransverseWave(waveElement, wavelength, frequency, amplitude, period);
    } else if (waveType === 'longitudinal') {
        waveElement.classList.add('longitudinal');
        waveElement.classList.remove('transverse');
        createLongitudinalWave(waveElement, wavelength, frequency, amplitude, period);
    }

    classifyWave(wavelength);
}

function classifyWave(wavelength) {
    var classification = '';
    if (wavelength > 1000000) {
        classification = 'Ondes radio';
    } else if (wavelength > 1000) {
        classification = 'Micro-ondes';
    } else if (wavelength > 700) {
        classification = 'Infrarouges';
    } else if (wavelength >= 400 && wavelength <= 700) {
        classification = 'Lumière visible';
        var color = determineVisibleLightColor(wavelength);
        displayColor(color);
    } else if (wavelength > 10) {
        classification = 'Ultra-violet';
    } else if (wavelength > 0.01) {
        classification = 'Rayons X';
    } else {
        classification = 'Rayons Gamma';
    }
    document.getElementById('classification').innerHTML = classification;

    var colorDiv = document.getElementById('colorDiv');
    var waveElement = document.getElementById('wave');

    if (classification !== 'Lumière visible') {
        colorDiv.style.display = 'none';
        waveElement.classList.remove('visible');
    } else {
        colorDiv.style.display = 'block';
        waveElement.classList.add('visible');

        var colorFrench = determineVisibleLightColor(wavelength);
        var colorEnglish = convertColorFrenchToEnglish(colorFrench);
        document.documentElement.style.setProperty('--wave-color', colorEnglish);
    }
}

function determineVisibleLightColor(wavelength) {
    var color = '';
    var colorFrench = ''; // Déclarer colorFrench avec une chaîne vide

    if (wavelength >= 620 && wavelength <= 750) {
        colorFrench = 'Rouge';
    } else if (wavelength >= 590 && wavelength < 620) {
        colorFrench = 'Orange';
    } else if (wavelength >= 570 && wavelength < 590) {
        colorFrench = 'Jaune';
    } else if (wavelength >= 495 && wavelength < 570) {
        colorFrench = 'Vert';
    } else if (wavelength >= 450 && wavelength < 495) {
        colorFrench = 'Bleu';
    } else if (wavelength >= 380 && wavelength < 450) {
        colorFrench = 'Violet';
    }

    color = convertColorFrenchToEnglish(colorFrench);
    return color;
}


function displayColor(colorFrench) {
    document.getElementById('color').innerHTML = colorFrench;
}





function createTransverseWave(container, wavelength, frequency, amplitude, period) {
    var waveWidth = container.offsetWidth;
    var time = 0;
    var interval = setInterval(function() {
        var waveCircle = document.createElement('div');
        waveCircle.classList.add('wave-circle');
        var leftOffset = (waveWidth * time / period) % waveWidth;
        waveCircle.style.left = leftOffset + 'px';
        waveCircle.style.bottom = amplitude * Math.sin(2 * Math.PI * frequency * time) + 'px';
        container.appendChild(waveCircle);
        time += 0.01;
        if (time >= period) {
            clearInterval(interval);
        }
    }, 10);
}

function createLongitudinalWave(container, wavelength, frequency, amplitude, period) {
    var waveWidth = container.offsetWidth;
    var time = 0;
    var interval = setInterval(function() {
        var waveLine = document.createElement('div');
        waveLine.classList.add('wave-line');
        var leftOffset = (waveWidth * time / period) % waveWidth;
        waveLine.style.left = leftOffset + 'px';
        waveLine.style.bottom = amplitude + 'px';
        container.appendChild(waveLine);
        time += 0.01;
        if (time >= period) {
            clearInterval(interval);
        }
    }, 10);
}

function convertColorFrenchToEnglish(color) {
    var colorMap = {
      rouge: 'red',
      orange: 'orange',
      jaune: 'yellow',
      vert: 'green',
      bleu: 'blue',
      violet: 'purple'
    };
  
    return colorMap[color.toLowerCase()] || color; // Utilisation de la couleur d'origine si la correspondance n'est pas trouvée
  }
  