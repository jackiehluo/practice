require 'csv'
require 'open-uri'

class Reservations

    def initialize(url, date)
        @url = url
        @date = date
        @months = {"01" => 31, "02" => 28, "03" => 31, "04" => 30,
            "05" => 31, "06" => 30, "07" => 31, "08"  => 31,
            "09" => 30, "10" => 31, "11" => 30, "12" => 31}
    end


    def check_month
        revenue = 0.00
        capacity = 0
        csv = CSV.parse(open(@url).read, :headers => true)
        csv.each do |data|
            if (@date >= data["StartDay"][0..-4] and data["EndDay"] == nil)
                if (@date == data["StartDay"][0..-4])
                    revenue += prorate_start(data["MonthlyPrice"], data["StartDay"])
                else
                    revenue += data["MonthlyPrice"].to_i
                end
            elsif (@date >= data["StartDay"][0..-4] and not data["EndDay"] == nil and
                @date <= data["EndDay"][0..-4])
                if (@date == data["StartDay"][0..-4])
                    revenue += prorate_start(data["MonthlyPrice"], data["StartDay"])
                elsif (@date == data["EndDay"][0..-4])
                    revenue += prorate_end(data["MonthlyPrice"], data["EndDay"])
                else
                    revenue += data["MonthlyPrice"].to_i
                end
            elsif (not @date == data["StartDay"][0..-4])
                if (not data["EndDay"] == nil and not @date == data["EndDay"][0..-4])
                    capacity += data["Capacity"].to_i
                elsif (data["EndDay"] == nil)
                    capacity += data["Capacity"].to_i
                end
            end
        end
        puts "Expected Revenue: $%.2f" % (revenue)
        puts "Expected Total Capacity of Unreserved Offices: #{capacity}"
    end


    def prorate_start(price, date)
        days = @months[date[5..-4]]
        rate = (price.to_f / days) * (days - date[8..10].to_i + 1)
    end


    def prorate_end(price, date)
        days = @months[date[5..-4]]
        rate = (price.to_f / days) * date[8..10].to_i
    end

end


if __FILE__ == $0
    date = gets.chomp
    reservations = Reservations.new('http://s3.amazonaws.com/misc-ww/data.csv', date)
    reservations.check_month
end