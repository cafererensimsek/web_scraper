from bs4 import BeautifulSoup
import requests
import pandas as pd



cimri = input("Enter an item to search at cimri.com: ")

""" input_computer = input("Are you searching for a laptop? (y/n): ").capitalize()

is_computer = None

while is_computer == None:
    if input_computer == 'Y':
        is_computer = True
    elif input_computer == 'N':
        is_computer = False
    else:
        print('Invalid input!')



def getComputerSpecs(link):

    soup2 = BeautifulSoup(requests.get(link).content, 'lxml')

    itemSpecs = soup2.find('div', {'class': 's10v53f3-0 bfgzQt'})

    screenResolution = itemSpecs.find(
        'span', {'class', 's10v53f3-6 geozbR'}).getText()
    coreNumber = itemSpecs.find(
        'span', {'class': 's10v53f3-6 geozbR'}).getText()
    processorFrequency = itemSpecs.find(
        'span', {'class': 's10v53f3-6 geozbR'}).getText()
    processorModel = itemSpecs.find(
        'span', {'class': 's10v53f3-6 geozbR'}).getText()
    ramGb = itemSpecs.find('span', {'class', 's10v53f3-6 geozbR'}).getText()
    ramMhz = itemSpecs.find('span', {'class': 's10v53f3-6 geozbR'}).getText()
    os = itemSpecs.find('span', {'class': 's10v53f3-6 geozbR'}).getText()
    panelType = itemSpecs.find(
        'span', {'class': 's10v53f3-6 geozbR'}).getText()

    #priceGraph = soup2.find('svg', {'class': 'rv-xy-plot__inner'})

    return screenResolution, coreNumber, processorFrequency, processorModel, ramGb, ramMhz, os, panelType


def scrapeCimriLaptop(cimri):
    resultList = []
    result = {}
    key = 0

    try:
        pageNumber = int(BeautifulSoup(requests.get("https://www.cimri.com/arama?page=1&sort=rank%2Cdesc&q=" +
                                                    cimri).content, 'lxml').findAll('a', {'class': 's1pk8cwy-2 dSbtQw'})[-1].get_text())
    except:
        pageNumber = 1

    for page in range(1, pageNumber):
        link = "https://www.cimri.com/arama?page=" + \
            str(page) + "&sort=rank%2Cdesc&q=" + cimri

        items = BeautifulSoup(requests.get(link).content, 'lxml').findAll(
            'div', {'id': 'cimri-product'})
        for item in items:
            try:
                link = "https://www.cimri.com" + \
                    item.find('a', {'class': 'link-detail'})['href']
                price = item.find(
                    'a', {'class': 's14oa9nh-0 fFCyge'}).get_text('!').partition('!')[2]
                title = item.find('h3', {'class': 'product-title'})['title']
                specs = getComputerSpecs(link)
                result[key] = {"title": title, "price": price,
                               "link": link, "specs": specs}
                resultList.append(result[key])
                key += 1
            except Exception as e:
                print(str(e))
                pass

    return resultList
"""

def scrape(cimri):
    resultList = []
    result = {}
    key = 0

    try:
        pageNumber = int(BeautifulSoup(requests.get("https://www.cimri.com/arama?page=1&sort=rank%2Cdesc&q=" +
                                                    cimri).content, 'lxml').findAll('a', {'class': 's1pk8cwy-2 dSbtQw'})[-1].get_text())
    except:
        pageNumber = 1

    for page in range(1, pageNumber):
        link = "https://www.cimri.com/arama?page=" + \
            str(page) + "&sort=rank%2Cdesc&q=" + cimri

        items = BeautifulSoup(requests.get(link).content, 'lxml').findAll(
            'div', {'id': 'cimri-product'})
        for item in items:
            try:
                link = "https://www.cimri.com" + \
                    item.find('a', {'class': 'link-detail'})['href']
                price = item.find(
                    'a', {'class': 's14oa9nh-0 fFCyge'}).get_text('!').partition('!')[2]
                title = item.find('h3', {'class': 'product-title'})['title']
                result[key] = {"title": title, "price": price, "link": link}
                resultList.append(result[key])
                key += 1
            except Exception as e:
                print(str(e))
                pass

    return resultList

def writeres):
    

    defaultColumnNames = ["Titles", "Prices", "Links"]
    df = pd.DataFrame(res).T.rename_axis('Link').reset_index()

    if len(df.columns) == 3:
        df.columns = defaultColumnNames
    else:
        for i in range(len(df.columns) - 3):
            defaultColumnNames.append("Spec " + str(i))
        df.columns = defaultColumnNames

    # Writing them to data.xlsx file
    writer = pd.ExcelWriter('data.xlsx', engine='xlsxwriter')
    df.to_excel(writer, sheet_name="Data", index=False)
    # Setting width of data
    worksheet = writer.sheets["Data"]
    for idx, col in enumerate(df):
        series = df[col]
        max_len = max((series.astype(str).map(
            len).max(), len(str(series.name))))
        worksheet.set_column(idx, idx, max_len)  # set column width
    writer.save()



""" if is_computer:
    print(scrapeCimriLaptop(cimri = cimri))
else:
    print(scrapeCimri(cimri = cimri))
 """


write(scrape(cimri = cimri))