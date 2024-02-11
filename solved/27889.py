from sys import stdin 

s = stdin.readline().strip()

school_names = {
    'NLCS': 'North London Collegiate School',
    'BHA': 'Branksome Hall Asia',
    'KIS': 'Korea International School',
    'SJA': 'St. Johnsbury Academy',
}

print(school_names[s])
