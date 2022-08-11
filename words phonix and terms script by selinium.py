
from selenium import webdriver
import time

import xlwt


"""
you should these first for run code:

1- open cmd and write (pip install selenium)
2- open cmd and write (pip install xlwt)
3- download chrome driver from this link (https://chromedriver.chromium.org/downloads) you should download the same version of chrome you have
4- change "chromeLocationFile" as specefied in code 



"""
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# ----------   change that path ----------- 
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1111
chromeLocationFile = "D:\Ahmed Zeedan\programs\chrom driver 103.5060/chromedriver.exe"


#google dictionary
url = "https://translate.google.com/?sl=en"

driver = webdriver.Chrome(chromeLocationFile)



terms = []
phonics = []


def get_words(file_path):
    file = open(file_path , "r")
    words = file.readlines()
    return words



# get words from text file
#words = get_words("WordList_ENG.txt")

words = get_words("D:\Ahmed Zeedan\work\create unlimited gmails\iles\w3.txt")



def git_phonix_and_term(word):
        time.sleep(1)
        
        driver.find_element("xpath",'//*[@class="er8xn"]').send_keys(word)
        time.sleep(1)
        term = ""
        phonix = ""
        try:
            term = driver.find_element("xpath",'//*[@class="fw3eif"]').get_attribute("innerHTML")
            
            phonix = driver.find_element("xpath",'//*[@class="kO6q6e"]').get_attribute("innerHTML")
            
        except :
            if term =="":
                term = word
            if phonix == "":
                phonix = word
        return term , phonix





# iters = 0
for word in words:
    # iters+=1
    # if iters == 20:
    #     break
    driver.get(url)
    term , phonix = git_phonix_and_term(word.lower()[:-1])
    terms.append(term)
    phonics.append(phonix)
    print("*"*200)
    print(phonix)
    print(term)

driver.close()


print(terms)
print(phonics)

# file_list = [phonixes,terms]

# exported = zip_longest(*file_list)

# with open("dictionary.csv" , "w", encoding="utf-8") as file:
#     wr = csv.writer(file)
#     wr.writerow(["Phonics" , "Dictionary Term"])
#     wr.writerows(exported)



wb = xlwt.Workbook()
ws = wb.add_sheet('Test Sheet')
lte = u'\u2264'
gte = u'\u2265'
ws.write(0,0,"Phonics")
ws.write(0,1,"Dictionary Term")

for i in range(0 , len(phonics)):
    ws.write(i+1,0,phonics[i])
    ws.write(i+1,1,terms[i])


wb.save('dict3.xls')
