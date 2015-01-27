user = prompt("Do you want to sing, dance, or act?").toLowerCase();

var talented = true;
var beautiful = false;

switch(user) {
    case 'sing':
        if (talented && beautiful) {
            console.log("You're the new T-Swift!");
        }
        else if (talented || beautiful) {
            console.log("You can do it!");
        }
        else {
            console.log("Well... it'll be a hard road ahead for you.");
        }
        break;
    case 'dance':
        console.log("Tough luck. No celebrities there.");
        break;
    case 'act':
        if (talented || beautiful) {
            console.log("Wow, big dreams. I think you've got what it takes to be the next Meryl Streep.");
        }
        else {
            console.log("Sorry. Maybe try reality shows?");
        }
        break;
    default:
        console.log("Someone lacks ambition...");
}