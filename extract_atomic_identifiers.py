from spiral import ronin
import json, time

'''
It will convert the identifiers name into its atomic form. i.e, totalCount into total and Count
It uses the spiral library to convert the raw identifiers into atomic form. The model name is ronin from spiral library
It will store the atomic identifier name atomicIdentifiersName.json file
The structure of file is: {repo_name:repo_name, atomic_identifiers_name:[]}
'''

count = 0
def convertToAtomicIdentifiers(repo_name, raw_identifiers_name):
	global count
	data = {"repo_name":" ", "atomic_identifiers_name":[]}
	atomic_identifiers_list = []
	data['repo_name'] = repo_name

	for raw_name in raw_identifiers_name:
		try:
			atomic_names = ronin.split(raw_name)
			#print(f"{count} Writing {atomic_names}identifiers list")
			atomic_identifiers_list = atomic_identifiers_list + atomic_names
			count+=1

		except:
			pass
		

	atomic_identifiers_set = set(atomic_identifiers_list)
	data['atomic_identifiers_name'] = list(atomic_identifiers_set)

	return data
		



def readIdentifiersNames():

	with open("rawIdentifiersNames.json", 'r') as json_read_file:
		data = json.load(json_read_file)
		atomic_identifiers_list = []

		for repo in data:
			repo_info = convertToAtomicIdentifiers(repo['repo_name'], repo['identifiers_name'])
			atomic_identifiers_list.append(repo_info)

		with open("atomicIdentifiersName.json", "w") as json_write_file:
			json.dump(atomic_identifiers_list, json_write_file, indent=4, sort_keys=True)

			
start_time = time.time()
readIdentifiersNames()
duration = time.time() - start_time
f = open("time2.txt", 'w')
f.write(str(duration))
f.close()

