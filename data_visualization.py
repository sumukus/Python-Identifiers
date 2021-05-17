import matplotlib.pyplot as plt
import json
import numpy as np

def similarityScatterPlot():
	with open("dataset/repoSimilarityDetails.json", 'r') as json_read_file:
		data = json.load(json_read_file)
		y_axis = []
		max_value = 0
		max_repo = ""
		min_value = 1
		min_repo = ""
		for value in data:
			if value['similarity_score'] > max_value:
				max_value = value['similarity_score']
				max_repo = value['repo_name']

			if value['similarity_score'] < min_value:
				min_value = value['similarity_score']
				min_repo = value['repo_name']
		for repo in data:
			y_axis.append(repo['similarity_score']) 

		x_axis = np.arange(len(y_axis))

		plt.scatter(x_axis,y_axis)
		plt.xlabel("Repositories")
		plt.ylabel("Similarity Score")
		plt.title("Similarity scores of Identifiers Name against Repositories")
		plt.text(0,max_value, f"Repo Name:{max_repo} Max Similarity Score:{round(max_value,2)}", color='green')
		plt.text(0,min_value, f"Repo Name:{min_repo} Min Similarity Score:{round(min_value,2)}", color='red')
		plt.show()

def identifiersNameLengthBarGraph():
	with open("dataset/rawIdentifiersNameFrequency.json", 'r') as json_read_file:
		data = json.load(json_read_file)
		identifiers_group_frequency = [[0] for _ in range(10)]
		for value in data:
			keys = value.keys()
			for k in keys:
				if int(k) <= 10:
					identifiers_group_frequency[0].append(value[k])
				elif int(k) <= 20:
					identifiers_group_frequency[1].append(value[k])
				elif int(k) <= 30:
					identifiers_group_frequency[2].append(value[k])
				elif int(k) <= 40:
					identifiers_group_frequency[3].append(value[k])
				elif int(k) <= 50:
					identifiers_group_frequency[4].append(value[k])
				elif int(k) <= 60:
					identifiers_group_frequency[5].append(value[k])
				elif int(k) <= 70:
					identifiers_group_frequency[6].append(value[k])
				elif int(k) <= 80:
					identifiers_group_frequency[7].append(value[k])
				elif int(k) <= 90:
					identifiers_group_frequency[8].append(value[k])
				else:
					identifiers_group_frequency[9].append(value[k])

		y_axis = [sum(x) for x in identifiers_group_frequency]
		total_sum = sum(y_axis)
		x_axis = np.arange(10)
		x_labels = ["0-10", "11-20", "21-30", "31-40", "41-50", "51-60", "61-70", "71-80", "81-90", "91<"]

		gbar = plt.bar(x_axis, y_axis, width=0.5)
		for g in gbar:
			h = g.get_height()
			plt.text(g.get_x() + g.get_width()/2.0, h, f"{h/total_sum*100:.6f}%", ha='center', va='bottom')

		plt.xticks(x_axis, x_labels)
		plt.xlabel("Identifiers length range")
		plt.ylabel("Total number of Identifiers")
		plt.title("Identifiers length against total count")
		plt.show()






similarityScatterPlot()
identifiersNameLengthBarGraph()
