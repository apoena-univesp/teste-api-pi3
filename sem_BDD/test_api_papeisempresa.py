import requests

url_endpoint = str('http://127.0.0.1:5000/papeisempresa')


def test_sucesso_200():
    response = requests.post(url_endpoint,
                             data={"files_sup_emp:": 1010101010101010101010,
                                   "id_exp_empresa:": 1,
                                   "pos": 1,
                                   "files_med_emp": 1010101010101010101010,
                                   "id_exp_empresa": 2,
                                   "files_inf_emp": 1010101010101010101010,
                                   "id_exp_empresa": 1,
                                   })
    assert response.status_code == 200


def test_nulo_400():
    response = requests.post(url_endpoint,
                             data={"files_sup_emp:": None,
                                   "id_exp_empresa:": None,
                                   "pos": None,
                                   "files_med_emp": None,
                                   "id_exp_empresa": None,
                                   "files_inf_emp": None,
                                   "id_exp_empresa": None,
                                   })
    assert response.status_code == 400


def test_obrigatoriedade_400():
    response = requests.post(url_endpoint,
                             data={})
    assert response.status_code == 400
