import json
import os

SUMMARY_FILE = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "../../../data/summary.json"
    )
)


class SummaryStore:

    @staticmethod
    def load():

        if not os.path.exists(SUMMARY_FILE):

            return {
                "ideas": []
            }

        with open(SUMMARY_FILE, "r") as f:
            return json.load(f)

    @staticmethod
    def save(data):

        with open(SUMMARY_FILE, "w") as f:
            json.dump(data, f, indent=2)

    @staticmethod
    def update(message):

        data = SummaryStore.load()

        if message not in data["ideas"]:
            data["ideas"].append(message)

        data["ideas"] = data["ideas"][-20:]

        SummaryStore.save(data)