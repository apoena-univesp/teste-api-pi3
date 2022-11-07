import requests

url_endpoint = str('http://127.0.0.1:5000/experimentos_empresa')


def test_sucesso_200():
    response = requests.post(url_endpoint,
                             data={"taxaemp": 2.34,
                                   "veloemp": 3.43,
                                   "pressaoemp": 92.6,
                                   "tempemp": 31.5,
                                   "umidemp": 70,
                                   "ventoemp": 18.6,
                                   "prodemp_1": "teste",
                                   "doseemp_1": 700,
                                   "id_comp_faz": 2,
                                   "nome_faz": "empresa123"
                                   })
    assert response.status_code == 200


def test_limite_400():
    response = requests.post(url_endpoint,
                             data={"taxaemp": 2222222222222222222222222222222222222222222222222222222222222222222222.34,
                                   "veloemp": 3777777777777777777777777777777777777777777777777777777777777777777777.43,
                                   "pressaoemp": 92.699999999999999999999999999999999999999999999999999999999999999999,
                                   "tempemp": 35666666666666666666666666666666666669000000000000000000000000000000001.5,
                                   "umidemp": 9.99999999999999999999999999999999990000000054444444444444444444444555570,
                                   "ventoemp": 1888888888888888888888888888888888888888888888888888888888888888888888.6,
                                   "prodemp_1": "testetestetestetestetestetestetestetestetestetestetestetestetestetestetestetestetestetestetestetestetestetestetestetestetesteteste",
                                   "doseemp_1": 733333333333333333333333333333333333333333333333333332.4444444444444300,
                                   "id_comp_faz": 289317304919238193809280482,
                                   "nome_faz": "empresatestetestetestetestetestetestetestetestetestetestetestetestetestetestetestetestetestetestetestetestetestetestetestetesteteste"
                                   })
    assert response.status_code == 400


def test_tipagem_400():
    response = requests.post(url_endpoint,
                             data={"taxaemp": "2.34",
                                   "veloemp": False,
                                   "pressaoemp": "92.6",
                                   "tempemp": True,
                                   "umidemp": "70",
                                   "ventoemp": "18.6",
                                   "prodemp_1": False,
                                   "doseemp_1": "700",
                                   "id_comp_faz": "2",
                                   "nome_faz": True
                                   })
    assert response.status_code == 400


def test_nulo_400():
    response = requests.post(url_endpoint,
                             data={"taxaemp": None,
                                   "veloemp": None,
                                   "pressaoemp": None,
                                   "tempemp": None,
                                   "umidemp": None,
                                   "ventoemp": None,
                                   "prodemp_1": None,
                                   "doseemp_1": None,
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
                             data={"taxaemp": "",
                                   "veloemp": "",
                                   "pressaoemp": "",
                                   "tempemp": "",
                                   "umidemp": "",
                                   "ventoemp": "",
                                   "prodemp_1": "",
                                   "doseemp_1": "",
                                   "id_comp_faz": "",
                                   "nome_faz": ""
                                   })
    assert response.status_code == 400

