from bs4 import BeautifulSoup
from requests import get
import pandas as pd 
import itertools 
import matplotlib.pyplot as plt 
import seaborn as sns
sns.set() 

headers = ({'User-Agent':
            'Mozilla/5.0 (Windows Nt 6.1) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/41.0.0.2228.0 Safari/537.36'})

zillow = 'https://www.zillow.com/homes/for_rent/Los-Angeles,-CA_rb/'
response = get(zillow, headers=headers)

print('\n{}\n'.format(response))
