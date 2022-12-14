from behave import *
import requests

from BDD.features.utils.payload import get_payload_papeis


@given('que estamos realizando uma chamada para o endpoint PapeisPost')
def step_impl(context):
    global url_endpoint
    url_endpoint = str('http')


@when('preenchermos o body <body> do endpoint PapeisPost')
def step_impl(context):
    get_payload_papeis()


@when('realizarmos a chamada do endpoint PapeisPost')
def step_impl(context):
    global response
    response = requests.post(url_endpoint,
                             data=get_payload_papeis(),
                             headers={"Content-Type": "application/json"})


@then('o resultado da chamada sera <status> do endpoint PapeisPost')
def step_impl(context):
    print(f'\n[RESPONSE]:', response.json())
    assert response.status_code == 200


@then('o retorno sera <resposta> do endpoint PapeisPost')
def step_impl(context):
    assert context.failed is False
