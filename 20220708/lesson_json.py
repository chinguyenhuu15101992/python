import json

country = '{"name":"United States", "population":331002651}'
country_dict = json.loads(country)



print (type(country))