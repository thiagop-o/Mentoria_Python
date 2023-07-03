<h1>Configuração do Sistema</h1>

* Instalar o Visual Studio Code: https://code.visualstudio.com
* Instalar o Python 3.11: https://www.python.org/
  
Usar o comando:
```bash
python --version
py --version
```
para validar se foi instalado corretamente.

Usar o comando no PowerShell(administrador):
```bash
Get-ExecutionPolicy
```
Para verificar o padrão de policy, normalmente vem como **Restricted**.

Para mudar este padrão usamos o comando:
```bash
Set-ExecutionPolicy AllSigned -Force
```
assim conseguiremos rodar o ambiente virtual futuramente.

Para remover pastas compactadas, configurar no settings.json o campo:
```json
    "terminal.integrated.defaultProfile.windows": "PowerShell",
    "explorer.compactFolders": false
``` 

Instalar as Extensões:
* Python
* Code Runner
  
Configurar o Code Runner:
```json
    "code-runner.executorMap": {
        "python": "clear ; python -u",
    },  
    "code-runner.runInTerminal": true,
    "code-runner.ignoreSelection": true,
    "python.defaultInterpreterPath": "python"
```

Minhas Extensões:
* Dracula Official
* Material Icon Theme