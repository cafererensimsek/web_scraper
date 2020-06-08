from bs4 import BeautifulSoup
import requests


def getComputerSpecs(link):
    
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