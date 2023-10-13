import requests
from bs4 import BeautifulSoup
import pandas as pd


# This list contains all the countries in Southeast Asia
countries = ['Singapore', 'Malaysia', 'Indonesia', 'Philippines', 'Thailand', 'Vietnam', 'Myanmar', 'Cambodia', 'Laos', 'Brunei', 'Timor-Leste']

# URL of the Numbeo webpage with currency set to USD
URL = "https://www.numbeo.com/cost-of-living/country_result.jsp?country={}&displayCurrency=USD"

# Empty list to store the scraped data
data = []

# Iterating through each country to scrape data
for country in countries:
    
    # Formating the URL to include the country name
    url_formatted = URL.format(country)

    # Sending a request to the URL and getting a response
    page = requests.get(url_formatted)

    # Parsing the HTML content of the page
    soup = BeautifulSoup(page.content, "html.parser")

    # Finding the table that contains the cost of living data
    table = soup.find("table", class_="data_wide_table new_bar_table")

    # Finding all the rows of the table
    rows = table.find_all("tr")

    # Iterating thorugh each row of the table
    for row in rows:
        
        # Extract all <th> (table header) and <td> (table data) elements within the current row
        elements = row.find_all(["th", "td"])
        
        #Create a new list where we will store the scrape values for each row
        final_results = []

        # Extract and clean the text from each element, then add it to the final_results list
        for element in elements:
            final_results.append(element.text.strip())

        #Add the current country name and its associated final_results to the data list
        data.append([country] + final_results)

#Store the results in a DataFrame
df = pd.DataFrame(data)

#Printing the DataFrame to the console for inspection
print(df)    

#Exporting the results to a CSV file
df.to_csv("numbeo_data_usd.csv", index =False, encoding = 'utf-8-sig')




