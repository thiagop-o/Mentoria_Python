""" 
if (numero < 30){
    System.out.println("E menor");
}
"""

numero = 20
if numero > 15:
    print('E Maior')
    
if numero < 30:
    print('E Menor')
    
if numero == 20:
    print('E igual')
    
if numero != 21:
    print('E diferente')

print('\n ------------ next ------------ \n')

""" 
if (numero > 15){
    System.out.println("E Maior");
}else {
    System.out.println("E Menor");
}
"""
    
numero = 10
if numero > 15:
    print('E Maior')
else:
    print('E Menor')
    
print('\n ------------ next ------------ \n')

""" 
if (nota >= 6){
    System.out.println("Aprovado");
}else if (nota >= 5 ){
    System.out.println("Recuperacao");
}else {
    System.out.println("Reprovado");
}
"""
    
nota = 4

if nota >= 6:
    print('Aprovado')
elif nota >= 5:
    print('Recuperacao')
else:
    print('Reprovado')
    
print('\n ------------ next ------------ \n')

#Short Hand IF
nota = 6

if nota >= 6: print('Aprovado')

print('\n ------------ next ------------ \n')

#Short Hand IF ELSE

idade = 17

print('E Maior') if idade >= 18 else print('E Menor')

print('\n ------------ next ------------ \n')

nota = 5

print('Aprovado') if nota >= 6 else print('Recuperacao') if nota >= 5 else print('Reprovado')

