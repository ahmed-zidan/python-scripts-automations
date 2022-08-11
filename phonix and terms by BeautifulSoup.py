from unittest import result
import requests 
from bs4 import BeautifulSoup
import xlwt



path = "https://www.oxfordlearnersdictionaries.com/definition/english/"



def get_words(file_path):
    file = open(file_path , "r")
    words = file.readlines()
    return words




words = get_words("uw.txt")




wb = xlwt.Workbook()
ws = wb.add_sheet('Test Sheet')
ws.write(0,0,"Phonix")
ws.write(0,1,"Dictionary Term")
ws.write(0,2,"Word")


i = 1

for word in words:

    phonix = word
    term = word

    uWord = word[:-1].upper()
    lWord = word[:-1].lower()

    result1 = requests.get(path+uWord,headers={
    "User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
    })
    

    src1 = result1.content
    

    soup1 = BeautifulSoup(src1 , "lxml")

    phonices = soup1.find_all("span" , {"class":"phon"})
    terms = soup1.find_all("span" , {"class":"def"})

    if(len(terms) > 0):
        term = terms[0].text
    if(len(phonices) > 0):
        phonix = phonices[0].text
    else :
        result2 = requests.get(path+lWord,headers={
        "User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
        })
        src2 = result2.content
        soup2 = BeautifulSoup(src2 , "lxml")
        phonices = soup2.find_all("span" , {"class":"phon"})
        terms = soup2.find_all("span" , {"class":"def"})
        if(len(terms) > 0):
            term = terms[0].text
        if(len(phonices) > 0):
            phonix = phonices[0].text
    
    
    ws.write(i,0,phonix)
    ws.write(i,1,term)
    ws.write(i,2,word)
    wb.save('dict1.xls')
    i+=1

    





    #print(soup1)
    
    
