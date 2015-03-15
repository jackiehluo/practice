$.getJSON("https://api.github.com/search/repositories?q=Space%20Invaders%20HTML5+language:JavaScript&callback=?", function(data) {
    console.log(data);
});