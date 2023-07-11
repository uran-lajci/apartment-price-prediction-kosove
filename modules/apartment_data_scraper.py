from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from bs4 import BeautifulSoup
import requests
import csv
import time

def requests_retry_session(
    retries=3,
    backoff_factor=0.3,
    status_forcelist=(500, 502, 504),
    session=None,
):
    session = session or requests.Session()
    retry = Retry(
        total=retries,
        backoff_factor=backoff_factor,
        status_forcelist=status_forcelist,
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    return session

def parse_property(property):
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

    return property_data

def get_data(url):
    try:
        response = requests_retry_session().get(url)
        response.raise_for_status()
    except Exception as x:
        print(f'It failed : {x.__class__.__name__}')
    else:
        soup = BeautifulSoup(response.text, 'html.parser')
        property_list = soup.find_all('li')
        data = []

        for property in property_list:
            property_data = parse_property(property)
            # Ensure all fields are present
            if all(k in property_data for k in ("title", "region", "number_of_rooms", "quadrat", "date", "price")):
                data.append(property_data)

        return data

data_for_csv = []
for page_number in range(1, 3425):
    url = f"https://gjirafa.com/Top/Patundshmeri?f={page_number}&sh=Kosove&k=Banesa&llshp=Qira"
    print(f"Processing page {page_number}")
    data_for_csv.extend(get_data(url))
    time.sleep(1)  # Pause between requests

with open('datasets/raw_apartment_renting_data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames = ["title", "region", "number_of_rooms", "quadrat", "date", "price"])
    writer.writeheader()
    for data in data_for_csv:
        writer.writerow(data)

print("Data scraping completed and saved to raw_apartment_renting_data.csv.")