import json,spacy
'''
It will compute the similarity between the repo name used and the identifiers name used in it
It uses the spacy library to compute the similarity between repository name and identifiers names
Then it stores the result in repoSimilarityDetails.json file
The structure of the file is: {repo_name:similarity_score}
'''

def computeRepoSimilarity():
	repo_identifiers_similarity = []
	nlp = spacy.load("en_core_web_lg")
	with open("dataset/atomicIdentifiersName.json", 'r') as json_read_file:
		data = json.load(json_read_file)
		for repo in data:
			repo_info = {"repo_name":" ", "similarity_score":0}
			repo_info['repo_name'] = repo['repo_name']
			repo_name = repo['repo_name']
			repo_name = nlp(repo_name)

			identifiers = " ".join(repo['atomic_identifiers_name'])

			identifiers_list = nlp(identifiers)

			repo_info['similarity_score'] = repo_name.similarity(identifiers_list)

			repo_identifiers_similarity.append(repo_info)

		with open("dataset/repoSimilarityDetails.json", 'w') as json_write_file:
			json.dump(repo_identifiers_similarity, json_write_file, indent=4, sort_keys=True)

computeRepoSimilarity()
