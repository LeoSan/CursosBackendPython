from sample_data import sample_articles

counter = 1
for article in sample_articles:
    print(f'{counter}: {article}')
    counter = counter + 1

sample_articles_enum = enumerate(sample_articles, start=10)
for counter, article in sample_articles_enum:
    print(f'{counter}: {article}')