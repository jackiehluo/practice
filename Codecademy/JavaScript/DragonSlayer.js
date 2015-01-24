var slaying = true;
var youHit = Math.floor(Math.random() * 2);
var damageThisRound = Math.floor(Math.random() * 5 + 1);
var totalDamage = 0;

while (slaying) {
    slaying = false;
    if (youHit == 1) {
        console.log("You hit the dragon!");
        totalDamage += damageThisRound;
        if (totalDamage >= 4) {
            console.log("The player killed the dragon.");
            slaying = false;
        }
        else {
            youHit = Math.floor(Math.random() * 2);
        }
    }
    else {
        console.log("The dragon defeated you.");
    }
}