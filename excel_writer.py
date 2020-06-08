import pandas as pd


def excel_writer(res):
    
    defaultColumnNames = ["Titles", "Prices", "Links"]
    df= pd.DataFrame(res).T.rename_axis('Link').reset_index()
    
    if len(df.columns) == 3: 
        df.columns = defaultColumnNames
    else:
        for i in range (len(df.columns) - 3):
            defaultColumnNames.append("Spec " + str(i))
        df.columns = defaultColumnNames
    
    #Writing them to data.xlsx file
    writer = pd.ExcelWriter('data.xlsx', engine='xlsxwriter')
    df.to_excel(writer, sheet_name="Data", index=False)
    #Setting width of data
    worksheet = writer.sheets["Data"] 
    for idx, col in enumerate(df):
        series = df[col]
        max_len = max((series.astype(str).map(len).max(),len(str(series.name))))
        worksheet.set_column(idx, idx, max_len)  # set column width
    writer.save()
