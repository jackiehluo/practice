def alphabetize(arr, rev = false)
    arr.sort!
    if rev == true
        arr.reverse!
    end
    arr
end

numbers = [1, 2, 3, 4, 5]
answer = alphabetize(numbers)
puts answer