import csv
def get_content(path):
    with open(path,'r',newline = '') as f:
        headers = next(csv.reader(f))
        print(headers)
        for i in csv.reader(f):
            print(i)
if __name__ == '__main__':
    get_content(r'csvfile.csv')
