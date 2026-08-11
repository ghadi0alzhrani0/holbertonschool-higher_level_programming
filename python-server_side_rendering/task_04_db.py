#!/usr/bin/python3
"""Display product data from JSON, CSV, or SQLite using Flask."""

import csv
import json
import sqlite3
from pathlib import Path

from flask import Flask, render_template, request


app = Flask(__name__)
BASE_DIRECTORY = Path(__file__).resolve().parent


def read_json_products():
    """Read products from the JSON file."""
    file_path = BASE_DIRECTORY / "products.json"

    with file_path.open("r", encoding="utf-8") as file:
        return json.load(file)


def read_csv_products():
    """Read products from the CSV file."""
    file_path = BASE_DIRECTORY / "products.csv"

    with file_path.open("r", encoding="utf-8", newline="") as file:
        return list(csv.DictReader(file))


def read_sql_products():
    """Read products from the SQLite database."""
    database_path = BASE_DIRECTORY / "products.db"
    connection = None

    try:
        connection = sqlite3.connect(database_path)
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        cursor.execute(
            "SELECT id, name, category, price FROM Products"
        )
        return [dict(row) for row in cursor.fetchall()]
    finally:
        if connection is not None:
            connection.close()


@app.route("/products")
def products():
    """Display products from the selected data source."""
    source = request.args.get("source")
    product_id = request.args.get("id")
    product_list = []
    error = None

    try:
        if source == "json":
            product_list = read_json_products()
        elif source == "csv":
            product_list = read_csv_products()
        elif source == "sql":
            product_list = read_sql_products()
        else:
            error = "Wrong source"
    except sqlite3.Error as database_error:
        error = f"Database error: {database_error}"

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
