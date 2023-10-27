const canvas = document.getElementById('canvas');
const ctx = canvas.getContext('2d');
const inputA = document.getElementById('inputA');
const inputB = document.getElementById('inputB');
const inputC = document.getElementById('inputC');
const areaElement = document.getElementById('area');
const focusElement = document.getElementById('focus');

function calculateC(a, b) {
    if (a > b) {
        return Math.sqrt(a*a - b*b);
    } else if (b > a) {
        return Math.sqrt(b*b - a*a);
    } else {
        return 0; // a and b are equal, no foci
    }
}

function calculateFoci(a, b, c) {
    if (a > b) {
        return [{ x: c, y: 0 }, { x: -c, y: 0 }];
    } else if (b > a) {
        return [{ x: 0, y: c }, { x: 0, y: -c }];
    } else {
        return []; // a and b are equal, no foci
    }
}

function updateInputs(a, b, c) {
    inputA.value = a;
    inputB.value = b;
    inputC.value = c;
}

function drawEllipse(a, b, c) {
    canvas.width = a * 2;
    canvas.height = b * 2;
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    
    const centerX = a;
    const centerY = b;

    // Draw ellipse
    ctx.beginPath();
    ctx.ellipse(centerX, centerY, a, b, 0, 0, 2 * Math.PI);
    ctx.stroke();

    // Draw lines for 'a' and 'b'
    ctx.beginPath();
    ctx.moveTo(centerX, centerY);
    ctx.lineTo(centerX + a, centerY);
    ctx.moveTo(centerX, centerY);
    ctx.lineTo(centerX, centerY - b);
    ctx.stroke();

    // Label 'a' and 'b'
    ctx.font = '12px Arial';
    ctx.fillText('a', centerX + a/2, centerY + 10);
    ctx.fillText('b', centerX + 10, centerY - b/2);

    // Draw foci
    const foci = calculateFoci(a, b, c);
    ctx.beginPath();
    ctx.arc(foci[0].x + a, foci[0].y + b, 3, 0, 2 * Math.PI, false);
    ctx.arc(foci[1].x + a, foci[1].y + b, 3, 0, 2 * Math.PI, false);
    ctx.fill();
    
    // Label foci
    ctx.fillText('F1', foci[0].x + a + 5, foci[0].y + b);
    ctx.fillText('F2', foci[1].x + a - 20, foci[1].y + b);

    // Draw ABC triangle with 'c' as hypotenuse
    ctx.beginPath();
    
    if (a > b) {
        ctx.moveTo(centerX, centerY - b);
    ctx.lineTo(foci[0].x + a, foci[0].y + b);
    } else if (b > a) {
        ctx.moveTo(centerX + a, centerY);
        ctx.lineTo(foci[1].x + a, foci[1].y + b);
    }
    ctx.closePath();
    ctx.strokeStyle = 'red'; // Set the color for the hypotenuse
    ctx.stroke();

    // Draw 'c' label
    if (a > b) {
        var cX = (centerX + foci[0].x + a) / 2;
        var cY = (centerY + foci[0].y ) / 2;
    } else if (b > a) {
        var cX = (centerX + foci[1].x + a * 2) / 2;
        var cY = (centerY + foci[1].y + b) / 2;
    }
    ctx.font = 'bold 14px Arial';
    ctx.fillStyle = 'red';
    ctx.fillText('c', cX, cY);

    updateInputs(a, b, c);

    // Update area value
    const area = Math.PI * a * b;
    areaElement.textContent = area.toFixed(2); // Display the area with two decimal places

    // Update focus coordinates
    focusElement.innerHTML = `F1(${foci[0].x + a}, ${foci[0].y + b}), F2(${foci[1].x + a}, ${foci[1].y + b})`;
}




function handleInputChange() {
    const a = Number(inputA.value);
    const b = Number(inputB.value);
    const c = calculateC(a, b);
    drawEllipse(a, b, c);
}

inputA.addEventListener('input', handleInputChange);
inputB.addEventListener('input', handleInputChange);
inputC.addEventListener('input', handleInputChange);

handleInputChange(); // Initialize the ellipse with default values
