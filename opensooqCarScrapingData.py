linkscar, city, n, Brand, Brand_child, Car_Year, regional_specs, Tramsmission_Cars, Fuel_Cars, Car_Color, ConditionUsed, Kilometers_Cars, paint, body_condition, CarCustoms, CarLicense, CarInsurance, Payment_Method, additions, price = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup
from itertools import zip_longest
#795 page

def getinfo(tag, fet, name,intq=0):
    Cars = soup.find_all(tag, {fet:name})
    if len(Cars)==0:
        Cars = np.NaN
    else:
        x = str(Cars[intq].text.replace('  ','').replace('\n',''))
        s = int(x.find(':'))
        Cars = x[s+1:]
    return Cars

# 485
for page in range(796,801):
    if page ==1:
        link = 'https://jo.opensooq.com/ar/%D8%B9%D9%85%D8%A7%D9%86/%D8%B3%D9%8A%D8%A7%D8%B1%D8%A7%D8%AA-%D9%88%D9%85%D8%B1%D9%83%D8%A8%D8%A7%D8%AA/%D8%B3%D9%8A%D8%A7%D8%B1%D8%A7%D8%AA-%D9%84%D9%84%D8%A8%D9%8A%D8%B9'
    else:
        link = f'https://jo.opensooq.com/ar/%D8%B9%D9%85%D8%A7%D9%86/%D8%B3%D9%8A%D8%A7%D8%B1%D8%A7%D8%AA-%D9%88%D9%85%D8%B1%D9%83%D8%A8%D8%A7%D8%AA/%D8%B3%D9%8A%D8%A7%D8%B1%D8%A7%D8%AA-%D9%84%D9%84%D8%A8%D9%8A%D8%B9?page={page}'
    result = requests.get(link)
    src = result.content
    soup = BeautifulSoup(src, "lxml")
    a = soup.find_all('a', {"class":"block postLink notEg postSpanTitle noEmojiText"},href=True)
    for i in a:
        x = 'https://jo.opensooq.com'+i['href']
        result = requests.get(x)
        src = result.content
        soup = BeautifulSoup(src, "lxml")
        price1 = soup.find_all('strong', {"class":"priceCurrencyMiddle"})
        city.append(getinfo('li', "class", "inline vTop relative mb15"))
        linkscar.append(x)
        n.append(getinfo('li', "class", "inline vTop relative mb15",1))
        Brand.append(getinfo('li', "data-icon", "PostDynamicAttribute[Brand]"))
        Brand_child.append(getinfo('li', "data-icon", "PostDynamicAttribute[Brand_child]"))
        Car_Year.append(getinfo('li', "data-icon", "PostDynamicAttribute[Car_Year]"))
        regional_specs.append(getinfo('li', "data-icon", "PostDynamicAttribute[regional_specs]"))
        Tramsmission_Cars.append(getinfo('li', "data-icon", "PostDynamicAttribute[Tramsmission_Cars]"))
        Fuel_Cars.append(getinfo('li', "data-icon", "PostDynamicAttribute[Fuel_Cars]"))
        Car_Color.append(getinfo('li', "data-icon", "PostDynamicAttribute[Car_Color]"))
        ConditionUsed.append(getinfo('li', "data-icon", "PostDynamicAttribute[ConditionUsed]"))
        Kilometers_Cars.append(getinfo('li', "data-icon", "PostDynamicAttribute[Kilometers_Cars]"))
        paint.append(getinfo('li', "data-icon", "PostDynamicAttribute[paint]"))
        body_condition.append(getinfo('li', "data-icon", "PostDynamicAttribute[body_condition]"))
        CarCustoms.append(getinfo('li', "data-icon", "PostDynamicAttribute[CarCustoms]"))
        CarLicense.append(getinfo('li', "data-icon", "PostDynamicAttribute[CarLicense]"))
        CarInsurance.append(getinfo('li', "data-icon", "PostDynamicAttribute[CarInsurance]"))
        Payment_Method.append(getinfo('li', "data-icon", "PostDynamicAttribute[Payment_Method]"))
        if len(price1)==0 or price1=='0.00':
            price.append(np.NaN)
        else:
            price.append(float(price1[0].text.replace(',','')))
        additions.append(list([i.text for i in soup.find_all('li', {"class":["fRight mb15", 'fRight mb15 latestParam']})]))
        # des.append(soup.find_all('div', {'class': 'albumDet clear'})[0].text)
        print(x)
        print(f'======= Done... Scraping page {page} =========\n\n')
data = {'linkscar':linkscar, 'city': city, 'place':n, 'Brand':Brand, 'Brand_child':Brand_child, 'Car_Year':Car_Year, 'regional_specs':regional_specs, 'Tramsmission_Cars':Tramsmission_Cars, 'Fuel_Cars':Fuel_Cars, 'Car_Color':Car_Color, 'ConditionUsed':ConditionUsed, 'Kilometers_Cars':Kilometers_Cars, 'paint':paint, 'body_condition':body_condition, 'CarCustoms':CarCustoms, 'CarLicense':CarLicense, 'CarInsurance':CarInsurance, 'Payment_Method':Payment_Method, 'additions':additions, 'price':price}
mydf = pd.DataFrame(data)
mydf.to_json('dataopensooq.json')