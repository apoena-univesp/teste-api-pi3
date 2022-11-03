from behave import *
import requests

from BDD.features.utils.payload import get_payload_experimentos_fazenda


@given('que estamos realizando uma chamada para o endpoint ExperimentosFazendaPost')
def step_impl(context):
    global url_endpoint
    url_endpoint = str('http.....')


@when('preenchermos o body <body> do endpoint ExperimentosFazendaPost')
def step_impl(context):
    get_payload_experimentos_fazenda()


@when('realizarmos a chamada do endpoint ExperimentosFazendaPost')
def step_impl(context):
    global response
    response = requests.post(url_endpoint,
                             data=get_payload_experimentos_fazenda(),
                             headers={"Content-Type": "application/json"})


@then('o resultado da chamada sera <status> do endpoint ExperimentosFazendaPost')
def step_impl(context):
    print(f'\n[RESPONSE]:', response.json())
    assert response.status_code == 200


@then('o retorno sera <resposta> do endpoint ExperimentosFazendaPost')
def step_impl(context):
    assert context.failed is False
