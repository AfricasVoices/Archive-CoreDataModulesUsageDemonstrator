import argparse
import json
import os
import time

import jsonpickle
from core_data_modules.cleaners.english.demographic_cleaner import DemographicCleaner
from core_data_modules.traced_data import Metadata

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Cleans a list of TracedData items")
    parser.add_argument("user", help="User launching this program", nargs=1)
    parser.add_argument("gender", help="Name of gender column to clean", nargs=1)
    parser.add_argument("input", help="Path to input file, containing a list of TracedData objects as JSON", nargs=1)
    parser.add_argument("output", help="Path to output file", nargs=1)

    args = parser.parse_args()
    user = args.user[0]
    input_path = args.input[0]
    output_path = args.output[0]
    gender_col = args.gender[0]

    with open(input_path, "r") as f:
        data = jsonpickle.decode(f.read())

    for td in data:
        cleaned = DemographicCleaner.clean_gender(td[gender_col])
        # Appending _clean follows AVF practice in Dreams
        td.append_data({"{}_clean".format(gender_col): cleaned}, Metadata(user, "clean_traced.py", time.time()))

    if not os.path.exists(os.path.dirname(output_path)):
        os.makedirs(os.path.dirname(output_path))

    with open(output_path, "w") as f:
        # Serialize the list of TracedData to a format which can be trivially deserialized.
        pickled = jsonpickle.dumps(data)

        # Pretty-print the serialized json
        pp = json.dumps(json.loads(pickled), indent=2, sort_keys=True)

        # Write pretty-printed JSON to a file.
        f.write(pp)
