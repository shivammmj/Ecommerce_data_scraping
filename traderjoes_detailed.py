import requests
import json
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.traderjoes.com/home/products/category/products-2")
    cookie_for_requests = context.cookies()[3]['value']
    page.wait_for_selector("button.Button_button__3Me73.Button_button_variant_secondary__RwIii", timeout=10000)
    page.click("button.Button_button__3Me73.Button_button_variant_secondary__RwIii")

    cookie_for_requests = context.cookies()[3]['value']
    browser.close()
    print(cookie_for_requests)

url = "https://www.traderjoes.com/api/graphql"
file_path = 'traderjoes_detailed.json'
current_page = 1
payload_template = """{\"query\":\"query SearchProducts($categoryId: String, $currentPage: Int, $pageSize: Int, $storeCode: String = \\\"TJ\\\", $availability: String = \\\"1\\\", $published: String = \\\"1\\\") {\\n  products(\\n    filter: {store_code: {eq: $storeCode}, published: {eq: $published}, availability: {match: $availability}, category_id: {eq: $categoryId}}\\n    currentPage: $currentPage\\n    pageSize: $pageSize\\n  ) {\\n    items {\\n      sku\\n      item_title\\n      category_hierarchy {\\n        id\\n        name\\n        __typename\\n      }\\n      primary_image\\n      primary_image_meta {\\n        url\\n        metadata\\n        __typename\\n      }\\n      sales_size\\n      sales_uom_description\\n      price_range {\\n        minimum_price {\\n          final_price {\\n            currency\\n            value\\n            __typename\\n          }\\n          __typename\\n        }\\n        __typename\\n      }\\n      retail_price\\n      fun_tags\\n      item_characteristics\\n      __typename\\n    }\\n    total_count\\n    pageInfo: page_info {\\n      currentPage: current_page\\n      totalPages: total_pages\\n      __typename\\n    }\\n    aggregations {\\n      attribute_code\\n      label\\n      count\\n      options {\\n        label\\n        value\\n        count\\n        __typename\\n      }\\n      __typename\\n    }\\n    __typename\\n  }\\n}\\n\",\"variables\":{\"storeCode\":\"TJ\",\"availability\":\"1\",\"published\":\"1\",\"categoryId\":2,\"currentPage\":%d,\"pageSize\":10}}"""
payload = payload_template % current_page
headers = {
  'accept': '*/*',
  'accept-language': 'en-US,en;q=0.9,hi;q=0.8',
  'content-type': 'application/json',
  'cookie': F'AMCVS_B5B4708F5F4CE8D80A495ED9%40AdobeOrg=1; s_cc=true; _gid=GA1.2.494186000.1721393126; affinity="1545dfbfb1e7a512"; s_vncm={cookie_for_requests}; s_ivc=true; s_lv_s=Less%20than%201%20day; s_visit=1; s_inv=34047; AMCV_B5B4708F5F4CE8D80A495ED9%40AdobeOrg=-2121179033%7CMCIDTS%7C19924%7CMCMID%7C40249968743363769040406892456492017720%7CMCAAMLH-1722062138%7C12%7CMCAAMB-1722062138%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1721464539s%7CNONE%7CvVersion%7C5.3.0; s_dur=1721459409570; s_ips=779; gpv_c51=https%3A%2F%2Fwww.traderjoes.com%2Fhome%2Fproducts%2Fcategory%2Fproducts-2; _ga_2HMPBJHQ41=GS1.1.1721457337.4.1.1721460757.0.0.0; _ga=GA1.1.856887140.1721393126; s_plt=3.09; s_pltp=www.traderjoes.com%7Chome%7Cproducts%7Ccategory%7Cproducts-2; s_ptc=0.00%5E%5E0.00%5E%5E0.00%5E%5E0.00%5E%5E0.98%5E%5E0.00%5E%5E2.06%5E%5E0.01%5E%5E3.09; s_tp=3455; s_tps=166; s_pvs=282; s_ppv=www.traderjoes.com%257Chome%257Cproducts%257Ccategory%257Cproducts-2%2C100%2C23%2C3455%2C4%2C4; s_nr30=1721460925210-Repeat; s_lv=1721460925212; s_tslv=1721460925216; s_sq=traderjoesprod%3D%2526c.%2526a.%2526activitymap.%2526page%253Dwww.traderjoes.com%25257Chome%25257Cproducts%25257Ccategory%25257Cproducts-2%2526link%253Dpage%2525202%2526region%253Dspa-root%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253Dwww.traderjoes.com%25257Chome%25257Cproducts%25257Ccategory%25257Cproducts-2%2526pidt%253D1%2526oid%253Dfunctionln%252528%252529%25257B%25257D%2526oidt%253D2%2526ot%253DLI; affinity="700cf69549b3b97e"',
  'origin': 'https://www.traderjoes.com',
  'priority': 'u=1, i',
  'referer': 'https://www.traderjoes.com/home/products/category/products-2',
  'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"macOS"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
}
response = requests.request("POST", url, headers=headers, data=payload)
response_json = response.json()
pages = response_json["data"]["products"]["pageInfo"]["totalPages"]
items = []
int_pages = int(pages)
'''json_string = json.dumps(items)
# Write the JSON string to the file, creating or overwriting it if it exists
with open(file_path, 'w') as file:
    file.write(json_string)'''
for i in range(1,int_pages+1):
    print(i)
    payload = payload_template % i
    response = requests.request("POST", url, headers=headers, data=payload)
    response_json = response.json()
    for a in response_json["data"]["products"]["items"]:
        product_url = "https://www.traderjoes.com/home/products/pdp/"+a["sku"]
        new_parameter = {"product_url": product_url}
        a.update(new_parameter)
    items = items + response_json["data"]["products"]["items"]

all_data=[]
for a in items:

    payload_template = """{\"query\":\"query SearchProduct($sku: String, $storeCode: String = \\\"TJ\\\", $published: String = \\\"1\\\") {\\n  products(\\n    filter: {sku: {eq: $sku}, store_code: {eq: $storeCode}, published: {eq: $published}}\\n  ) {\\n    items {\\n      category_hierarchy {\\n        id\\n        url_key\\n        description\\n        name\\n        position\\n        level\\n        created_at\\n        updated_at\\n        product_count\\n        __typename\\n      }\\n      item_story_marketing\\n      product_label\\n      fun_tags\\n      primary_image\\n      primary_image_meta {\\n        url\\n        metadata\\n        __typename\\n      }\\n      other_images\\n      other_images_meta {\\n        url\\n        metadata\\n        __typename\\n      }\\n      context_image\\n      context_image_meta {\\n        url\\n        metadata\\n        __typename\\n      }\\n      published\\n      sku\\n      url_key\\n      name\\n      item_description\\n      item_title\\n      item_characteristics\\n      item_story_qil\\n      use_and_demo\\n      sales_size\\n      sales_uom_code\\n      sales_uom_description\\n      country_of_origin\\n      availability\\n      new_product\\n      promotion\\n      price_range {\\n        minimum_price {\\n          final_price {\\n            currency\\n            value\\n            __typename\\n          }\\n          __typename\\n        }\\n        __typename\\n      }\\n      retail_price\\n      nutrition {\\n        display_sequence\\n        panel_id\\n        panel_title\\n        serving_size\\n        calories_per_serving\\n        servings_per_container\\n        details {\\n          display_seq\\n          nutritional_item\\n          amount\\n          percent_dv\\n          __typename\\n        }\\n        __typename\\n      }\\n      ingredients {\\n        display_sequence\\n        ingredient\\n        __typename\\n      }\\n      allergens {\\n        display_sequence\\n        ingredient\\n        __typename\\n      }\\n      created_at\\n      first_published_date\\n      last_published_date\\n      updated_at\\n      related_products {\\n        sku\\n        item_title\\n        primary_image\\n        primary_image_meta {\\n          url\\n          metadata\\n          __typename\\n        }\\n        price_range {\\n          minimum_price {\\n            final_price {\\n              currency\\n              value\\n              __typename\\n            }\\n            __typename\\n          }\\n          __typename\\n        }\\n        retail_price\\n        sales_size\\n        sales_uom_description\\n        category_hierarchy {\\n          id\\n          name\\n          __typename\\n        }\\n        __typename\\n      }\\n      __typename\\n    }\\n    total_count\\n    page_info {\\n      current_page\\n      page_size\\n      total_pages\\n      __typename\\n    }\\n    __typename\\n  }\\n}\\n\",\"variables\":{\"storeCode\":\"TJ\",\"published\":\"1\",\"sku\":\"%s\"}}"""
    payload = payload_template % a['sku']
    response = requests.request("POST", url, headers=headers, data=payload)
    response_json=response.json()
    all_data=all_data+response_json["data"]["products"]["items"]


json_string = json.dumps(all_data)

with open(file_path, 'w') as file:
    file.write(json_string)

