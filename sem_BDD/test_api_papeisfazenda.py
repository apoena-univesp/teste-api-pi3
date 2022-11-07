import requests

url_endpoint = str('http://127.0.0.1:5000/papeisfazenda')


def test_sucesso_200():
    response = requests.post(url_endpoint,
                             data={"files_sup_faz:": 1010101010101010101010,
                                   "id_exp_fazenda:": 1,
                                   "pos": 1,
                                   "files_med_faz": 1010101010101010101010,
                                   "id_exp_fazenda": 2,
                                   "files_inf_faz": 1010101010101010101010,
                                   "id_exp_fazenda": 1,
                                   })
    assert response.status_code == 200


def test_nulo_400():
    response = requests.post(url_endpoint,
                             data={"files_sup_faz:": None,
                                   "id_exp_fazenda:": None,
                                   "pos": None,
                                   "files_med_faz": None,
                                   "id_exp_fazenda": None,
                                   "files_inf_faz": None,
                                   "id_exp_fazenda": None,
                                   })
    assert response.status_code == 400


def test_obrigatoriedade_400():
    response = requests.post(url_endpoint,
                             data={})
    assert response.status_code == 400
