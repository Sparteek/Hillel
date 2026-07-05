import csv
import json
import logging
import os
import xml.etree.ElementTree as ET

first_file =  "G:/Hillel/homeworks/Homework_14/random.csv"
second_file = "G:/Hillel/homeworks/Homework_14/random-michaels.csv"
result_file = "G:/Hillel/homeworks/Homework_14/result.csv"



def read_csv(for_csv):
    with open(for_csv, "r", encoding="utf-8", newline='') as csvfile:
        reader = csv.reader(csvfile)
        reader = list(reader)
        return reader

def remove_duplicates_with_set(data):
    act_rows = set()
    unique_rows = []

    for row in data:
        row_tuple = tuple(row)

        if row_tuple not in act_rows:
            act_rows.add(row_tuple)
            unique_rows.append(row_tuple)

    return unique_rows

def write_csv_result(for_csv,data):
    with open(for_csv, "w", encoding="utf-8", newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)


firtst_data = read_csv(first_file)
second_data = read_csv(second_file)
combined_data = firtst_data + second_data
unique_data = remove_duplicates_with_set(combined_data)
write_csv_result(result_file,unique_data)

#Task 2

json_path = "G:/Hillel/homeworks/Homework_14"
log_file = "json__riezanov.log"

logging.basicConfig(filename=log_file, level=logging.ERROR, format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

def validate_json_files(folder):
    for file in os.listdir(folder):
        if file.endswith(".json"):
            file_path = os.path.join(folder, file)
            with open(file_path, "r", encoding="utf-8", newline='') as json_file:
                try:
                    json.load(json_file)
                    print(f"{file} is valid")
                except json.JSONDecodeError as e:
                    logging.error(f"{file} is invalid: {e}")
                    print(f"{file} is invalid -details in {log_file}")

validate_json_files(json_path)

