print "Please enter a word."
user_input = gets.chomp
user_input.downcase!
if user_input.include? "s"
    user_input.gsub!(/s/, "th")
else
    print "Sadly, the letter 's' is not in your name."
end
puts "Oh, '#{user_input},' you say?"