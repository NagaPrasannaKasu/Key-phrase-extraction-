# Key-phrase-extraction-
keyword/keyphrase extraction using BERT embedding
With the help of KeyBERT embeddings we can also get keyphrases other than keywords. These keyphrases, make more effecient in identifying the document.

Remark: I have processed with only few data from the given sample data due to slow machine in my house, the source code can also process on hundreds of millions of documents

Requirements:
Visualstudio code
Extensions: Python 3.9 , SQLite3 version 3.37.2
Libraries: Keybert (>pip install keybert), pandas, zipfile
keybert[all] - for all backends (>pip install keybert[all])


About Task:
- patent folders are changed from .tgz to .zip file formate for my convenient
- implemented Python code and started key phrase extraction directly from the .zip folder
- performed key phrase extraction on 'Abstract' and 'Title' of each patent 
- used KeyBERT embeddings in order to extract key phrases 
-- extracted key phrases in ngram range of (1,3) for 'Abstract' 
-- and extracted key phrases in ngram range of (1,2) for 'invention-title'

- with the help of key phrases, identified related documents and 
- stored few key phrases and identified documents into .xml files
- stored all key phrases and documents that were identified into the Database 'Abstract_keyphras_extraction.db'

Docker:
- tried to run the source code in Docker container, issued with the error: ModuleNotFoundError: No module named 'keybert'
- related docker files were also added 
