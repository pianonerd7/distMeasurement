import csv

class Trace :
    my_list = list();
    
    with open('Destinations.csv', "r") as f:
        my_list.insert(f.readline())

    for s in my_list:
        print s

    print len(my_list)
    print "hi"
