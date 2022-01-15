# Key-phrase-extraction-
keyword/keyphrase extraction using BERT embedding


Requirements:
Visualstudio code
Extensions: Python, SQLite3
Libraries: Keybert (>pip install keybert), pandas
keybert[all] - for all backends


About Task:
all patent folders are added into .zip file
implemented Python code and started key phrase extraction directly from the .zip folder
focused on key phrase extraction on the 'Title' of each patent and 'Abstract' of each patent
used KeyBERT embedding in order to extract key phrases 
- extracted key phrases in ngram range of (1,3) for 'Abstract' of each patent
- and extracted key phrases in ngram range of (1,2) for 'invention-title'

- stored key phrases into title_keyphrases.xml/abstract_keyphrases.xml files and at the same time stores into the Database
- with the help of key phrases that were stored into the abstract_keyphrases.xml file, identified related document and document names are stored into abstract_identifiers.xml and at the same time stored into the Database

With the help of KeyBERT embeddings we can also get keyphrases other than keywords. These keyphrases, make more effecient in identifying the document.
