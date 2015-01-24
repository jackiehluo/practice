var friends = {
    bill: {
        firstName: "Bill",
        lastName: "Gates",
        number: "(206) 555-5555",
        address: ["One Microsoft Way", "Redmond", "WA", "98052"],
    },
    steve: {
        firstName: "Steve",
        lastName: "Jobs",
        number: "(212) 111-1111",
        address: ["One Infinite Loop", "Cupertino", "CA", "95014"],
    },
};

var list = function(friends) {
    for (var key in friends) {
        console.log(key);
    }
}

var search = function(name) {
    for (var look in friends) {
        if (friends[look].firstName === name) {
            console.log(friends[look]);
            return friends[look];
        }
    }
};