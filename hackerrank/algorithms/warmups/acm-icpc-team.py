def max_topics(competitors, people):
    max_topics = 0
    teams = 0
    for j in range(people):
        for k in range(people):
            topics = bin(competitors[j] | competitors[k]).count("1")
            if topics > max_topics:
                teams = 1
                max_topics = topics
            elif topics == max_topics:
                teams += 1
    return (max_topics, teams)

people, topics = (int(x) for x in raw_input().split())

competitors = []

for i in range(people):
    competitors.append(int(raw_input(), 2))

max_topics, teams = max_topics(competitors, people)
print max_topics
print (teams / 2)