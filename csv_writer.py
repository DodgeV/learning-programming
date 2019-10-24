import csv
def creat_csv_file(path):
    head = ['name','sex','age']
    body = [('lucy','girl','14'),
            ('jack','boy','17')]
    with open(path,'w',newline='') as f:
        a = csv.writer(f)
        a.writerow(head)
        a.writerows(body)
if __name__ == '__main__':
    creat_csv_file('csvfile.csv')
