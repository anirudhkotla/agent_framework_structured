import json
import os

WIKI_FILE = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "../../../data/wiki.json"
    )
)


class WikiStore:

    @staticmethod
    def load_wiki():

        if not os.path.exists(WIKI_FILE):
            return {}

        with open(WIKI_FILE, "r") as f:
            return json.load(f)

    @staticmethod
    def save_wiki(data):

        with open(WIKI_FILE, "w") as f:
            json.dump(data, f, indent=2)

    @staticmethod
    def update_entity(entity, relation, target):

        wiki = WikiStore.load_wiki()

        if entity not in wiki:
            wiki[entity] = {}

        if relation not in wiki[entity]:
            wiki[entity][relation] = []

        if target not in wiki[entity][relation]:
            wiki[entity][relation].append(target)

        WikiStore.save_wiki(wiki)