// Setup your quiz text and questions here

// NOTE: pay attention to commas, IE struggles with those bad boys

var quizJSON = {
    "info": {
        "name":    "Test Your Baseball Knowledge!!",
        "main":    "<p>Test your knowledge of current and historical sports knowledge! This month's featured sport is Baseball.  </p>",
        "results": "<h5>Learn More</h5><p>Etiam scelerisque, nunc ac egestas consequat, odio nibh euismod nulla, eget auctor orci nibh vel nisi. Aliquam erat volutpat. Mauris vel neque sit amet nunc gravida congue sed sit amet purus.</p>",
        "level1":  "Baseball Trivia-Night Ready",
        "level2":  "Trivia Contender",
        "level3":  "Diamond Amateur",
        "level4":  "Trivia Beginner",
        "level5":  "Hit the books, you'll get there" // no comma here
    },
    "questions": [
        { // Question 1 - Multiple Choice, Single True Answer
            "q": "What year was the first official game of baseball played?",
            "a": [
                {"option": "1876",      "correct": false},
                {"option": "1493",     "correct": false},
                {"option": "1910",      "correct": false},
                {"option": "1846",     "correct": true} // no comma here
            ],
            "correct": "<p><span>That's right!</span> The first offical game of baseball was played in 1846, before the Civil War!</p>",
            "incorrect": "<p><span>Incorrect</span> The first offical game of baseball was played in 1846, before the Civil War!</p>" // no comma here
        },
        { // Question 2 - Multiple Choice, Multiple True Answers, Select Any
            "q": "Who is the head coach of the Tar Heels?",
            "a": [
                {"option": "Matt Williams",               "correct": false},
                {"option": "Mike Fox",                   "correct": true},
                {"option": "Mike Rizzo",               "correct": false},
                {"option": "Dave Arendas", "correct": false} // no comma here
            ],
            "select_any": true,
            "correct": "<p><span>Nice!</span> Mike Fox, graduate of the University of North Carolina, is in his 15th season as head coach.</p>",
            "incorrect": "<p><span> Incorrect. </span> Mike Fox, graduate of the University of North Carolina, is in his 15th season as head coach.</p>" // no comma here
        },
        { // Question 3 - Multiple Choice, Multiple True Answers, Select All
            "q": "How much did the average baseball ticket cost in 1920?",
            "a": [
                {"option": "$1",           "correct": true},
                {"option": "50 cents",                  "correct": false},
                {"option": "$3",  "correct": false},
                {"option": "All games were free back then",          "correct": false} // no comma here
            ],
            "correct": "<p><span>Brilliant!</span> The average baseball ticket cost $1.00 in 1920. Booming 20s?</p>",
            "incorrect": "<p><span>Not Quite.</span> The average baseball ticket cost $1.00 in 1920. Booming 20s?</p>" // no comma here
        },
        { // Question 4
            "q": "What year was the first TV broadcast of a baseball game?",
            "a": [
                {"option": "1950",    "correct": false},
                {"option": "1939",     "correct": true},
                {"option": "1945",      "correct": false},
                {"option": "1921",   "correct": false} // no comma here
            ],
            "correct": "<p><span>Correct!</span> The first televised baseball game in the United States was 1939.</p>",
            "incorrect": "<p><span>Nope</span> The first televised baseball game in the United States was 1939.</p>" // no comma here
        },
        { // Question 5
            "q": "Go Heels?",
            "a": [
                {"option": "Yes",    "correct": true},
                {"option": "No",     "correct": false} // no comma here
            ],
            "correct": "<p><span>Correct</span>You've come to the right place. </p>",
            "incorrect": "<p><span>ERRRR!</span>You can leave now. </p>" // no comma here
        } // no comma here
    ]
};
