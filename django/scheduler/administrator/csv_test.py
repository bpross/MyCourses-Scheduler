if __name__ == '__main__':
    import csv
    file = open("/Users/esteggall/Scheduler/django/scheduler/administrator/testcsvfile.txt")
    testReader = csv.reader(file,delimiter = ' ', quotechar = '|')
    for row in testReader:
        print row
