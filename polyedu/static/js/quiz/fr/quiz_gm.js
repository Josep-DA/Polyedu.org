$("#quiz").quiz({
    //resultsScreen: '#results-screen',
    //counter: false,
    //homeButton: '#custom-home',
    counterFormat: "Question %current de %total",
    questions: [
      {
        q: "Quelles sont les deux polices d'écritures principalement utilisés avec le Guide Méthodologique?",
        options: [
          "Impact et Georgia",
          "Arial et Times New Roman",
          "Courier New et Comic Sans MS",
          "Merriweather et Roboto Slab"
        ],
        correctIndex: 1,
        correctResponse: "Parfait! Les deux polices d'écritures principalement utilisés avec le Guide Méthodologique sont <strong>Arial et Times New Roman</strong>.",
        incorrectResponse: "Incorrect! Les deux polices d'écritures principalement utilisés avec le Guide Méthodologique sont <strong>Arial et Times New Roman</strong>."
      },
      {
        q: "Pour la majorité du document, quel est l'interligne devant être utilisé?",
        options: [
          "Simple",
          "1,15",
          "1,5",
          "Double"
        ],
        correctIndex: 2,
        correctResponse: "Parfait! Pour la majorité du document, l'interligne devant être utilisé doit être de <strong>1,5</strong>.",
        incorrectResponse: "Incorrect! Pour la majorité du document, l'interligne devant être utilisé doit être de <strong>1,5</strong>."
      },
      {
        q: "De combien les marges du document doivent-ils être?",
        options: [
          "0.5 cm",
          "1 cm",
          "1.5 cm",
          "2.5 cm"
        ],
        correctIndex: 3,
        correctResponse: "Parfait! Les marges du document doivent être de <strong>2.5 cm</strong>.",
        incorrectResponse: "Incorrect! Les marges du document doivent être de <strong>2.5 cm</strong>."
      },
      {
        q: "Quel doit être le format du papier?",
        options: [
          "Lettre (21.6 x 27.9 cm)",
          "A4 (21 x 29.7 cm)",
          "B4 (25 x 35.3 cm)",
          "A3 (29.7 x 42 cm)"
        ],
        correctIndex: 0,
        correctResponse: "Parfait! Le format du papier doit être de <strong>Lettre (21.6 x 27.9 cm)</strong>.",
        incorrectResponse: "Incorrect! Le format du papier doit être de <strong>Lettre (21.6 x 27.9 cm)</strong>."
      }
    ]
  });
  