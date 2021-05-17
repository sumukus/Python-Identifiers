import json
import os

def detectPythonFile():
	
	file_name_list = []
	repo_list = os.listdir('repo/')
	#This is used for truncating absolute path when saving python file name
	present_path = os.path.abspath(".")
	with open("pythoncodepath.json", 'w') as jsonfile:
		for repo in repo_list:

			data = {"repo_name":" ", "python_file_name": []}
			data['repo_name'] = repo

			location = os.path.abspath(f"repo/{repo}")
			
			items = os.listdir(location)

			while True:
				new_dir = []
				for value in items:
					if '/home' not in value: 
						if os.path.isfile(f"{location}/{value}"):
							if value[len(value)-3:] == ".py":
								print(f"writing {value} files to json")
								path = f"{location}/{value}"
								path = path.replace(f"{present_path}/", "")

								data['python_file_name'].append(path)

						elif os.path.isdir(f"{location}/{value}"):
							new_dir.append(f"{location}/{value}")

						else:
							pass
					else:
						new_dir.append(value)

				items.clear()
				items = items + new_dir
			
				if len(items) != 0:
					temp_list = os.listdir(items[0])
					location = os.path.abspath(items[0])
					items.pop(0)
					items = items + temp_list
				else:
					break
			file_name_list.append(data)
		json.dump(file_name_list, jsonfile, indent=4, sort_keys=True)

detectPythonFile()
