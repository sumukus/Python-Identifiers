# Python-Identifiers
This is my first attempt to carry out the empirical study on python identifiers. I wanted to know how the identifiers name are used in the python code. What are the different lenghts of identifiers name used in python code? Is there any relevence between the repository name and the identifiers name used inside the repository? By the end of the work I wanted to have a dataset of python identifiers name which can be used by other researcher.

# Dependencies Installation
I have used spiral and spacy python3 package for my work.

## 1. Spiral
I have used spiral package for splitting the identifiers name. It is written in python3.
It can be access from the github repository called [spiral](https://github.com/casics/spiral)

### The quick installtion is as follows
<pre>
git clone https://github.com/casics/spiral.git
cd spiral
sudo python3 -m pip install .
</pre>

## 2. Spacy
I have used spacy package for computing the similarity between the two list of texts. 
The builtin model I have used from the spacy package is called **en_core_web_lg**.
The some of other prebuilt models are as follows:
* *en_core_web_sm*
* *en_core_web_md*
The more documentaton on spacy can be found at [spacy website](https://spacy.io/models)
### The quick installtion is as follows
<pre>
pip3 install spacy
python3 -m spacy download en_core_web_lg
</pre>

# Research Questions
The some of the research questions that I wanted to address are as follows:\
**RQ1) How well does my system download the relevant project from the github repository?**
**RQ2) To what degree different length identifier names are used in python source code?**
**RQ3) Is there any relevance between the identifier name used and the name of the python project repository in the github?**


 
