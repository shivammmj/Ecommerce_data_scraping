import json

schemas = {
    'lechocolat': {
        "type": "array",
        "items": {
            "type": "object",
            "properties": {
                "id_product": {"type": "string"},
                "name": {"type": "string"},
                "type": {"type": "string"},
                "image_src": {"type": "string"},
                "product_url": {"type": "string"},
                "weight": {"type": "string"},
                "price": {"type": "string"},
                "availability": {"type": "string"},
                "Description": {"type": "string"},
                "Allergens": {"type": "string"},
                "Vegan": {"type": "string"},
                "Price per kilo": {"type": "string"}
            },
            "required": ["id_product", "name", "type", "image_src", "product_url", "weight", "price", "availability", "Description"]
        }
    },
    'foreignfortune': {
        "type": "array",
        "items": {
            "type": "object",
            "properties": {
                "Product Name": {"type": "string"},
                "Product Link": {"type": "string"},
                "Product ID": {"type": "string"},
                "Image URL": {"type": "string"},
                "Price": {"type": "string"},
                "images": {
                    "type": "array",
                    "items": {"type": "string"}
                },
                "variants": {
                    "type": "object",
                    "properties": {
                        "Size": {"type": "array", "items": {"type": "string"}},
                        "Color": {"type": "array", "items": {"type": "string"}},
                        "Style": {"type": "array", "items": {"type": "string"}}
                    }
                },
                "description": {"type": "string"}
            },
            "required": ["Product Name", "Product Link", "Product ID", "Image URL", "Price", "description"]
        }
    },
    'traderjoes_detailed': {
        "type": "array",
        "items": {
            "type": "object",
            "properties": {
                "category_hierarchy": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "id": {"type": "integer"},
                            "url_key": {"type": "string"},
                            "description": {"type": "string"},
                            "name": {"type": "string"},
                            "position": {"type": "integer"},
                            "level": {"type": "integer"},
                            "created_at": {"type": "string"},
                            "updated_at": {"type": "string"},
                            "product_count": {"type": "integer"},
                            "__typename": {"type": "string"}
                        },
                        "required": ["id", "name", "position", "level", "created_at", "updated_at", "product_count", "__typename"]
                    }
                },
                "item_story_marketing": {"type": "string"},
                "product_label": {"type": "string"},
                "fun_tags": {
                    "type": "array",
                    "items": {"type": "string"}
                },
                "primary_image": {"type": "string"},
                "primary_image_meta": {
                    "type": "object",
                    "properties": {
                        "url": {"type": "string"},
                        "metadata": {
                            "type": "object",
                            "properties": {
                                "src": {"type": "string"},
                                "srcSet": {
                                    "type": "array",
                                    "items": {
                                        "type": "object",
                                        "properties": {
                                            "src": {"type": "string"},
                                            "media": {"type": "string"},
                                            "type": {"type": "string"}
                                        },
                                        "required": ["src", "media", "type"]
                                    }
                                },
                                "alt": {"type": "string"},
                                "srcOriginal": {"type": "string"}
                            },
                            "required": ["src", "alt", "srcOriginal"]
                        },
                        "__typename": {"type": "string"}
                    },
                    "required": ["url", "metadata"]
                },
                "other_images": {
                    "type": "array",
                    "items": {"type": "string"}
                },
                "other_images_meta": {
                    "type": "array",
                    "items": {"type": "object"}
                },
                "context_image": {"type": "string"},
                "context_image_meta": {"type": "object"},
                "published": {"type": "integer"},
                "sku": {"type": "string"},
                "url_key": {"type": "string"},
                "name": {"type": "string"},
                "item_description": {"type": "string"},
                "item_title": {"type": "string"},
                "item_characteristics": {"type": "string"},
                "item_story_qil": {"type": "string"},
                "use_and_demo": {"type": "string"},
                "sales_size": {"type": "integer"},
                "sales_uom_code": {"type": "string"},
                "sales_uom_description": {"type": "string"},
                "country_of_origin": {"type": "string"},
                "availability": {"type": "string"},
                "new_product": {"type": "string"},
                "promotion": {"type": "string"},
                "price_range": {
                    "type": "object",
                    "properties": {
                        "minimum_price": {
                            "type": "object",
                            "properties": {
                                "final_price": {
                                    "type": "object",
                                    "properties": {
                                        "currency": {"type": "string"},
                                        "value": {"type": "number"},
                                        "__typename": {"type": "string"}
                                    },
                                    "required": ["currency", "value"]
                                },
                                "__typename": {"type": "string"}
                            },
                            "required": ["final_price"]
                        },
                        "__typename": {"type": "string"}
                    },
                    "required": ["minimum_price"]
                },
                "retail_price": {"type": "string"},
                "nutrition": {"type": "string"},
                "ingredients": {"type": "string"},
                "allergens": {"type": "string"},
                "created_at": {"type": "string"},
                "first_published_date": {"type": "string"},
                "last_published_date": {"type": "string"},
                "updated_at": {"type": "string"},
                "related_products": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "sku": {"type": "string"},
                            "item_title": {"type": "string"},
                            "primary_image": {"type": "string"},
                            "primary_image_meta": {
                                "type": "object",
                                "properties": {
                                    "url": {"type": "string"},
                                    "metadata": {
                                        "type": "object",
                                        "properties": {
                                            "src": {"type": "string"},
                                            "srcSet": {
                                                "type": "array",
                                                "items": {
                                                    "type": "object",
                                                    "properties": {
                                                        "src": {"type": "string"},
                                                        "media": {"type": "string"},
                                                        "type": {"type": "string"}
                                                    },
                                                    "required": ["src", "media", "type"]
                                                }
                                            },
                                            "alt": {"type": "string"},
                                            "srcOriginal": {"type": "string"}
                                        },
                                        "required": ["src", "alt", "srcOriginal"]
                                    },
                                    "__typename": {"type": "string"}
                                },
                                "required": ["url", "metadata"]
                            },
                            "price_range": {
                                "type": "object",
                                "properties": {
                                    "minimum_price": {
                                        "type": "object",
                                        "properties": {
                                            "final_price": {
                                                "type": "object",
                                                "properties": {
                                                    "currency": {"type": "string"},
                                                    "value": {"type": "number"},
                                                    "__typename": {"type": "string"}
                                                },
                                                "required": ["currency", "value"]
                                            },
                                            "__typename": {"type": "string"}
                                        },
                                        "required": ["final_price"]
                                    },
                                    "__typename": {"type": "string"}
                                },
                                "required": ["minimum_price"]
                            },
                            "retail_price": {"type": "string"},
                            "sales_size": {"type": "integer"},
                            "sales_uom_description": {"type": "string"},
                            "category_hierarchy": {
                                "type": "array",
                                "items": {
                                    "type": "object",
                                    "properties": {
                                        "id": {"type": "integer"},
                                        "name": {"type": "string"},
                                        "__typename": {"type": "string"}
                                    },
                                    "required": ["id", "name"]
                                }
                            },
                            "__typename": {"type": "string"}
                        },
                        "required": ["sku", "item_title", "price_range", "retail_price"]
                    }
                },
                "__typename": {"type": "string"}
            },
            "required": ["category_hierarchy", "item_story_marketing", "product_label", "fun_tags", "primary_image", "primary_image_meta", "other_images", "context_image", "published", "sku", "url_key", "name", "item_description", "item_title", "sales_size", "sales_uom_code", "sales_uom_description", "availability", "new_product", "promotion", "price_range", "retail_price", "created_at", "first_published_date", "last_published_date", "updated_at"]
        }
    }
}

class Validate:
    def __init__(self, json_file_path):
        self.json_file_path = json_file_path
        
        # Determine schema type from file name
        self.schema_type = json_file_path.split('/')[-1].split('.')[0]
        
        if self.schema_type not in schemas:
            raise ValueError(f"Invalid schema type. Choose from: {', '.join(schemas.keys())}")
        
        with open(self.json_file_path, 'r') as file:
            self.json_data = json.load(file)
        
    def validate_description(self):
        description_key = {
            'lechocolat': 'Description',
            'foreignfortune': 'description',
            'traderjoes_detailed': 'item_story_marketing'
        }.get(self.schema_type)

        id_key = {
            'lechocolat': 'id_product',
            'foreignfortune': 'Product ID',
            'traderjoes_detailed': 'sku'
        }.get(self.schema_type)

        valid_ids = []
        invalid_ids = []

        for item in self.json_data:
            description = item.get(description_key)
            item_id = item[id_key]

            if description is None:
                invalid_ids.append(item_id)
            elif not description.strip():
                invalid_ids.append(item_id)
            else:
                valid_ids.append(item_id)

        return {
            'valid_ids': valid_ids,
            'invalid_ids': invalid_ids
        }
    
    def validate_price_is_numeric(self):
        price_key = {
            'lechocolat': 'price',
            'foreignfortune': 'Price',
            'traderjoes_detailed': 'retail_price'
        }.get(self.schema_type)

        id_key = {
            'lechocolat': 'id_product',
            'foreignfortune': 'Product ID',
            'traderjoes_detailed': 'sku'
        }.get(self.schema_type)

        valid_ids = []
        invalid_ids = []

        for item in self.json_data:
            price = item.get(price_key)
            item_id = item[id_key]
            try:
                int_price = float(price)
            except:
                invalid_ids.append(item_id)
                continue
            if int_price == 0.0 or int_price <= 0.0:
                invalid_ids.append(item_id)
            else:
                valid_ids.append(item_id)

        return {
            'valid_ids': valid_ids,
            'invalid_ids': invalid_ids
        }
    
    def validate_schema(self):
        id_key = {
            'lechocolat': 'id_product',
            'foreignfortune': 'Product ID',
            'traderjoes_detailed': 'sku'
        }.get(self.schema_type)
        schema = schemas[self.schema_type]
        all_valid_ids = []
        all_invalid_ids = []

        for item in self.json_data:
            try:
                item_id = item[id_key]
                missing_fields = []

                for field in schema['items']['properties']:
                    if field not in item:
                        missing_fields.append(field)

                if missing_fields:
                    all_invalid_ids.append(item_id)
                    print(f"{item_id} is missing fields: {', '.join(missing_fields)}")
                else:
                    all_valid_ids.append(item_id)
            except Exception as e:
                print(e)
                all_invalid_ids.append(item_id)

        return {'valid_ids': all_valid_ids, 'invalid_ids': all_invalid_ids}
    
    def run_all_validations(self):
        print("\nChecking if any fields are missing - \n")
        print(self.validate_schema())
        print("\nChecking if description exists and is not empty - \n")
        print(self.validate_description())
        print("\nChecking if Retail prices are numeric -")
        print(self.validate_price_is_numeric())

if __name__ == "__main__":
    validator = Validate("foreignfortune.json")
    validator.run_all_validations()
    validator = Validate("lechocolat.json")
    validator.run_all_validations()
    validator = Validate("traderjoes_detailed.json")
    validator.run_all_validations()
    


