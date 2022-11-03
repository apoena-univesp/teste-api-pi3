import requests

url_endpoint = str('http://127.0.0.1:5000/papeisfazenda')


def test_sucesso_200():
    response = requests.post(url_endpoint,
                             data={"dv1": 0,
                                   "dv5": 0,
                                   "dv9": 0,
                                   "porcent_coverage": 0,
                                   "image_area": 0,
                                   "deposit_cm": 0,
                                   "deposition": 0,
                                   "posicao": 1})
    #    print(f'\n[RESPONSE]:', response.json())
    assert response.status_code == 200


def test_limite_400():
    response = requests.post(url_endpoint,
                             data={
                                 "nome": "12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901",
                                 "data": "11111-02-24",
                                 "ponta": "12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901",
                                 "equipamento": "12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901"})
    #    print(f'\n[RESPONSE]:', response.json())
    assert response.status_code == 400


# respostas de erro
#  assert 'request parameters: [data]' in response.json()['message']
#  assert 'bla' in response.json()['message']

def test_tipagem_400():
    response = requests.post(url_endpoint,
                             data={"nome": "123",
                                   "data": "teste",
                                   "ponta": "123",
                                   "equipamento": "123"})
    #    print(f'\n[RESPONSE]:', response.json())
    assert response.status_code == 400


# respostas de erro
#  assert 'request parameters: [data]' in response.json()['message']
#  assert 'bla' in response.json()['message']


def test_nulo_400():
    response = requests.post(url_endpoint,
                             data={"nome": None,
                                   "data": None,
                                   "ponta": None,
                                   "equipamento": None})
    #    print(f'\n[RESPONSE]:', response.json())
    assert response.status_code == 400


# respostas de erro
#  assert 'request parameters: [data]' in response.json()['message']
#  assert 'bla' in response.json()['message']

def test_obrigatoriedade_400():
    response = requests.post(url_endpoint,
                             data={})
    #    print(f'\n[RESPONSE]:', response.json())
    assert response.status_code == 400


# respostas de erro
#  assert 'request parameters: [data]' in response.json()['message']
#  assert 'bla' in response.json()['message']

def test_vazio_400():
    response = requests.post(url_endpoint,
                             data={"nome": "",
                                   "data": "",
                                   "ponta": "",
                                   "equipamento": ""})
    #    print(f'\n[RESPONSE]:', response.json())
    assert response.status_code == 400

# respostas de erro
#  assert 'request parameters: [data]' in response.json()['message']
#  assert 'bla' in response.json()['message']
