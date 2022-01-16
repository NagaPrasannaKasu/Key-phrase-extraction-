import xml.etree.ElementTree as ET
import keybert
#from keybert import KeyBERT
from zipfile import ZipFile
import sqlite3
import pandas as pd


file_name = 'ongoing_120001_140000.zip'

t = ZipFile(file_name)
xml_fileslist = t.namelist()

#key phrase extraction on the 'Title' of each patent
file_count=1
for i in xml_fileslist:
    file_count=file_count+1
    if file_count < len(xml_fileslist): 
        xmlfile_1 = xml_fileslist[file_count]    
        xml_data = ET.parse(xmlfile_1)
        root = xml_data.getroot()
        for x in root[0].findall('invention-title'):   
            title = x.text
            kw_bert = keybert.KeyBERT()
            keywords = kw_bert.extract_keywords(title, keyphrase_ngram_range=(1, 2))
            """ keyphrase_file = 'title_keyphrases.xml'
            extracted_keywords_file = open(keyphrase_file, 'a')
            print(keywords, file=extracted_keywords_file)                    
            extracted_keywords_file.close()   """
        for j in keywords:              
            str =  x.text.lower()
            if j[0] in str:                
                """ document_identifiers ='title_identifier.xml'            
                output_file = open(document_identifiers, 'a') 
                print("key Phrases: "+j[0]+" <==> Title text: "+title+" Document identified: "+xmlfile_1, file=output_file)  
                output_file.close() """
                
                _dict_ = {    
                "Key_Phrases" : j[0],
                "Title_text" : title,
                "Document_identified" : xmlfile_1 }
                _df_ = pd.DataFrame(_dict_, index=[0]) 
                connection = sqlite3.connect('Titles_Keyphrase_extraction.db')
                cursor = connection.cursor()
                command1 = """Create Table if not exists Titles_keyphrases_list(Key_Phrases VARCHAR(300), Title_text VARCHAR(300), Document_identified VARCHAR(300))""" 
                cursor.execute(command1)  
                _df_.to_sql("Titles_keyphrases_list", connection, index=False, if_exists='append')                
                connection.close()
    else:
        break   

print("close database succesfully...")                      

 

#key phrase extraction on the 'Abstract' of each patent
count=1
for k in xml_fileslist:
    count=count+1
    if count < len(xml_fileslist):
        xmlfile_1_ = xml_fileslist[count]    
        xml_data = ET.parse(xmlfile_1_)        
        root = xml_data.getroot()        
        for x in root.findall('./abstract'):               
            abstract = (" ".join(x.itertext())) 
            print(abstract)
            kw_bert = keybert.KeyBERT()
            _keywords_ = kw_bert.extract_keywords(abstract, keyphrase_ngram_range=(1, 3))
            """ keyphrase_file = 'abstract_keyphrases.xml'
            abstract_keywords_file = open(keyphrase_file, 'a')
            print(_keywords_, file=abstract_keywords_file)                    
            abstract_keywords_file.close()  """ 
            for l in _keywords_:                          
                if l[0] in abstract:                
                    #document_identifiers ='abstract_identifiers.xml'            
                    #output_file1 = open(document_identifiers, 'a')                
                    #print("key Phrases: "+l[0]+" <==> Abstract text: "+abstract+" Document identified: "+xmlfile_1_, file=output_file1)     
                    #output_file1.close()                   
                    
                    _dict_ = {    
                    "Key_Phrases" : l[0],
                    "Abstract_text" : abstract,
                    "Document_identified" : xmlfile_1_ }
                    _df = pd.DataFrame(_dict_, index=[0]) 
                    connection = sqlite3.connect('Abstract_Keyphrase_extraction.db')
                    cursor = connection.cursor()                
                    command1 = """Create Table if not exists Abstract_keyphrases_list(Key_Phrases VARCHAR(300), Abstract_text VARCHAR(300), Document_identified VARCHAR(300))""" 
                    cursor.execute(command1)                    
                    _df.to_sql("Abstract_keyphrases_list", connection, index=False, if_exists='append')
                    connection.close()
    else:
        break   
    
print("close database succesfully...")

