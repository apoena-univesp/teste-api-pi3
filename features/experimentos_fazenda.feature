Feature: inserção de entidades de produto, experimento e produto utilizado em se tratando de empresa

  @ExperimentosFazendaPost
  Scenario Outline: Verificar se ExperimentosFazendaPost realiza a chamada e traz o retorno conforme esperado
    Given que estamos realizando uma chamada para o endpoint ExperimentosFazendaPost
    When preenchermos o body "<body>" do endpoint ExperimentosFazendaPost
    And realizarmos a chamada do endpoint ExperimentosFazendaPost
    Then o resultado da chamada sera <status> do endpoint ExperimentosFazendaPost
    And o retorno sera "<resposta>" do endpoint ExperimentosFazendaPost

    Examples:
      |  body   | status | resposta |
      |  valido |   201  |    ok    |
      | tipoDif |   400  |badRequest|
      | limites |   400  |badRequest|
      |   obg   |   201  |    ok    |
      |  vazio  |   400  |badRequest|
      |  nulo   |   400  |badRequest|