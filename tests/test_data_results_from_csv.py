import csv
    
def test_dataFromCSV():
    data =[]    #define an empty list to store data from csv file
    with open("testData\\credentials.csv") as csvFile:
        dataInCsv = csv.DictReader(csvFile)  #Read data inside csv file
        for row in dataInCsv:       # for reading data from csv file, we need to convert it into rows and then read it
            data.append(row)        #append will add each row into data list
    
    print("all the data of csv is ", data)
    print("first row data of csv is ", data[0])     
    print("username from first row is ", data[0]["username"])  #username is the key in csv file

    



    


