import itertools

import pandas as pd

EXCEL_FILE = 'sheet_sample.xlsx'


if __name__ == '__main__':

    file = EXCEL_FILE
    xl = pd.ExcelFile(file, engine='openpyxl')
    print(xl.sheet_names)
    df1 = xl.parse('Sheet1')
    names = list(itertools.combinations(df1['Person'], 2))
    Persons1 = []
    Persons2 = []
    Projects = []
    Weights = []
    for name_tuple in names:
        select_df = df1.loc[(df1['Person'] == name_tuple[0]) & (df1['Person'] == name_tuple[1])]
        select_df['Project'].tolist()

        Persons1.append(name_tuple[0])
        Persons2.append(name_tuple[1])
        Projects.append("_".join(select_df['Project'].tolist()))
        Weights.append(len(select_df['Project'].tolist()))

    data = {
        'Person1': Persons1,
        'Person2': Persons2,
        'Projects': Projects,
        'Weight': Weights
    }

    df = pd.DataFrame(data)

    writer = pd.ExcelWriter(EXCEL_FILE, engine='openpyxl')

    df1.to_excel(writer, 'Sheet1', index=False)
    df.to_excel(writer, 'Sheet2', index=False)
    writer.save()
