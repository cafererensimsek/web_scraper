def scrapeCimri(cimri = input("Enter an item to search at cimri.com: ")):

    from bs4 import BeautifulSoup
    import requests
    import pandas as pd
    import pyrebase
    

    resultList = []
    result = {}
    key = 0

    try:
        pageNumber = int(BeautifulSoup(requests.get("https://www.cimri.com/arama?page=1&sort=rank%2Cdesc&q=" + cimri).content, 'lxml').findAll('a', {'class': 's1pk8cwy-2 dSbtQw'})[-1].get_text())
    except:
        pageNumber = 1

    for page in range(1, int(pageNumber)):
        link = "https://www.cimri.com/arama?page=" + str(page) + "&sort=rank%2Cdesc&q=" + cimri

        items = BeautifulSoup(requests.get(link).content, 'lxml').findAll('div', {'id': 'cimri-product'})
        for item in items:
            try:
                links = "https://www.cimri.com" + item.find('a', {'class': 'link-detail'})['href']
                price = item.find('a', {'class': 's14oa9nh-0 fFCyge'}).get_text('!').partition('!')[2]
                title = item.find('h3', {'class': 'product-title'})['title']
                #specs = getComputerSpecs(link)
                result[key] = {"title": title, "price": price, "link": links}
                resultList.append(result[key])
                key += 1
            except Exception:
                pass

    
    firebase = pyrebase.initialize_app(config)
    db = firebase.database()
    db.remove
    db.update(result)
<<<<<<< HEAD


scrapeCimri()
=======
    return jsonify(resultList)
    
if __name__ == '__main__':
    app.run()
>>>>>>> c61cfd2a3c5302c002a0716abd6b64ef411fbf36
