import json

HughMovies = []
ratingAvg = 0

with open ('movies.json') as f:
    data = []
    for line in f:
        data.append(json.loads(line))

for line in data:
    for lst in line['actors']:
        if lst[1] == 'Hugh Jackman':
            HughMovies.append(line)

for line in HughMovies:
       rating = line['rating']['avg']    
       ratingAvg += rating

answer = ratingAvg/len(HughMovies)

print(round(answer, 2))
    
