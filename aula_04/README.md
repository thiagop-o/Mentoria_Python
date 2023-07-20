<h1><b>Estruturas condicionais</b></h1>

```python
numero = 20
if numero > 15:
    print('E Maior')
    
if numero < 30:
    print('E Menor')
    
if numero == 20:
    print('E igual')
    
if numero != 21:
    print('E diferente')
```

```python
numero = 10
if numero > 15:
    print('E Maior')
else:
    print('E Menor')
```

```python
nota = 4

if nota >= 6:
    print('Aprovado')
elif nota >= 5:
    print('Recuperacao')
else:
    print('Reprovado')
```

```python
#Short Hand
idade = 17

print("De maior") if idade >= 18 else print("De menor")

nota = 4
print('Aprovado') if nota >= 6 else print('Recuperacao') if nota >= 5 else print('Reprovado')
```