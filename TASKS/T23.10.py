import pandas
from pandas.tseries.offsets import Second

first = pandas.read_excel('T23.10.xlsx')

projects = list(set(first['Project']))


second = []
for project in projects:
    project_people = list(set(first[first['Project'] == project]['Person']))
    for i in range(len(project_people)):
        for j in range(i+1, len(project_people)):
            second.append([project_people[i], project_people[j], project])
second = pandas.DataFrame(second)
second.columns = ['Person1', 'Person2', 'Project']

writer = pandas.ExcelWriter('T23.10_rez.xlsx')

first.to_excel(writer, sheet_name='First', index=False)
second.to_excel(writer, sheet_name='Second', index=False)

writer.save()