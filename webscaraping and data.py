!pip install pandas, numpy
!pip install lxml

import pandas as pd
def warn(*arg, **kwarg):
  pass

import warning
warnings.warn = warn
warinigs.filterwarning('ignore')

#extracting the required GDP data from the given URL using Web Scraping.


URL="https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29"
import requests
import pandas as pd
GDP_data = requests.get(URL).text #from URL extracting all data


""" output 
'<!DOCTYPE html>\n<html class="client-nojs vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-sticky-header-disabled 
vector-feature-page-tools-pinned-disabled vector-feature-toc-pinned-enabled vector-feature-main-menu-pinned-disabled vector-feature-limited-width-clientpref-1 
vector-feature-limited-width-content-enabled vector-feature-zebra-design-disabled vector-feature-custom-font-size-clientpref-disabled" 
lang="en" dir="ltr">\n<head><script type="text/javascript" src="https://web-static.archive.org/_static/js/bundle-playback.js?v=2N_sDSC0" charset="utf-8">....................
"""

# extracting tables from webpage using Pandas. Retain table number 3 as the required dataframe.
#method 1
tables = pd.read_html(StringIO(GDP_data))

df  =tables[2]
df

"""#method 2
tables = pd.read_html(URl)

df = tables [3]
df
{O/p =  	Country/Territory 	UN region 	IMF[1][13] 	World Bank[14] 	United Nations[15]
	Country/Territory 	UN region 	Estimate 	Year 	Estimate 	Year 	Estimate 	Year
0 	World 	— 	105568776 	2023 	100562011 	2022 	96698005 	2021
1 	United States 	Americas 	26854599 	2023 	25462700 	2022 	23315081 	2021
2 	China 	Asia 	19373586 	[n 1]2023 	17963171 	[n 3]2022 	17734131 	[n 1]2021
3 	Japan 	Asia 	4409738 	2023 	4231141 	2022 	4940878 	2021
4 	Germany 	Europe 	4308854 	2023 	4072192 	2022 	4259935 	2021
... 	... 	... 	... 	... 	... 	... 	... 	...
209 	Anguilla 	Americas 	— 	— 	— 	— 	303 	2021
210 	Kiribati 	Oceania 	248 	2023 	223 	2022 	227 	2021
211 	Nauru 	Oceania 	151 	2023 	151 	2022 	155 	2021
212 	Montserrat 	Americas 	— 	— 	— 	— 	72 	2021
213 	Tuvalu 	Oceania 	65 	2023 	60 	2022 	60 	2021}"""

214 rows × 8 columns

# Replace the column headers with column numbers
df.columns = range(df.shape[1])
df

"""{ o/p:  	0 	1 	2 	3 	4 	5 	6 	7
0 	World 	— 	105568776 	2023 	100562011 	2022 	96698005 	2021
1 	United States 	Americas 	26854599 	2023 	25462700 	2022 	23315081 	2021
2 	China 	Asia 	19373586 	[n 1]2023 	17963171 	[n 3]2022 	17734131 	[n 1]2021
3 	Japan 	Asia 	4409738 	2023 	4231141 	2022 	4940878 	2021
4 	Germany 	Europe 	4308854 	2023 	4072192 	2022 	4259935 	2021
... 	... 	... 	... 	... 	... 	... 	... 	...
209 	Anguilla 	Americas 	— 	— 	— 	— 	303 	2021
210 	Kiribati 	Oceania 	248 	2023 	223 	2022 	227 	2021
211 	Nauru 	Oceania 	151 	2023 	151 	2022 	155 	2021
212 	Montserrat 	Americas 	— 	— 	— 	— 	72 	2021
213 	Tuvalu 	Oceania 	65 	2023 	60 	2022 	60 	2021

214 rows × 8 columns

}"""
# Retain columns with index 0 and 2 (name of country and value of GDP quoted by IMF)
df = df[[0,2]]

"""{ 
 	0 	2
0 	World 	105568776
1 	United States 	26854599
2 	China 	19373586
3 	Japan 	4409738
4 	Germany 	4308854
... 	... 	...
209 	Anguilla 	—
210 	Kiribati 	248
211 	Nauru 	151
212 	Montserrat 	—
213 	Tuvalu 	65

214 rows × 2 columns
} """

# Retain the Rows with index 1 to 10, indicating the top 10 economies of the world.
df = df.iloc[1:11, :]

"""{
   	 	0 	2
1 	United States 	26854599
2 	China 	19373586
3 	Japan 	4409738
4 	Germany 	4308854
5 	India 	3736882
6 	United Kingdom 	3158938
7 	France 	2923489
8 	Italy 	2169745
9 	Canada 	2089672
10 	Brazil 	2081235
}"""
# Assign column names as "Country" and "GDP (Million USD)"
df.columns = ['Country','GDP (Million USD)']

"""{
 	Country 	GDP (Million USD)
1 	United States 	26854599
2 	China 	19373586
3 	Japan 	4409738
4 	Germany 	4308854
5 	India 	3736882
6 	United Kingdom 	3158938
7 	France 	2923489
8 	Italy 	2169745
9 	Canada 	2089672
10 	Brazil 	2081235
}"""

# Change the data type of the 'GDP (Million USD)' column to integer. Use astype() method.
df['GDP (Million USD)']= df['GDP (Million USD)'].astype(int)
df
"""{
 	Country 	GDP (Million USD)
1 	United States 	26854
2 	China 	19373
3 	Japan 	4409
4 	Germany 	4308
5 	India 	3736
6 	United Kingdom 	3158
7 	France 	2923
8 	Italy 	2169
9 	Canada 	2089
10 	Brazil 	2081

}"""
# Convert the GDP value in Million USD to Billion USD
df['GDP (Million USD)'] = df['GDP (Million USD)'] / 1000
df
"""{
 	Country 	GDP (Million USD)
1 	United States 	26.854
2 	China 	19.373
3 	Japan 	4.409
4 	Germany 	4.308
5 	India 	3.736
6 	United Kingdom 	3.158
7 	France 	2.923
8 	Italy 	2.169
9 	Canada 	2.089
10 	Brazil 	2.081
}"""
# Use numpy.round() method to round the value to 2 decimal places.
df['GDP (Million USD)'] = np.round(df['GDP (Million USD)'],2)
df
"""{
 	Country 	GDP (Million USD)
1 	United States 	26854.60
2 	China 	19373.59
3 	Japan 	4409.74
4 	Germany 	4308.85
5 	India 	3736.88
6 	United Kingdom 	3158.94
7 	France 	2923.49
8 	Italy 	2169.74
9 	Canada 	2089.67
10 	Brazil 	2081.24

}"""
# Rename the column header from 'GDP (Million USD)' to 'GDP (Billion USD)'
df.rename(columns= {'GDP (Million USD)' : 'GDP (Billion USD)'})
"""{ 
 	Country 	GDP (Billion USD)
1 	United States 	26854.60
2 	China 	19373.59
3 	Japan 	4409.74
4 	Germany 	4308.85
5 	India 	3736.88
6 	United Kingdom 	3158.94
7 	France 	2923.49
8 	Italy 	2169.74
9 	Canada 	2089.67
10 	Brazil 	2081.24

} """


# Load the DataFrame to the CSV file named "Largest_economies.csv"
df.to_csv('./GDP_data.csv')
read_csv = pd.read_csv('./GDP_data.csv')
print(read_csv)

"""{
   Unnamed: 0         Country  GDP (Million USD)
0           1   United States           26854.60
1           2           China           19373.59
2           3           Japan            4409.74
3           4         Germany            4308.85
4           5           India            3736.88
5           6  United Kingdom            3158.94
6           7          France            2923.49
7           8           Italy            2169.74
8           9          Canada            2089.67
9          10          Brazil            2081.24


}"""
