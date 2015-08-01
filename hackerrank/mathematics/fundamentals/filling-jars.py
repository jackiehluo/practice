def fill_jars(count, a, b, candies):
    count += (b - a + 1) * candies
    return count
    
jars, operations = (int(x) for x in raw_input().split())
count = 0

for i in range(operations):
    a, b, candies = (int(y) for y in raw_input().split())
    count = fill_jars(count, a, b, candies)
average = count / jars
print average