from behave import *
import requests

from BDD.features.utils.payload import get_payload_comparativos


@given('que estamos realizando uma chamada para o endpoint ComparativosPost')
def step_impl(context):
    global url_endpoint
    url_endpoint = str('http.....')


@when('preenchermos o body <body> do endpoint ComparativosPost')
def step_impl(context):
    get_payload_comparativos()


@when('realizarmos a chamada do endpoint ComparativosPost')
def step_impl(context):
    global response
    response = requests.post(url_endpoint,
                             data=get_payload_comparativos(),
                             headers={"Content-Type": "application/json"})


@then('o resultado da chamada sera <status> do endpoint ComparativosPost')
def step_impl(context):
    print(f'\n[RESPONSE]:', response.json())
    assert response.status_code == 200


@then('o retorno sera <resposta> do endpoint ComparativosPost')
def step_impl(context):
    assert 'sucesso' in response.json()['message']
