Feature: Pagina actual y paginas totales al obtener los usuarios

    Scenario: Paginacion con 10 usuarios, limit 5, primera pagina
        Given existen 10 usuarios registrados
        When obtengo los usuarios con offset 0 limit 5
        Then el numero de pagina actual es 1
            And el numero de paginas totales es 2
            And los usuarios desde 0 hasta 4 estan en la pagina actual
            And la pagina actual tiene 5 usuarios

    Scenario: Paginacion con 10 usuarios, limit 5, segunda pagina
        Given existen 10 usuarios registrados
        When obtengo los usuarios con offset 5 limit 5
        Then el numero de pagina actual es 2
            And el numero de paginas totales es 2
            And los usuarios desde 5 hasta 9 estan en la pagina actual
            And la pagina actual tiene 5 usuarios

    Scenario: Paginacion con 7 usuarios, limit 3, primera pagina
        Given existen 7 usuarios registrados
        When obtengo los usuarios con offset 0 limit 3
        Then el numero de pagina actual es 1
            And el numero de paginas totales es 3
            And los usuarios desde 0 hasta 2 estan en la pagina actual
            And la pagina actual tiene 3 usuarios

    Scenario: Paginacion con 7 usuarios, limit 3, segunda pagina
        Given existen 7 usuarios registrados
        When obtengo los usuarios con offset 3 limit 3
        Then el numero de pagina actual es 2
            And el numero de paginas totales es 3
            And los usuarios desde 3 hasta 5 estan en la pagina actual
            And la pagina actual tiene 3 usuarios

    Scenario: Paginacion con 7 usuarios, limit 3, tercera pagina
        Given existen 7 usuarios registrados
        When obtengo los usuarios con offset 6 limit 3
        Then el numero de pagina actual es 3
            And el numero de paginas totales es 3
            And los usuarios desde 6 hasta 6 estan en la pagina actual
            And la pagina actual tiene 1 usuarios

    Scenario: Paginacion con 10 usuarios, limit 5, primera pagina con offset 0
        Given existen 10 usuarios registrados
        When obtengo los usuarios con offset 0 limit 5
        Then el numero de pagina actual es 1
            And el numero de paginas totales es 2
            And los usuarios desde 0 hasta 4 estan en la pagina actual
            And la pagina actual tiene 5 usuarios

    Scenario: Paginacion con 10 usuarios, limit 5, primera pagina con offset 1
        Given existen 10 usuarios registrados
        When obtengo los usuarios con offset 1 limit 5
        Then el numero de pagina actual es 1
            And el numero de paginas totales es 2
            And los usuarios desde 0 hasta 4 estan en la pagina actual
            And la pagina actual tiene 5 usuarios

    Scenario: Paginacion con 10 usuarios, limit 5, primera pagina con offset 2
        Given existen 10 usuarios registrados
        When obtengo los usuarios con offset 2 limit 5
        Then el numero de pagina actual es 1
            And el numero de paginas totales es 2
            And los usuarios desde 0 hasta 4 estan en la pagina actual
            And la pagina actual tiene 5 usuarios

    Scenario: Paginacion con 10 usuarios, limit 5, primera pagina con offset 3
        Given existen 10 usuarios registrados
        When obtengo los usuarios con offset 3 limit 5
        Then el numero de pagina actual es 1
            And el numero de paginas totales es 2
            And los usuarios desde 0 hasta 4 estan en la pagina actual
            And la pagina actual tiene 5 usuarios

    Scenario: Paginacion con 10 usuarios, limit 5, primera pagina con offset 4
        Given existen 10 usuarios registrados
        When obtengo los usuarios con offset 4 limit 5
        Then el numero de pagina actual es 1
            And el numero de paginas totales es 2
            And los usuarios desde 0 hasta 4 estan en la pagina actual
            And la pagina actual tiene 5 usuarios

    Scenario: Paginacion con 10 usuarios, limit 5, segunda pagina con offset 5
        Given existen 10 usuarios registrados
        When obtengo los usuarios con offset 5 limit 5
        Then el numero de pagina actual es 2
            And el numero de paginas totales es 2
            And los usuarios desde 5 hasta 9 estan en la pagina actual
            And la pagina actual tiene 5 usuarios

    Scenario: Paginacion con 10 usuarios, limit 5, segunda pagina con offset 6
        Given existen 10 usuarios registrados
        When obtengo los usuarios con offset 6 limit 5
        Then el numero de pagina actual es 2
            And el numero de paginas totales es 2
            And los usuarios desde 5 hasta 9 estan en la pagina actual
            And la pagina actual tiene 5 usuarios

    Scenario: Paginacion con 10 usuarios, limit 5, segunda pagina con offset 7
        Given existen 10 usuarios registrados
        When obtengo los usuarios con offset 7 limit 5
        Then el numero de pagina actual es 2
            And el numero de paginas totales es 2
            And los usuarios desde 5 hasta 9 estan en la pagina actual
            And la pagina actual tiene 5 usuarios

    Scenario: Paginacion con 10 usuarios, limit 5, segunda pagina con offset 8
        Given existen 10 usuarios registrados
        When obtengo los usuarios con offset 8 limit 5
        Then el numero de pagina actual es 2
            And el numero de paginas totales es 2
            And los usuarios desde 5 hasta 9 estan en la pagina actual
            And la pagina actual tiene 5 usuarios

    Scenario: Paginacion con 10 usuarios, limit 5, segunda pagina con offset 9
        Given existen 10 usuarios registrados
        When obtengo los usuarios con offset 9 limit 5
        Then el numero de pagina actual es 2
            And el numero de paginas totales es 2
            And los usuarios desde 5 hasta 9 estan en la pagina actual
            And la pagina actual tiene 5 usuarios

    Scenario: Paginacion con 7 usuarios, limit 3, primera pagina con offset 0
        Given existen 7 usuarios registrados
        When obtengo los usuarios con offset 0 limit 3
        Then el numero de pagina actual es 1
            And el numero de paginas totales es 3
            And los usuarios desde 0 hasta 2 estan en la pagina actual
            And la pagina actual tiene 3 usuarios

    Scenario: Paginacion con 7 usuarios, limit 3, primera pagina con offset 1
        Given existen 7 usuarios registrados
        When obtengo los usuarios con offset 1 limit 3
        Then el numero de pagina actual es 1
            And el numero de paginas totales es 3
            And los usuarios desde 0 hasta 2 estan en la pagina actual
            And la pagina actual tiene 3 usuarios

    Scenario: Paginacion con 7 usuarios, limit 3, primera pagina con offset 2
        Given existen 7 usuarios registrados
        When obtengo los usuarios con offset 2 limit 3
        Then el numero de pagina actual es 1
            And el numero de paginas totales es 3
            And los usuarios desde 0 hasta 2 estan en la pagina actual
            And la pagina actual tiene 3 usuarios

    Scenario: Paginacion con 7 usuarios, limit 3, segunda pagina con offset 3
        Given existen 7 usuarios registrados
        When obtengo los usuarios con offset 3 limit 3
        Then el numero de pagina actual es 2
            And el numero de paginas totales es 3
            And los usuarios desde 3 hasta 5 estan en la pagina actual
            And la pagina actual tiene 3 usuarios

    Scenario: Paginacion con 7 usuarios, limit 3, segunda pagina con offset 4
        Given existen 7 usuarios registrados
        When obtengo los usuarios con offset 4 limit 3
        Then el numero de pagina actual es 2
            And el numero de paginas totales es 3
            And los usuarios desde 3 hasta 5 estan en la pagina actual
            And la pagina actual tiene 3 usuarios

    Scenario: Paginacion con 7 usuarios, limit 3, segunda pagina con offset 5
        Given existen 7 usuarios registrados
        When obtengo los usuarios con offset 5 limit 3
        Then el numero de pagina actual es 2
            And el numero de paginas totales es 3
            And los usuarios desde 3 hasta 5 estan en la pagina actual
            And la pagina actual tiene 3 usuarios

    Scenario: Paginacion con 7 usuarios, limit 3, tercera pagina con offset 6
        Given existen 7 usuarios registrados
        When obtengo los usuarios con offset 6 limit 3
        Then el numero de pagina actual es 3
            And el numero de paginas totales es 3
            And los usuarios desde 6 hasta 6 estan en la pagina actual
            And la pagina actual tiene 1 usuarios

    Scenario: Paginacion con 7 usuarios que empiezan con user, 3 que empiezan con mateo, limit 3, primera pagina con offset 0
        Given existen 7 usuarios registrados que empiezan con "user"
            And existen 3 usuarios registrados que empiezan con "mateo"
        When obtengo los usuarios con offset 0 limit 3 y nombre similar a "mat"
        Then el numero de pagina actual es 1
            And el numero de paginas totales es 1
            And los usuarios desde 0 hasta 2 que empiezan con "mateo" estan en la pagina actual
            And la pagina actual tiene 3 usuarios

    Scenario: Paginacion con 7 usuarios que empiezan con user, 6 que empiezan con mateo, limit 3, segunda pagina con offset 3
        Given existen 7 usuarios registrados que empiezan con "user"
            And existen 6 usuarios registrados que empiezan con "mateo"
        When obtengo los usuarios con offset 3 limit 3 y nombre similar a "mat"
        Then el numero de pagina actual es 2
            And el numero de paginas totales es 2
            And los usuarios desde 3 hasta 5 que empiezan con "mateo" estan en la pagina actual
            And la pagina actual tiene 3 usuarios