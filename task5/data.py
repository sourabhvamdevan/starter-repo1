import csv
import os

DATA_DIRECTORY = "./data"
OUTPUT_FILE_PATH = "./formatted_data.csv"

with open(OUTPUT_FILE_PATH, "w", newline="") as output_file:
    writer = csv.writer(output_file)
    writer.writerow(["sales", "date", "region"])

    for file_name in os.listdir(DATA_DIRECTORY):
        with open(f"{DATA_DIRECTORY}/{file_name}", "r") as input_file:
            reader = csv.reader(input_file)
            next(reader)  # Skip header
            for product, raw_price, quantity, transaction_date, region in reader:
                if product == "pink morsel":
                    sale = float(raw_price[1:]) * int(quantity)
                    writer.writerow([sale, transaction_date, region])
