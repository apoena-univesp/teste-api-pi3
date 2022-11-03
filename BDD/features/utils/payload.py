import json
import os

here = os.path.dirname(os.path.realpath(__file__))


def get_payload_comparativos():
    with open(os.path.join(here, f'body_comparativos.json')) as json_file:
        return json.load(json_file)
    # TODO: CRIAR IFS


def get_payload_experimentos_empresa():
    with open(os.path.join(here, f'body_experimentos_empresa.json')) as json_file:
        return json.load(json_file)
    # TODO: CRIAR IFS


def get_payload_experimentos_fazenda():
    with open(os.path.join(here, f'body_experimentos_fazenda.json')) as json_file:
        return json.load(json_file)
    # TODO: CRIAR IFS


def get_payload_papeis():
    with open(os.path.join(here, f'body_papeis.json')) as json_file:
        return json.load(json_file)
    # TODO: CRIAR IFS
