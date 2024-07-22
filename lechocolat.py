import requests
import json
from bs4 import BeautifulSoup
import re
import unicodedata

def remove_unicode(input_string):
    if not input_string:
        return input_string
    normalized_string = unicodedata.normalize('NFKD', input_string)
    ascii_bytes = normalized_string.encode('ascii', 'ignore')
    cleaned_string = ascii_bytes.decode('ascii')
    return cleaned_string

url = 'https://www.lechocolat-alainducasse.com/uk'
response = requests.get(url)
file_path = 'lechocolat.json'
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    chocolat_submenu = soup.find('ul', id='submenu_110')
    cafe_submenu = soup.find('ul', id='submenu_127')
    if chocolat_submenu:
        hrefs = [a['href'] for a in chocolat_submenu.find_all('a', class_='siteMenuItem__link')]

    else:
        print('chocolat_submenu not found')
        exit(0)
    if cafe_submenu:
        hrefs = hrefs + [a['href'] for a in cafe_submenu.find_all('a', class_='siteMenuItem__link')]
    else:
        print('cafe_submenu not found')
        exit(0)
else:
    print(f'Failed to retrieve the webpage. Status code: {response.status_code}')
    exit(0)


pdp = []
for href in hrefs:
    url = href
    print(href)
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        section = soup.find('section', id='js-product-list')

        if section:
            product_divs = section.find_all('div', class_='productMiniature')
            products = []
            
            for product_div in product_divs:
                title_tag = product_div.find('h2', class_='productMiniature__title')
                title_text = title_tag.get_text(strip=True, separator='|').split('|')[0]
                add_to_cart_button = product_div.find('button', class_='productMiniature__addToCart')
                if add_to_cart_button:
                    if add_to_cart_button.get('disabled') is not None:
                        availability = 'Soon Available'
                    else:
                        availability = 'Available'
                else:
                    availability = ''


                product_info = {
                    'id_product': remove_unicode(product_div.get('data-id-product', None)),
                    'name': remove_unicode(product_div.get('data-product-name', None)),
                    'type': remove_unicode(url.rsplit('/', 1)[-1]),
                    'image_src': remove_unicode(product_div.find('img')['src'] if product_div.find('img') else None),
                    'product_url': remove_unicode(product_div.find('a', class_='productMiniature__name')['href'] if product_div.find('a', class_='productMiniature__name') else None),
                    'weight': remove_unicode(product_div.find('span', class_='productMiniature__weight').get_text(strip=True) if product_div.find('span', class_='productMiniature__weight') else None),
                    'price': remove_unicode(product_div.find('span', class_='productMiniature__price').get_text(strip=True) if product_div.find('span', class_='productMiniature__price') else None),
                    'availability': remove_unicode(availability)
                }
                products.append(product_info)
                
            pdp = pdp + products

for a in pdp:
    product_url = a['product_url']
    response = requests.get(product_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
    else:
        print(f'Failed to retrieve the webpage. Status code: {response.status_code}')
        exit(0)
    result = {}
    soup = BeautifulSoup(response.text, 'html.parser')

    product_content = soup.find('div', class_='productAccordion__content js-tab-content')


    description_paragraphs = product_content.find_all('p')[0:2]
    description = " ".join([p.get_text(strip=True) for p in description_paragraphs])
    result['Description'] = description

    sections = product_content.find_all('h3', class_='wysiwyg-title-default')

    for section in sections:
        title = section.get_text(strip=True)
        content = section.find_next_sibling('p').get_text(strip=True)
        result[title] = content

    for key, value in result.items():
        param={key:remove_unicode(value)}
        a.update(param)

pdp_json = json.dumps(pdp, indent=4)

with open(file_path, 'w') as file:
    file.write(pdp_json)

