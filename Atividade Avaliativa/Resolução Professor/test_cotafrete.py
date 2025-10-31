import cota_frete

def test_tabela_distancia_1():
    destino = 1
    distancia = cota_frete.tabela_distancia(destino)
    assert distancia == 102

def test_tabela_distancia_2():
    destino = 2
    distancia = cota_frete.tabela_distancia(destino)
    assert distancia == 112

def test_tabela_distancia_3():
    destino = 3
    distancia = cota_frete.tabela_distancia(destino)
    assert distancia == 98

def test_tabela_distancia_4():
    destino = 4
    distancia = cota_frete.tabela_distancia(destino)
    assert distancia == 2922

def test_tabela_distancia_5():  
    destino = 5
    distancia = cota_frete.tabela_distancia(destino)
    assert distancia == 6294

def test_calcula_frete_1():
    destino = 1
    distancia = 102
    embalagem = 1
    altura = 1 
    largura = 1 
    profundidade = 1
    peso = 1
    fator = cota_frete.calcula_frete(destino, embalagem, altura , largura, profundidade, peso)
    assert fator == cota_frete.

def test_calcula_frete_2():
    destino = 1
    distancia = 102
    embalagem = 2
    altura = 1 
    largura = 1 
    profundidade = 1
    peso = 1
    fator = cota_frete.calcula_frete(destino, embalagem, altura , largura, profundidade, peso)
    assert fator == ((altura * largura * profundidade * peso) * (1 + fator)) * (1+(distancia * 9.8))