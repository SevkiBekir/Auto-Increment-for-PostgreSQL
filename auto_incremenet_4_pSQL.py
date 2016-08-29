##########################################################
# Coded by Sevki Bekir
# Date: August 26, 2016
# Defn: This helps to be auto increment for PostgreSQL
#       change your input file location below.
# Ex:   Look at filename.txt 
##########################################################
inputFile='/Users/SBK/Desktop/filename.txt'
outputFile='/Users/SBK/Desktop/output.sql'
schemeName="\"eLearningProject\""

file=open(outputFile,"w")
#file.write("Let's start")


with open(inputFile) as fp:
    for line in fp:
        #print line
        line=line[1:]
        line=line[:-2]
        comment="/* ###\tTABLE:"+line+"\t###*/\n"
        file.write(comment)
        query="CREATE SEQUENCE "+line+"_id_seq;\n"
        query=query+"ALTER TABLE "+schemeName+".\""+line+ "\" ALTER id SET DEFAULT NEXTVAL(\'"+line+"_id_seq');\n\n\n"
        #print query;
        file.write(query)
