### Professor
[Jansen Leite](https://github.com/JansenLeite)

## Login

- Usuario = admin
- Senha = 1234

## COTAFRETE - Avaliação Python Jansen Leite

##  Descrição
**COTAFRETE** é um sistema desenvolvido em Python com o objetivo de calcular cotações de frete com base em dados como aeroporto de destino, dimensões da embalagem, peso e tipo de embalagem. Além disso, o sistema conta com uma calculadora integrada com funções matemáticas básicas.

Este projeto é parte do **Projeto Python 02**.

---

### Professor
[Jansen Leite](https://github.com/JansenLeite)

---


## Requisitos Não-Funcionais (RNF)

### Tela Inicial [RNF001]
- Exibe uma **mensagem de boas-vindas personalizada** com o nome do software **COTAFRETE** sempre que o sistema é iniciado.

### Tela de Login [RNF002]
- O usuário deve fornecer um **nome de usuário** e **senha** contendo letras e/ou números.
- Caso o login ou senha estejam incorretos, será exibida uma **mensagem de erro**.
- Com credenciais válidas, o sistema redireciona o usuário para o **Menu Principal**.

### Menu Principal [RNF003]
- Apresenta um menu com opções de navegação para diferentes funcionalidades:
  - Cotação de Frete
  - Calculadora
  - Sair do sistema

---

## Menu Cotação de Frete [RNF004]
Ao selecionar a opção de cotação de frete, o sistema solicitará os seguintes dados:

- **Aeroporto de Destino**
- **Tipo de Embalagem** (Caixa de Papelão ou Container)
- **Dimensões**: Altura, Largura, Profundidade
- **Peso** em Kg
- **Total de Itens**

###  Tabela de Aeroportos x Distância

| Aeroporto de Origem | Aeroporto de Destino | Distância |
|---------------------|----------------------|-----------|
| Viracopos           | Congonhas-SP         | 102 KM    |
| Viracopos           | Guarulhos-SP         | 112 KM    |
| Viracopos           | Campo de Marte-SP    | 98 KM     |
| Viracopos           | Pinto Martins-CE     | 2922 KM   |
| Viracopos           | Eduardo Gomes-AM     | 6294 KM   |

###  Cálculo do Custo de Frete

#### Embalagem: **Caixa de Papelão**
- **Unidade**: metros
- **Fator de custo (F)**: 0.26
- **Fórmula**:


#### Embalagem: **Container**
- **Unidade**: centímetros
- **Fator de custo (F)**: 0.37
- **Fórmula**:

