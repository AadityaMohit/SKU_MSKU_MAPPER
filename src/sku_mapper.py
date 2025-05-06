# part1_sku_mapper/sku_mapper.py

import pandas as pd
from fuzzywuzzy import process

class SKUMapper:
    def __init__(self, mapping_file):
        self.mapping_df = pd.read_excel(mapping_file)
        self.sku_to_msku = dict(zip(self.mapping_df['SKU'], self.mapping_df['MSKU']))

    def map_skus(self, sales_df):
        sales_df['MSKU'] = sales_df['SKU'].apply(self.get_msku)
        return sales_df

    def get_msku(self, sku):
        if sku in self.sku_to_msku:
            return self.sku_to_msku[sku]
        match, score = process.extractOne(sku, self.sku_to_msku.keys())
        return self.sku_to_msku[match] if score > 80 else "Unmapped"
