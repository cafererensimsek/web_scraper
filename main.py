def getComputerSpecs(link):
    from bs4 import BeautifulSoup
    import requests
    
    soup2 = BeautifulSoup(requests.get(link).content, 'lxml')
    
    itemSpecs = soup2.find('div', {'class': 'specs'})

    screenResolution = itemSpecs.find('span', {'class', 's10v53f3-6 geozbR'}).getText()
    coreNumber = itemSpecs.find('span', {'class': 's10v53f3-6 geozbR'}).getText()
    processorFrequency = itemSpecs.find('span', {'class': 's10v53f3-6 geozbR'}).getText()
    processorModel = itemSpecs.find('span', {'class': 's10v53f3-6 geozbR'}).getText()
    ramGb = itemSpecs.find('span', {'class', 's10v53f3-6 geozbR'}).getText()
    ramMhz = itemSpecs.find('span', {'class': 's10v53f3-6 geozbR'}).getText()
    os = itemSpecs.find('span', {'class': 's10v53f3-6 geozbR'}).getText()
    panelType = itemSpecs.find('span', {'class': 's10v53f3-6 geozbR'}).getText()

    #priceGraph = soup2.find('svg', {'class': 'rv-xy-plot__inner'})

    return screenResolution, coreNumber, processorFrequency, processorModel, ramGb, ramMhz, os, panelType






def scrapeCimri(cimri=input("Enter an item to search at cimri.com: ")):

    from bs4 import BeautifulSoup
    import requests

    resultList = []
    result = {}
    key = 0

    try:
        pageNumber = int(BeautifulSoup(requests.get("https://www.cimri.com/arama?page=1&sort=rank%2Cdesc&q=" +
                                                    cimri).content, 'lxml').findAll('a', {'class': 's1pk8cwy-2 dSbtQw'})[-1].get_text())
    except:
        pageNumber = 1

    for page in range(1, 3):
        link = "https://www.cimri.com/arama?page=" + \
            str(page) + "&sort=rank%2Cdesc&q=" + cimri

        items = BeautifulSoup(requests.get(link).content, 'lxml').findAll(
            'div', {'id': 'cimri-product'})
        for item in items:
            try:
                links = "https://www.cimri.com" + \
                    item.find('a', {'class': 'link-detail'})['href']
                price = item.find(
                    'a', {'class': 's14oa9nh-0 fFCyge'}).get_text('!').partition('!')[2]
                title = item.find('h3', {'class': 'product-title'})['title']
                #specs = getComputerSpecs(link)
                result[key] = {"title": title, "price": price, "link": links}
                resultList.append(result[key])
                key += 1
            except Exception:
                pass

    return resultList


def excel_writer(res):
    import pandas as pd
    
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


excel_writer(scrapeCimri())
