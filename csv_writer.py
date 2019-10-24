import csv
def creat_csv_file(path):
    head = ['name','sex','age']
    body = [('lucy','girl','14'),
            ('jack','boy','17')]
    with open(path,'w',newline='') as f: #指定newline=‘’，可以防止向文件中写入空行
        a = csv.writer(f)
        a.writerow(head)
        a.writerows(body)
if __name__ == '__main__':
    creat_csv_file('csvfile.csv')
