require 'csv'
require 'open-uri'

class Reservations

    @months = {"01" => 31, "02" => 28, "03" => 31, "04" => 30,
            "05" => 31, "06" => 30, "07" => 31, "08"  => 31,
            "09" => 30, "10" => 31, "11" => 30, "12" => 31}


    def initialize(url, date)
        @url = url
        @date = date
    end


    def check_month
        revenue = 0
        capacity = 0
        csv = CSV.new(open(@url), :headers => :first_row)
        CSV.foreach(csv) do |line|
            data = line.inspect
            if (@date >= data[2][0..-4] and data[3].length == 10 and
                @date <= data[3][0..-4])
                if (@date == data[2][0..-4])
                    revenue += prorate_start(data[1], data[2])
                elsif (@date == data[3][0..-4])
                    revenue += prorate_end(data[1], data[3])
                else
                    revenue += data[1].to_i * 100
                end
            elsif (@date >= data[2][0..-4] and data[3].length == 1)
                if (@date == data[2][0..-4])
                    revenue += prorate_start(data[1], data[2])
                else
                    revenue += data[1].to_i * 100
                end
            else
                capacity += data[0].to_i
            end
        end
        puts "Expected Revenue: $%.2f" % (revenue / 100.00)
        puts "Expected Total Capacity of Unreserved Offices: #{capacity}"
    end


    def prorate_start(price, date)
        days = @months[date[5..-4]]
        rate = (price.to_i * 100 / days) * (days - date[8..10].to_i + 1)
    end


    def prorate_end(price, date)
        days = @months[date[5..-4]]
        rate = (price.to_i * 100 / days) * date[8..10].to_i
    end

end


if __FILE__ == $0
    date = gets.chomp
    reservations = Reservations.new('http://s3.amazonaws.com/misc-ww/data.csv', date)
    reservations.check_month
end