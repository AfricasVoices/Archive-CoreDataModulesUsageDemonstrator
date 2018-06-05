import argparse
import os

from core_data_modules.traced_data.io import TracedDataCodaIO, TracedDataJsonIO

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Applies Coda-coded data to TracedData JSON file")
    parser.add_argument("user", help="User launching this program", nargs=1)
    parser.add_argument("raw_column", metavar="raw-column", help="Name of raw message column to apply code to", nargs=1)
    parser.add_argument("coded_column", metavar="coded-column", help="Name of column to store code to", nargs=1)
    parser.add_argument("input", help="Path to input file, containing a list of TracedData objects as JSON", nargs=1)
    parser.add_argument("coda_input", metavar="coda-input", help="Path to a coded Coda data file", nargs=1)
    parser.add_argument("output", help="Path to write merged dataset to, as JSON", nargs=1)

    args = parser.parse_args()
    user = args.user[0]
    json_input_path = args.input[0]
    coda_input_path = args.coda_input[0]
    output_path = args.output[0]

    col_raw = args.raw_column[0]
    col_coded = args.coded_column[0]

    # Load data from a JSON file
    with open(json_input_path, "r") as f:
        data = TracedDataJsonIO.import_json_to_traced_data_iterable(f)

    # Merge Coda input into the data imported from the JSON
    with open(coda_input_path, "r") as f:
        data = list(TracedDataCodaIO.import_coda_to_traced_data_iterable(user, data, col_raw, col_coded, f))

    # Write merged output
    if os.path.dirname(output_path) is not "" and not os.path.exists(os.path.dirname(output_path)):
        os.makedirs(os.path.dirname(output_path))
    with open(output_path, "w") as f:
        TracedDataJsonIO.export_traced_data_iterable_to_json(data, f, pretty_print=True)
