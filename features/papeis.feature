Feature: inserção de uma lista de papéis

  @PapeisPost
  Scenario Outline: Verificar se o endpoint PapeisPost realiza a chamada e traz o retorno conforme esperado
    Given que estamos realizando uma chamada para o endpoint PapeisPost
    When preenchermos o body "<body>" do endpoint PapeisPost
    And realizarmos a chamada do endpoint PapeisPost
    Then o resultado da chamada sera <status> do endpoint PapeisPost
    And o retorno sera "<resposta>" do endpoint PapeisPost

    Examples:
      |  body   | status | resposta |
      |  valido |   201  |    ok    |
      | tipoDif |   400  |badRequest|
      | limites |   400  |badRequest|
      |   obg   |   201  |    ok    |
      |  vazio  |   400  |badRequest|
      |  nulo   |   400  |badRequest|