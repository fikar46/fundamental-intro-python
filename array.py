listTest = [1, 'hi', ['hello', 2, True, [0, 1]]]
print(listTest[1]);
print(listTest[:2]);
print(listTest[2]);
print(listTest[2][1:]);
print(listTest[2][2]);
print(listTest[2][3][0]);

# x=[40,100,1,5,25,10]

x = [6000, 34, 203, 3, 746, 200, 984, 198, 764, 9, 1]
def bubbleSort(list) :
    for i in range(len(list), 0, -1) :
        for j in range(0,i-1) :
            if (list[j] > list[j + 1]) :
                temp = list[j]; 
            list[j] = list[j + 1]; 
            list[j + 1] = temp;
    return list;
print(bubbleSort(x));

y = [ 1,2,3,2,5,2,7,2 ]
def getMode(list) :
    countList = [];
    # create countList
    for num in list :
        check = False;
        for list1 in countList :
            if(list1[0] == num) :
                list1[1] += 1;
                check = True;
        if(check == False) :
            countList.append([num, 0]);
    # create list of mode/s
    maxFrequency = 0;
    modes = [];
    for list1 in countList :
        if (list1[1] > maxFrequency) :
            modes = [list1[0]];
            maxFrequency = list1[1];
        elif (list1[1] == maxFrequency) :
            modes.append(list1[0]);
    # if every value appears same amount of times
    if (len(modes) == len(countList)) :
        modes = [];
    return modes;
print(getMode(y));