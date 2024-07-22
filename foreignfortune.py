import requests
import json
from bs4 import BeautifulSoup
import re
url = 'https://foreignfortune.com'
def get_grid_data(category, func_url):
    products_data = []
    while True:
        response = requests.get(func_url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
        else:
            print(f'Failed to retrieve the webpage. Status code: {response.status_code}')
            exit(0)
        grid_container = soup.find('div', class_='grid grid--uniform grid--view-items')
        grid_items = grid_container.find_all('div', class_='grid__item')
        
        #

        #

        for grid_item in grid_items:
            product_card = grid_item.find('div', class_='grid-view-item product-card')
            if product_card:
                product_link = product_card.find('a', class_='product-card__link').get('href')
                product_name = product_card.find('span', class_='visually-hidden').get_text(strip=True)
                image_tag = product_card.find('img', class_='grid-view-item__image')
                image_url = 'https:' + image_tag.get('src') if image_tag else ''
                product_price = product_card.find('span', class_='product-price__price').get_text(strip=True) if product_card.find('span', class_='product-price__price') else ''
                
                product_data = {
                    'Product Name': re.sub(r'[^\x00-\x7F]+', '', product_name),
                    'Product Link': product_link,
                    'Product ID': product_link.split('/')[-1],
                    'Image URL': image_url,
                    'Price': product_price
                }
                
                products_data.append(product_data)
                
        next_link = ''
        next_link = soup.find('link', {'rel': 'next'})
        if next_link:
            func_url = url + next_link['href']
            print(next_link)
        else:
            break
    return products_data


response = requests.get(url)
file_path = 'foreignfortune.json'
all_data=[]
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    siteNav = soup.find('ul', id='SiteNav')
    links_dict = {}
    links = siteNav.find_all('a', class_='site-nav__link--main')

    for link in links:
        href = link.get('href')
        text = link.get_text(strip=True)
        links_dict[text] = href
else:
    print(f'Failed to retrieve the webpage. Status code: {response.status_code}')
    exit(0)

for category,local_url in links_dict.items():
    local_url = url+local_url
    print(f'Category: {category}, URL: {local_url}')
    products_data = get_grid_data(category,local_url)
    all_data = all_data + products_data

for a in all_data:
    product_url = url+a['Product Link']
    response = requests.get(product_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
    else:
        print(f'Failed to retrieve the webpage. Status code: {response.status_code}')
        exit(0)
    ul_element = soup.find('ul', class_='grid grid--uniform product-single__thumbnails product-single__thumbnails-product-template')
    if ul_element:
        anchor_tags = ul_element.find_all('a')
        images = [anchor['href'] for anchor in anchor_tags]
        for i in range(len(images)):
            images[i] = "https:" + images[i]
        new_parameter1 = {"images": images}
        a.update(new_parameter1)
    elements = soup.find_all(id=re.compile(r"^SingleOptionSelector-"))
    variants = {}
    for element in elements:
        label = soup.find('label', {'for': element['id']}).get_text(strip=True)
        options = [option.get_text(strip=True) for option in element.find_all('option')]
        cleaned_options = [re.sub(r'[^\x00-\x7F]+', '', option) for option in options]
        variants[label] = cleaned_options
    new_parameter2 = {"variants": variants}
    a.update(new_parameter2)

    description_div = soup.find('div', class_='product-single__description rte')
    description_text = description_div.get_text(strip=True) if description_div else None
    description_text = re.sub(r'[^\x00-\x7F]+', '', description_text)
    new_parameter3 = {"description": description_text}
    a.update(new_parameter3)

data_json = json.dumps(all_data, indent=4)

with open(file_path, 'w') as file:
    file.write(data_json)








