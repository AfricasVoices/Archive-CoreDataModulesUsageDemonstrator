import jsonpickle
import json
import time
from core_data_modules.cleaners.english.demographic_cleaner import DemographicCleaner
from core_data_modules.traced_data import Metadata

GENDER_COL = "Gender (Text) - Camelids-LoadTestRandom"

if __name__ == "__main__":
    with open("data/input.json", "r") as f:
        data = jsonpickle.decode(f.read())

    for td in data:
        cleaned = DemographicCleaner.clean_gender(td[GENDER_COL])
        td.append_data({GENDER_COL: cleaned}, Metadata("user", "cleaner", time.time()))  # TODO: User via CLI

    with open("data/output.json", "w") as f:
        # Serialize the list of TracedData to a format which can be trivially deserialized.
        pickled = jsonpickle.dumps(data)

        # Pretty-print the serialized json
        pp = json.dumps(json.loads(pickled), indent=2, sort_keys=True)

        # Write pretty-printed JSON to a file.
        f.write(pp)
