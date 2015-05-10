from datetime import datetime

for _ in range(int(input())):
    start = datetime.strptime(input(), '%a %d %b %Y %H:%M:%S %z')
    end = datetime.strptime(input(), '%a %d %b %Y %H:%M:%S %z')
    print(abs(int((end - start).total_seconds())))