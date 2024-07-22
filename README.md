# Ecommerce_data_scraping
Scraping three e-commerce websites for PDPs

foreignfortune.py - extracts from the frontend of https://foreignfortune.com/collections/men-unisex

lechocolat.py - extracts from the frontend of https://www.lechocolat-alainducasse.com/uk

traderjoes_detailed.py - gets a cookie from https://www.traderjoes.com using playwright then uses graphql to get product skus and uses graphql again to extract detailed information.
Possible improvements - in Trader Joes, batch api calls instead of single call per product, but was running short of time to do so, if you tried to run it at your end please expect the runtime to be greater than 30 mins. Uploading a less detailed version - traderjoes.py if you want to test it out quickly.

validation.py - 
The Validate Class takes the .json path as input.
The validate_schema function outputs all fields missing for a product, along with a dictionary of valid and invalid. validate_description and validate_price_is_numeric validates individual fields.

