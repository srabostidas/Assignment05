#------------------------------------------#
# Title: CDInventory.py
# Desc: Assignment05
# Change Log: (Who, When, What)
# PDas, 2021-Feb-12, Created File
# PDas, 2021-Feb-14, Added all other code
#------------------------------------------#
# Declare variables

strChoice = '' # User input
lstTbl = []  # list of data rows to hold data
dicRow = {} 
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object

# Get user Input
print('The Magic CD Inventory\n')
while True:
    # 1. Display menu allowing the user to choose:
    print('[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit')
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()

    if strChoice == 'x':
        # 5. Exit the program if the user chooses so
        break
    if strChoice == 'l':
        # TODO Add the functionality of loading existing data
        lstTbl.clear()
        objFIle = open(strFileName, 'r')
        for row in objFile:
                lstrow = row.strip().split (',')
                dicRow = {'ID':lstrow[0], 'title':lstrow[1],'artist':lstrow[2]}
                lstTbl.append(dicRow)
        objFile.close()
        pass
    elif strChoice == 'a':  # no elif necessary, as this code is only reached if strChoice is not 'exit'
        # 2. Add data to the table (2d-list) each time the user wants to add data
        strID = input('Enter an ID: ')
        strTitle = input('Enter the CD\'s Title: ')
        strArtist = input('Enter the Artist\'s Name: ')
        intID = int(strID)
        dicRow = {'ID':intID, 'title':strTitle, 'artist':strArtist}
        lstTbl.append(dicRow)
        print()
    elif strChoice == 'i':
        # 3. Display the current data to the user each time the user wants to display the data
        print('ID, CD Title, Artist')
        for row in lstTbl:
            print(*row.values(), sep = ', ')
    elif strChoice == 'd':
        print('ID, CD Title, Artist')
        for row in lstTbl:
            print(*row.values(), sep = ', ')
        while True:
            strDelChoice = ''
            strDelChoice = input('enter ID of entry to delete, or e to exit to main menu\n')
            if strDelChoice == 'e':
                break
            else:
                for row in lstTbl:
                    if row['ID'] == int(strDelChoice):
                        lstTbl.remove(row)
                        print('entry deleted\n')
                break
        pass
    elif strChoice == 's':
        # 4. Save the data to a text file CDInventory.txt if the user chooses so
        objFile = open(strFileName, 'w')
        for row in lstTbl:
            strRow = ''
            for item in row.values():
                strRow += str(item) + ','
            strRow = strRow[:-1] + '\n'
            objFile.write(strRow)
        objFile.close()
    else:
        print('Please choose either l, a, i, d, s or x!')

