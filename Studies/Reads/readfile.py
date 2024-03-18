from io import StringIO

#Paths
pathIN = "I:\\IVALIX\\TXT\\artesanart\\dados\\in\\"
pathOUT = "I:\\IVALIX\\TXT\\artesanart\\dados\\in\\"
marker = "ARTESANART"
makerlen = 0
#Features File
filein = pathIN + 'input.txt'
fileout = pathOUT + 'output-test.txt'

head = "iddoc;page;competence;company;idcompany;doc1company;idemployee;employee;typesalary;doc1employee;doc2employee;doc3employee;cbo;cc;idpost;post;department"
detail = "cod;description;ref;credit;debit"
totals = "credit;debit;liquid"
footer = "salarybase;baseinss;basefgts;fgtsmonth;baseir;bandir;depir;bank,bankagency;bankaccount"

# File adjustments
with open (filein, 'r') as file:
    filein.replace("","")

# Len marker

makerlen = marker
makerlen.find(marker)
print('Teste', makerlen)

#Read file
with open (filein, 'r') as file:
    
    #look for patterns
    countmarkers = 0
    for file in filein:
        file = file.strip().upper()
        #print(file)
        if file.find(marker) != -1 and len (file) == makerlen:
            countmarkers = countmarkers +1
            
        #else:
        #    print('No Docs in file!')
        
    print('there are ', countmarkers, 'documents')
    
    #competence = file.readlines()[3] + file.readline()[40:60]
    countregisters = countmarkers
    competence = ("JUNHO/2021")
    company = file.readline()[:39]
    localcompany = file.readline()[:60]
    doc1company = file.readline()[:18]
    
print(countregisters, company, localcompany, doc1company)

with open (fileout, 'w') as file:
    
    headcsv = head +';'+ detail +';'+ totals +';'+ footer
    datadoc = countregisters, +';'+ competence +';'+ company +';'+ localcompany +';'+ doc1company
    file.write(headcsv + "\n") 
    file.write(datadoc)

