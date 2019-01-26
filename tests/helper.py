import json
import os


class Helper:

    """
    doc block goes here
    """
    @staticmethod
    def load_fixture(name):
        directory = os.path.dirname(os.path.realpath(__file__))
        filename = '{}/fixtures/{}.json'.format(directory, name)

        with open(filename, 'r') as f:
            return json.loads(f.read())


