import csv

def main():
    my_list = list();
    
    with open("Destinations.csv") as file:
    	my_list.append(file.read().splitlines())

    for s in my_list:
        print s


if __name__ == '__main__':
    main()
