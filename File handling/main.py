import csv
def get_emp_sal_more_than(file_name, sal):
    file = open(file_name)
    records = []
    reader_obj = csv.reader(file)
    next(reader_obj)
    for record in reader_obj:
        salary = record[5]
        if int(salary) > sal:
            records.append(sal)
    file.close()
    return records
print(get_emp_sal_more_than("emp_log.csv", 1000))