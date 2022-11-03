Feature: inserção de entidades de produto, experimento e produto utilizado em se tratando de empresa

  @ExperimentosEmpresaPost
  Scenario Outline: Verificar se ExperimentosEmpresaPost realiza a chamada e traz o retorno conforme esperado
    Given que estamos realizando uma chamada para o endpoint ExperimentosEmpresaPost
    When preenchermos o body "<body>" do endpoint ExperimentosEmpresaPost
    And realizarmos a chamada do endpoint ExperimentosEmpresaPost
    Then o resultado da chamada sera <status> do endpoint ExperimentosEmpresaPost
    And o retorno sera "<resposta>" do endpoint ExperimentosEmpresaPost

    Examples:
      |  body   | status | resposta |
      |  valido |   201  |    ok    |
      | tipoDif |   400  |badRequest|
      | limites |   400  |badRequest|
      |   obg   |   201  |    ok    |
      |  vazio  |   400  |badRequest|
      |  nulo   |   400  |badRequest|