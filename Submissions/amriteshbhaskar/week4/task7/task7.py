import shodan

key = 'F0gr1M7T08FKs5irlKCKWZkBeFuqIoNf'
api = shodan.Shodan(key)

query = 'apache'

result = api.count(query, facets=[('country', 3), ('org', 3)])

print('Top 3 countries are:- ')
for count in (result['facets']['country']):
    print(count['value'] + ' having ' + str(count['count']) + ' servers')

print()
print('Top 3 Organisations are:- ')
for count in (result['facets']['org']):
    print(count['value'] + ' having ' + str(count['count']) + ' servers')
