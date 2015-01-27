puts "Your text: "
text = gets.chomp
puts "The word you want redacted: "
redact = gets.chomp

words = text.split(" ")

words.each do |x|
    if x == redact
        print "REDACTED "
    else
        print x + " "
    end
end