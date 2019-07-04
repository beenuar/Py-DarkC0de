# -*- coding: utf-8 -*-

import pandas as pd

# To extract fundamental data
from bs4 import BeautifulSoup as bs
import requests


#Define The Method To Extract Fundamental Data


def get_fundamental_data(df):
    for symbol in df.index:
        
            url = ("http://finviz.com/quote.ashx?t=" + symbol.lower())
            soup = bs(requests.get(url).content, features='html5lib') 
            for m in df.columns:                
                try:
                    df.loc[symbol,m] = fundamental_metric(soup,m)                
                except Exception as e:
                    print(symbol, 'not found')
                    print(e)
                    break        
    return df


def fundamental_metric(soup, metric):
    return soup.find(text = metric).find_next(class_='snapshot-td2').text


#Define A List Of Stocks And The Fundamental Metrics

stock_list = ['AMZN','GOOG', 'MSFT', 'WMT', 'AAPL', 'FOX']
num = len(stock_list)
metric = ['P/B',
'P/E',
'Forward P/E',
'PEG',
'Debt/Eq',
'EPS (ttm)',
'Dividend %',
'ROE',
'ROI',
'EPS Q/Q',
'Insider Own'
]

df = pd.DataFrame(index=stock_list,columns=metric)
df = get_fundamental_data(df)
print("\n\n Gathering companies with fundamental data..\n")

print(df.head(num))

print "\n\n[+] Assessing security analysis per Benjamin Graham principals"

for index, row in df.iterrows():
	print "[+] Analysing :" +str(index)
	try:
		if (float(row['P/E'])< 20) & (float(row ['P/B']) <3):
			print "\t[-] Rule 1: The business is listed at low valuations"
		else:
			print "\t[-] Rule 1: The business isn't valued low"
	except:
		print "\t[-] Rule 1: Can't comment on the business valuations"
		pass
	try:
		if (float(row['EPS Q/Q'][:-1])/100 > 0.1):
			print "\t[-] Rule 2: The business has demonstrated earning power"
		else:
			print "\t[-] Rule 2: The business hasn't demonstrated earning power"
	except:
		print "\t[-] Rule 2: Can't comment on the business earning power"
		pass
		
	try:
		if (float(row['Debt/Eq'])< 1) & (float(row['ROE'][:-1])/100 > 0.1):
			print "\t[-] Rule 3: The business has good returns while employing little or no debt"
		else:
			print "\t[-] Rule 3: The business hasn't got good returns while employing little or no debt"
	except:
		print "\t[-] Rule 3: Can't comment if the business has good returns while employing little or no debt"
		pass
		
	try:
		if (float(row['Insider Own'][:-1])/100 > 0.3):
			print "\t[-] Rule 4: The management has over 30% ownership"
		else:
			print "\t[-] Rule 4: The management hasn't got over 30% ownership"
	except:
		print "\t[-] Rule 4: Can't determine if management has over 30% ownership"
		pass
	
	try:
		health_index = (float(row['P/E'])) * (float(row ['P/B']))
		print "\t[-] The Health Index is: "+str(health_index)+". Higher the better"
	except:
		print "\t[-] Can't determine the Health index"
		pass
	
# #1. Businesses which are quoted at low valuations
# #P/E < 20
# #P/B < 3

# df = df[(df['P/E'].astype(float)<20) & (df['P/B'].astype(float) < 3)]

# #2. Businesses which have demonstrated earning power
# #EPS Q/Q > 10%

# df['EPS Q/Q'] = df['EPS Q/Q'].map(lambda x: x[:-1])
# df = df[df['EPS Q/Q'].astype(float) > 10]

# #3. Businesses earning good returns on equity while employing little or no debt
# #Debt/Eq < 1
# #ROE > 10%

# df['ROE'] = df['ROE'].map(lambda x: x[:-1])
# df = df[(df['Debt/Eq'].astype(float) < 1) & (df['ROE'].astype(float) > 10)]

# #4. Management having substantial ownership in the business
# #Insider own > 30%

# df['Insider Own'] = df['Insider Own'].map(lambda x: x[:-1])
# df = df[df['Insider Own'].astype(float) > 30]