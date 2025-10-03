# Conceitos Básicos de Python: `while` e `try`

Este material tem fins **educacionais** e é voltado a iniciantes que estão aprendendo Python. Ele explica dois conceitos fundamentais da linguagem: o laço `while` e o tratamento de exceções com `try` / `except`.

---

##  Estrutura `while`

###  O que é?

O `while` é uma **estrutura de repetição** que executa um bloco de código **enquanto uma condição for verdadeira**.

###  Sintaxe:

```python
while condição:
    # bloco de código
```

###  Exemplo:

```python
contador = 0

while contador < 5:
    print("Repetição número", contador)
    contador += 1
```

 **Explicação:**

* O código acima imprime os números de 0 a 4.
* O loop só termina quando `contador < 5` se torna falso.

###  Cuidado com loops infinitos!

```python
while True:
    print("Isso nunca vai parar!")
```

> Use `Ctrl + C` para interromper loops infinitos no terminal.

---

##  Estrutura `try` / `except`

###  O que é?

`try` é usado para **testar um bloco de código** que pode c
