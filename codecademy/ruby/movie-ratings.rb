movies = {
    "The Prestige" => 4,
    "Black Swan" => 3,
    "The Social Network" => 4,
}

puts("You can add, update, display, or delete movies. Please type your choice.")
choice = gets.chomp

case choice
when "add"
    puts("Movie title?")
    title = gets.chomp
    puts("Rating?")
    rating = gets.chomp
    if movies[title.to_sym].nil? == true
        movies[title.to_sym] = rating.to_i
    else
        puts "I'm sorry, that movie is already there!"
    end
when "update"
    puts("Movie title?")
    title = gets.chomp
    if movies[title].nil? == true
        puts "I'm sorry, that movie isn't here."
    else
        puts("New rating?")
        rating = gets.chomp
        movies[title.to_sym] = rating.to_i
    end
when "display"
    movies.each do |title, rating|
        puts "#{title}: #{rating}"
    end
when "delete"
    puts("Movie title?")
    title = gets.chomp
    if movies[title].nil? == true
        puts "I'm sorry, that movie isn't here."
    else
        movies.delete(title)
    end
else
    puts "Error!"
end