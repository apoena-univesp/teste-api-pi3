Feature: inserção de um comparativo na plataforma

  @ComparativosPost
  Scenario Outline: Verificar se o endpoint ComparativosPost realiza a chamada e traz o retorno conforme esperado
    Given que estamos realizando uma chamada para o endpoint ComparativosPost
    When preenchermos o body "<body>" do endpoint ComparativosPost
    And realizarmos a chamada do endpoint ComparativosPost
    Then o resultado da chamada sera <status> do endpoint ComparativosPost
    And o retorno sera "<resposta>" do endpoint ComparativosPost

    Examples:
      |  body   | status | resposta |
      |  valido |   201  |    ok    |
      | tipoDif |   400  |badRequest|
      | limites |   400  |badRequest|
      |   obg   |   201  |    ok    |
      |  vazio  |   400  |badRequest|
      |  nulo   |   400  |badRequest|