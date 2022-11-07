import requests

url_endpoint = str('http://127.0.0.1:5000/experimentos_fazenda')


def test_sucesso_200():
    response = requests.post(url_endpoint,
                             data={"taxafaz": 2.34,
                                   "velofaz": 3.43,
                                   "pressaofaz": 92.6,
                                   "tempfaz": 31.5,
                                   "umidfaz": 70,
                                   "ventofaz": 18.6,
                                   "prodfaz_1": "teste",
                                   "dosefaz_1": 700,
                                   "id_comp_faz": 1,
                                   "nome_faz": "fazenda123"
                                   })
    assert response.status_code == 200


def test_limite_400():
    response = requests.post(url_endpoint,
                             data={"taxafaz": 2322222222222222222222222222222222222222222222222222222222222222222222.34,
                                   "velofaz": 3222222222222222222222222222222222222222222222222222222222222222222222.43,
                                   "pressaofaz": 92333333333333333333333333333333333333333333333333333333333333333333.6,
                                   "tempfaz": 44444444444444444444444444444444444444444444444444444444444444444444431.5,
                                   "umidfaz": 7444444444444444444444444444444444444444444444444444444444444444444444440,
                                   "ventofaz": 1877777777777777777777777777777777777777777777777777777777777777777777.6,
                                   "prodfaz_1": "testetestetestetestetestetestetestetestetestetestetestetestetestetestetestetestetestetestetestetestetestetestetestetestetestetestetestetestetesteteste",
                                   "dosefaz_1": 70333333333333333333333333333333333333333333333333333333333333333333330,
                                   "id_comp_faz": 123342243244444444444444446666666666666666666666666666666666666544444,
                                   "nome_faz": "fazendatestetestetestetestetestetestetestetestetestetestetestetestetestetestetestetestetestetestetestetestetestetestetestetestetestetestetestetesteteste"
                                   })
    assert response.status_code == 400


def test_tipagem_400():
    response = requests.post(url_endpoint,
                             data={"taxafaz": True,
                                   "velofaz": "3.43",
                                   "pressaofaz": False,
                                   "tempfaz": "31.5",
                                   "umidfaz": True,
                                   "ventofaz": "18.6",
                                   "prodfaz_1": 123,
                                   "dosefaz_1": False,
                                   "id_comp_faz": "1",
                                   "nome_faz": 123
                                   })
    assert response.status_code == 400


def test_nulo_400():
    response = requests.post(url_endpoint,
                             data={"taxafaz": None,
                                   "velofaz": None,
                                   "pressaofaz": None,
                                   "tempfaz": None,
                                   "umidfaz": None,
                                   "ventofaz": None,
                                   "prodfaz_1": None,
                                   "dosefaz_1": None,
                                   "id_comp_faz": None,
                                   "nome_faz": None
                                   })
    assert response.status_code == 400


def test_obrigatoriedade_400():
    response = requests.post(url_endpoint,
                             data={})
    assert response.status_code == 400


def test_vazio_400():
    response = requests.post(url_endpoint,
                             data={"taxafaz": "",
                                   "velofaz": "",
                                   "pressaofaz": "",
                                   "tempfaz": "",
                                   "umidfaz": "",
                                   "ventofaz": "",
                                   "prodfaz_1": "",
                                   "dosefaz_1": "",
                                   "id_comp_faz": "",
                                   "nome_faz": ""
                                   })
    assert response.status_code == 400
