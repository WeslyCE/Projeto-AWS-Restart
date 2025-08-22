# Projeto de Infraestrutura Web: Flask e AWS
Neste projeto colaborativo do curso AWS re/Start, demonstramos a capacidade de construir uma infraestrutura de aplicação web do zero. A aplicação foi desenvolvida em Python usando o framework Flask. Para a implantação na nuvem, aplicamos conhecimentos em:

- Amazon EC2: Configuração e gerenciamento de uma instância Linux para hospedar a aplicação.

- Amazon VPC: Configuração de rede segura, incluindo sub-redes e grupos de segurança (Security Groups) para proteger o acesso.

- Git e GitHub: Gerenciamento de código-fonte e colaboração em equipe.

Este projeto é um exemplo prático de nossa habilidade em utilizar as principais ferramentas da AWS para construir e gerenciar ambientes de nuvem robustos.

## 📘 Guia de Configuração do Ambiente Virtual e Flask

### 1. Criar o Ambiente Virtual

No terminal (cmd ou PowerShell), dentro da pasta do projeto:

```bash
python -m venv venv
```

Isso vai criar a pasta `venv` que contém o ambiente isolado.

---

### 2. Ativar o Ambiente Virtual

#### 🔹 Windows

* **Prompt de Comando (cmd):**

```bat
venv\Scripts\activate.bat
```

* **PowerShell:**

```powershell
venv\Scripts\Activate
```

#### 🔹 Linux / MacOS

```bash
source venv/bin/activate
```

Se deu certo, você verá `(venv)` no início da linha do terminal.

---

### 3. Instalar o Flask

Com o ambiente virtual ativado:

```bash
pip install flask
```

---

### 4. Verificar Instalação

```bash
pip show flask
```

ou

```bash
python -m flask --version
```

---

### 5. Rodar o Projeto

Se o arquivo principal for `app.py`:

```bash
python app.py
```

O Flask será iniciado em `http://127.0.0.1:5000`.

---

### 6. ⚠️ Caso de Erro no PowerShell (Execution Policy)

Se ao ativar o ambiente no PowerShell aparecer erro como:

```
O arquivo ...Activate.ps1 não pode ser carregado porque a execução de scripts foi desabilitada neste sistema
```

#### ✅ Solução

Abra o PowerShell **como Administrador** e rode:

```powershell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Isso habilita a execução de scripts locais, mantendo a segurança.

Depois, ative novamente:

```powershell
venv\Scripts\Activate
```

---

### 7. (Opcional) Criar `requirements.txt`

Para salvar as dependências do projeto:

```bash
pip freeze > requirements.txt
```

E para reinstalar em outro ambiente:

```bash
pip install -r requirements.txt
```
