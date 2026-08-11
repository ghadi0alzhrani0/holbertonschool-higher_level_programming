#!/usr/bin/python3
"""Display product data from JSON or CSV files using Flask."""

import csv
import json
from pathlib import Path

from flask import Flask, render_template, request


app = Flask(__name__)
BASE_DIRECTORY = Path(__file__).resolve().parent


def read_json_products():
    """Read and return products from the JSON file."""
    file_path = BASE_DIRECTORY / "products.json"

    with file_path.open("r", encoding="utf-8") as json_file:
        return json.load(json_file)


def read_csv_products():
    """Read and return products from the CSV file."""
    file_path = BASE_DIRECTORY / "products.csv"

    with file_path.open(
        "r",
        encoding="utf-8",
        newline=""
    ) as csv_file:
        return list(csv.DictReader(csv_file))


@app.route("/products")
def products():
    """Display products from the selected data source."""
    source = request.args.get("source")
    product_id = request.args.get("id")
    product_list = []
    error = None

    if source == "json":
        product_list = read_json_products()
    elif source == "csv":
        product_list = read_csv_products()
    else:
        error = "Wrong source"

    if error is None and product_id is not None:
        product_list = [
            product
            for product in product_list
            if str(product.get("id")) == product_id
        ]

        if not product_list:
            error = "Product not found"

    return render_template(
        "product_display.html",
        products=product_list,
        error=error
    )


if __name__ == "__main__":
    app.run(debug=True, port=5000)
