var userChoice = prompt("Do you choose rock, paper or scissors?");
var computerChoice = Math.random();
if (computerChoice < 0.34) {
	computerChoice = "rock";
} else if(computerChoice <= 0.67) {
	computerChoice = "paper";
} else {
	computerChoice = "scissors";
} console.log("Computer: " + computerChoice);

var compare = function (choice1, choice2) {
    if (choice1 === choice2) {
        console.log("The result is a tie! Could you pick again?");
        compare(userChoice, computerChoice);
    }
    else if (choice1 === "rock") {
        if (choice2 === "scissors") {
            return "rock wins";
        }
        else {
            return "paper wins";
        }
    }
    else if (choice1 === "paper") {
        if (choice2 === "rock") {
            return "paper wins";
        }
        else {
            return "scissors wins";
        }
    }
    else if (choice1 === "scissors") {
        if (choice2 === "paper") {
            return "scissors wins";
        }
        if (choice2 === "rock") {
            return "rock wins";
        }
    }
    else {
        console.log "That's not one of the choices. Could you pick again?";
    }
};

compare(userChoice, computerChoice);