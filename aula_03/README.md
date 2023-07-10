<h1><b>Operadores Matematicos e Logicos</b></h1>

<h3><b>Operadores Matematicos</b></h3>

```python
soma = 10 + 10
print(f'Soma: {soma}')
```

```python
subtracao = 10 - 5
print(f'Subtracao: {subtracao}')
```

```python
multiplicacao = 10 * 5
print(f'Multiplicacao: {multiplicacao}')
```

```python
divisao = 11 / 5
print(f'Divisao: {divisao}')
```

```python
divisao_inteiro = 11 // 5
print(f'Divisao por inteiro: {divisao_inteiro}')
```

```python
exponencial = 2 ** 3
print(f'Exponencial: {exponencial}')
```

```python
modulo = 5 % 2
print(f'Modulo: {modulo}')
```

```python
concatenacao = 'python e ' + 'top'
print(f'Concatenacao: {concatenacao}')
```

```python
repeticao = 'python ' * 3
print(f'Repeticao: {repeticao}')
```

<br>
<b>Exercicio: </b>Criar uma calculadora normal e uma de IMC utilizando o que ja aprendemos em outras aulas (tipo input...)

<br><br>

<h3><b>Operadores Logicos</b></h3>

```python
igualdade = 10 == 10
print(f'Igual: {igualdade}')
```
<br>
Tabela Verdade E

| p | q | p^q |
|---|---|---|
| F | F | F |
| F | V | F |
| V | F | F |
| V | V | V |

```python
#Qualquer valor com Falso = falso, somente verdadeiro quando todas condiçoes forem verdadeiras
e_01 = True and False
print(f'E 01: {e_01}')
e_02 = True and True
print(f'E 02: {e_02}')
```

<br>
Tabela Verdade OU

| p | q | pvq |
|---|---|---|
| F | F | F |
| F | V | V |
| V | F | V |
| V | V | V |

```python
#Qualquer valor com Verdeiro = verdadeiro, somente falso quando todas condiçoes forem falsas
ou_01 = False or True
print(f'Ou 01: {ou_01}')
```

```python
#Inverte o resultado
nao = not True
print(f'Nao: {nao}')
```

```python
#Maior
maior = 10 > 0
print(f'Maior: {maior}')
```

```python
#Menor
menor = 10 < 0
print(f'Menor: {menor}')
```

```python
#Diferente
diferente = 10 != 0
print(f'Diferente: {diferente}')
```