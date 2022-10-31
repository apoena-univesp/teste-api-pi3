from behave import *
import requests

from features.utils.payload import get_payload_experimentos_empresa


@given('que estamos realizando uma chamada para o endpoint ExperimentosEmpresaPost')
def step_impl(context):
    global url_endpoint
    url_endpoint = str('http.....')


@when('preenchermos o body <body> do endpoint ExperimentosEmpresaPost')
def step_impl(context):
    get_payload_experimentos_empresa()


@when('realizarmos a chamada do endpoint ExperimentosEmpresaPost')
def step_impl(context):
    global response
    response = requests.post(url_endpoint,
                             data=get_payload_experimentos_empresa(),
                             headers={"Content-Type": "application/json"})


@then('o resultado da chamada sera <status> do endpoint ExperimentosEmpresaPost')
def step_impl(context):
    print(f'\n[RESPONSE]:', response.json())
    assert response.status_code == 200


@then('o retorno sera <resposta> do endpoint ExperimentosEmpresaPost')
def step_impl(context):
    assert context.failed is False
