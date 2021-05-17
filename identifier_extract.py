
import tokenize, json, keyword, time

def writeIdentifiersNames(repo_name, file_path_list):
	data = {"repo_name":" ", "identifiers_name":[]}
	data['repo_name'] = repo_name
	for single_file_path in file_path_list:

		#For reading each line of code for individual pyhton code file
		with open(single_file_path, 'rb') as filereader:
			for line in filereader:
				try:
					tokens = tokenize.tokenize(filereader.readline)
					for token in tokens:						
						if token.string.isidentifier() and not keyword.iskeyword(token.string):
							data['identifiers_name'].append(token.string)
							#print(f"   Writing --{token.string}-- identifiers name in json file")
				except tokenize.TokenError:
					pass

				except:
					#To catch any other sort of unknown error occur due to token
					pass
	return data




def readPythonFile():
	#Open the pythoncodefile which contains path of python code pythoncodepath.json
	with open("pythoncodepath.json", 'r') as json_read_file:
		data = json.load(json_read_file)
		identifiers_name_list = []
		with open("rawIdentifiersNames.json", 'w') as json_write_file:
			#print("Initiating the writing of Identifiers Name to json file")
			time.sleep(2)
			for repo_data in data:
				repo_info = writeIdentifiersNames(repo_data['repo_name'], repo_data['python_file_name'])
				identifiers_name_list.append(repo_info)
			json.dump(identifiers_name_list, json_write_file, indent=4, sort_keys=True)
		#print("Writing of Identifiers Names is successfully completed")

start_time = time.time()
readPythonFile()
duration = time.time() - start_time
f = open("time.txt", 'w')
f.write(str(duration))
f.close()

