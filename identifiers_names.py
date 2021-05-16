import json,time

'''
It will count the unique number of identifiers name from all the repositories
Then it will save in identifiersName.json file
The structure of json file is: {"identifiers_name":[], total_count: int}
'''

def uniqueIdentifiers():
	identifiers_name_list = []
	count = 0
	with open("dataset/atomicIdentifiersName.json", 'r') as json_read_file:
		identifiers_names = {'identifiers_name':[], "total_count":0}
		identifiers_names_set = set()
		data = json.load(json_read_file)
		for repo in data:
			for name in repo['atomic_identifiers_name']:
				if "/" not in name:
					if name.isalnum() or name.isalpha():
						identifiers_names_set.add(name)
						count += 1
	
		identifiers_names['identifiers_name'] = identifiers_names['identifiers_name'] + list(identifiers_names_set)
		identifiers_names['total_count'] = count
		identifiers_name_list.append(identifiers_names)

		with open("identifiersName.json", 'w') as json_write_file:
			json.dump(identifiers_name_list, json_write_file, indent=4, sort_keys=True)


uniqueIdentifiers()

