import argparse
import os
import time

from core_data_modules.cleaners.english.demographic_cleaner import DemographicCleaner
from core_data_modules.traced_data import Metadata
from core_data_modules.traced_data.io import TracedDataCodaIO, TracedDataJsonIO

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Cleans a list of TracedData items")
    parser.add_argument("user", help="User launching this program", nargs=1)
    parser.add_argument("gender", help="Name of gender column to clean", nargs=1)
    parser.add_argument("input", help="Path to input file, containing a list of TracedData objects as JSON", nargs=1)
    parser.add_argument("output", help="Path to write results of automatic coding to", nargs=1)
    parser.add_argument("coda_output", metavar="coda-output", help="Path to write Coda file to", nargs=1)

    args = parser.parse_args()
    user = args.user[0]
    input_path = args.input[0]
    json_output_path = args.output[0]
    coda_output_path = args.coda_output[0]
    gender_col = args.gender[0]
    gender_col_clean = "{}_clean".format(gender_col)  # Appending _clean follows AVF practice in Dreams

    # Load data from JSON file
    with open(input_path, "r") as f:
        data = TracedDataJsonIO.import_json_to_traced_data_iterable(f)

    # Clean data
    for td in data:
        cleaned = DemographicCleaner.clean_gender(td[gender_col])
        td.append_data({gender_col_clean: cleaned}, Metadata(user, Metadata.get_call_location(), time.time()))

    # Write json output
    if os.path.dirname(json_output_path) is not "" and not os.path.exists(os.path.dirname(json_output_path)):
        os.makedirs(os.path.dirname(json_output_path))
    with open(json_output_path, "w") as f:
        TracedDataJsonIO.export_traced_data_iterable_to_json(data, f, pretty_print=True)

    # Write Coda output
    if os.path.dirname(coda_output_path) is not "" and not os.path.exists(os.path.dirname(coda_output_path)):
        os.makedirs(os.path.dirname(coda_output_path))
    with open(coda_output_path, "w") as f:
        TracedDataCodaIO.export_traced_data_iterable_to_coda(
            data, gender_col, f, exclude_coded_with_key=gender_col_clean)
