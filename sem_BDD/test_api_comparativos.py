import requests

url_endpoint = str('http://127.0.0.1:5000/comparativos')


def test_sucesso_200():
    response = requests.post(url_endpoint,
                             data={"nome": "xpto",
                                   "data": "2022-02-24",
                                   "ponta": "teste",
                                   "equipamento": "tal"})
    assert response.status_code == 200


def test_limite_400():
    response = requests.post(url_endpoint,
                             data={
                                 "nome": "12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901",
                                 "data": "11111-02-24",
                                 "ponta": "12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901",
                                 "equipamento": "12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901"})
    assert response.status_code == 400


def test_tipagem_400():
    response = requests.post(url_endpoint,
                             data={"nome": "123",
                                   "data": "teste",
                                   "ponta": "123",
                                   "equipamento": "123"})
    assert response.status_code == 400


def test_nulo_400():
    response = requests.post(url_endpoint,
                             data={"nome": None,
                                   "data": None,
                                   "ponta": None,
                                   "equipamento": None})
    assert response.status_code == 400


def test_obrigatoriedade_400():
    response = requests.post(url_endpoint,
                             data={})
    assert response.status_code == 400


def test_vazio_400():
    response = requests.post(url_endpoint,
                             data={"nome": "",
                                   "data": "",
                                   "ponta": "",
                                   "equipamento": ""})
    assert response.status_code == 400
