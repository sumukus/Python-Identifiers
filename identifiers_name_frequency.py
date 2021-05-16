import json

'''
It will count the frequency of length of identifiers name that will occur in entire repositories
Then it will save the data in rawIdentifiersNameFrequency.json file
The structure of json file is: {length:count}
'''

def countUniqueIdentifiersFrequency():
	identifiers_frequency_list = []
	with open("rawIdentifiersNames.json", 'r') as json_read_file:
		data = json.load(json_read_file)
		rawIdentifiers_name_frequency = {}
		for repo in data:
			for name in repo['identifiers_name']:
				keys = rawIdentifiers_name_frequency.keys()
				if len(name) in keys:
					rawIdentifiers_name_frequency[len(name)] = rawIdentifiers_name_frequency[len(name)] + 1

				else:
					rawIdentifiers_name_frequency[len(name)] = 1

		identifiers_frequency_list.append(rawIdentifiers_name_frequency)

		with open("rawIdentifiersNameFrequency.json", 'w') as json_write_file:
			json.dump(identifiers_frequency_list, json_write_file, indent=4, sort_keys=True)



countUniqueIdentifiersFrequency()
