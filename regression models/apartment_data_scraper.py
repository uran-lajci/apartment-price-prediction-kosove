import requests
from bs4 import BeautifulSoup
import csv

def get_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    property_list = soup.find_all('li')
    data = []

    for property in property_list:
        property_data = {}
        title_element = property.find('h3')
        if title_element is not None:
            property_data['title'] = title_element.get_text(strip=True)

        all_p_tags = property.find_all('p')
        for p_tag in all_p_tags:
            if "Rajoni:" in p_tag.text:
                property_data['region'] = p_tag.text.split(":")[1].strip()
            elif "Numri i dhomave:" in p_tag.text:
                property_data['number_of_rooms'] = p_tag.text.split(":")[1].strip()
            elif "Kuadratura:" in p_tag.text:
                property_data['quadrat'] = p_tag.text.split(":")[1].strip()
            elif "Data:" in p_tag.text:
                property_data['date'] = p_tag.text.split(":")[1].strip()

        price_element = property.find('p', class_="price")
        if price_element is not None:
            property_data['price'] = price_element.text.split(":")[1].strip()

        # Add property data only if it's not empty
        if property_data:
            data.append(property_data)

    return data

# Prepare data for CSV
data_for_csv = []

# Go through pages 1 to 3000
for page_number in range(1, 3000):
    url = f"https://gjirafa.com/Top/Patundshmeri?f={page_number}&sh=Kosove&k=Banesa&llshp=Qira"
    print(f"Processing page {page_number}")
    data_for_csv.extend(get_data(url))

# Write data to CSV
with open('property_data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames = ["title", "region", "number_of_rooms", "quadrat", "price", "date"])
    writer.writeheader()
    for data in data_for_csv:
        writer.writerow(data)

print("Data scraping completed and saved to property_data.csv.")
