<h1><b>PEP8 e tipos de Variaveis/Dados</b></h1>

<h3><b>PEP8</b></h3>
Consultar pdf disponibilizado na pasta desta aula.

<br><br>

<h3><b>Funções de Entrada e Saida de dados</b></h3>
Entrada (Input) - sempre recebera uma string

```python
input() #entrada padrao
input('Digite algo: ') #entrada com texto a ser exibido
```

Saida (Output)

```python
print()
print(f'Sua idade é: {idade}') #imprimir formatado
print('python', end=' ') #usado para remover a quebra de linha
print(1, 2, sep='-') #usado para separar com -
```

<br>
Exercicio:
Escreva um programa que recebera seu nome, idade e profissao. E imprimira Meu nome é XXXX, tenho YYY anos e sou ZZZ

<br><br>
<h3><b>Dir e Help</b></h3>
dir: usado para informar todos os metodos/funcoes disponiveis para determinada variavel/tipo de dado.

```python
dir('NTT Data')
```

help: usado para informar a documentacao de uma funçao/metodo


```python
help(int())
```

<br><br>
<h3><b>Tipos de Dados/Variaveis</b></h3>

Tipo inteiro:

```python
num = 1
joao = 2
```

E nao existe limite de tamanho em python para uma variavel numerica. O ceu e o limite(brincadeira a sua memoria da maquina que e)

Podemos tambem para auxiliar na visao de um numero usar separadores por underline. Ex:
```python
print(1_000_000)
```

Tipo float: Real ou decimal

```python
real = 5.44
carlos = 2.22
```

Tipo Boolean: Verdadeiro ou Falso

```python
falso = True
verdadeiro = False
```

Tipo String: Qualquer dado entre aspas simples '' ou duplas ""

```python
nome = "Noemia"
cor = 'Azul'
```

<br><br>
<h3><b>Escopo de Variavel</b></h3>

Global - são variaveis reconhecidas por todo o programa

Local - são variaveis conhecidas somente por um bloco de instrucao ou funcao/metodo


Lembrando: Python e uma linguagem de tipagem dinamica e forte, isso quer dizer que
ela sofre alteracao no tipo porem nao realiza a conversao automaticamente

<br>
Exercicio:

Criar as variaveis que estao sendo utilizadas pelo print com os tipos de dados corretos (string, int, float e boolean)

```python
print('Nome:', nome)
print('Sobrenome:', sobrenome)
print('Idade:', idade)
print('Ano de nascimento:', ano_nascimento)
print('É maior de idade?', maior_de_idade)
print('Altura em metros:', altura_metros)
```