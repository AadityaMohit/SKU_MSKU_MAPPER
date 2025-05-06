# webapp/main.py
from flask import Flask, render_template, request
import pandas as pd
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.sku_mapper import SKUMapper


app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["file"]
        sales_df = pd.read_excel(file)
        mapper = SKUMapper(r"C:\Users\aadit\OneDrive\Documents\OneDrive\Desktop\Wms_project\part1_sku_mapper\webapp\mapping_template.xlsx")

        result = mapper.map_skus(sales_df)
        result.to_excel("data/output_web.xlsx", index=False)
        return "Uploaded and mapped successfully!"
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
