from Cotafrete import calcular_frete
import cota_frete
import pytest

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
    assert fator == cota_frete

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
import cota_frete  # importa o módulo com a função que você quer testar

#def test_calcula_frete_caixa_papelao():
#    distancia = 102
#    embalagem = "caixa papelão"
#    altura = 1
#    largura = 1
#    profundidade = 1
#    peso = 1
#    resultado = cota_frete.calcular_frete(distancia, altura, largura, profundidade, peso, total_itens, embalagem)
 #   F = 0.26   # fator F depende da embalagem (0.26 para caixa, 0.37 para container)
 #   esperado = (altura * largura * profundidade * peso * (1 + F)) * (1 + (distancia * 9.8)) * total_itens

#    assert resultado == esperado


#def test_calcula_frete_container():
#    distancia = 98
#    embalagem = "container"
#    altura = 1
 #   largura = 1
#    profundidade = 1
  #  peso = 1
 #   resultado = cota_frete.calcular_frete(distancia, altura, largura, profundidade, peso, total_itens, embalagem)
#    F = 0.37 # fator F depende da embalagem (0.26 para caixa, 0.37 para container)
  #  esperado = (altura * largura * profundidade * peso * (1 + F)) * (1 + (distancia * 9.8)) * total_itens
#    assert resultado == esperado



    
# Adicionado código para teste de embalagem caixa papelao e container, embalagem invalida se voce colocar "sacola"como exemplo | usado import pytest 

#def test_calculo_caixa_papelao():
 #   resultado = calcular_frete(100, 1, 1, 1, 2, 1, "caixa papelão")
  #  esperado = (1 * (1 + 0.26)) * (1 + (100 * 9.8)) * 2  # conforme sua fórmula
   # assert resultado == esperado

#def test_calculo_container():
 #   resultado = calcular_frete(50, 1, 1, 1, 1, 2, "container")
  #  esperado = (1 * (1 + 0.37)) * (1 + (50 * 9.8)) * 2
   # assert resultado == esperado
