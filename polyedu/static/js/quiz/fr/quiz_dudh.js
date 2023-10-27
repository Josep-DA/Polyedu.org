$("#quiz").quiz({
    //resultsScreen: '#results-screen',
    //counter: false,
    //homeButton: '#custom-home',
    counterFormat: "Question %current de %total",
    questions: [
      {
        q: "Complétez la phrase: L’article 3 de la déclaration universelle des droits de l’Homme correspond au droit…",
        options: [
          "...à la liberté d’opinion et d’expression.",
          "...à la vie, à la liberté et à la sûreté de sa personne.",
          "à... la sécurité sociale.",
          "à... l’éducation."
        ],
        correctIndex: 1,
        correctResponse: "Parfait! L'article 3 de la dudh est le droit à la vie, à la liberté et à la sûreté de sa personne.",
        incorrectResponse: "Incorrect! L'article 3 de la dudh correspond au droit <strong>à la vie, à la liberté et à la sûreté de sa personne</strong>."
      },
      {
        q: "Vrai ou faux? L'article 3 de la DUDH correspond à l'article 7 de la Charte canadienne des droits et libertés.",
        options: ["Vrai", "Faux"],
        correctIndex: 0,
        correctResponse: "Parfait, vous avez eu la bonne réponse.",
        incorrectResponse: "Et non! La bonne réponse était <strong>vrai</strong>."
      },
      {
        q: "Les trois termes décrivant l'article 3 de la DUDH peuvent être résumés en un mot. Lequel?",
        options: [
          "L'éducation.",
          "La liberté d'expression.",
          "La sécurité (globale).",
          "La santé."
        ],
        correctIndex: 2,
        correctResponse: "Oui!! Ces trois termes, vie, liberté et sûreté, étant reliés, ils peuvent être résumé en un mot: <strong>sécurité</strong>. L’article 3 de la DUDH a donc pour objectif d'assurer une sécurité globale à tous sans exception.",
        incorrectResponse: "Non, ces trois termes, tout en étant reliés, peuvent être résumés en un mot: <strong>sécurité</strong>. L’article 3 de la DUDH a donc pour objectif d'assurer une sécurité globale à tous sans exception."
      }
    ]
  });
  