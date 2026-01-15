# Construindo um Projeto Ágil: Da Gestão ao Controle de Qualidade

## 📌 Descrição do Projeto

Este projeto simula o desenvolvimento de um sistema de gerenciamento de tarefas utilizando metodologias ágeis, versionamento de código e práticas de Engenharia de Software. O sistema foi desenvolvido para a empresa fictícia **TechFlow Solutions**, contratada por uma startup do setor de logística que necessita acompanhar o fluxo de trabalho em tempo real, priorizar tarefas críticas e monitorar o desempenho da equipe.

O projeto tem como foco a aplicação prática de conceitos como organização de repositórios, planejamento ágil, controle de qualidade por meio de testes automatizados e gestão de mudanças durante o ciclo de vida do software.

---

## 🎯 Objetivo

Desenvolver um sistema básico de gerenciamento de tarefas que permita:

- Criar, visualizar, atualizar e remover tarefas (CRUD)
- Definir prioridades para as tarefas
- Simular a gestão ágil do projeto utilizando GitHub Projects (Kanban)
- Garantir qualidade do código por meio de testes automatizados
- Aplicar integração contínua com GitHub Actions
- Documentar uma mudança de escopo durante o desenvolvimento

---

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python 3.12
- **Editor de Código:** Visual Studio Code
- **Versionamento:** Git e GitHub
- **Testes Automatizados:** Pytest
- **Integração Contínua:** GitHub Actions
- **Metodologia Ágil:** Kanban

---

## 🧩 Metodologia Ágil Adotada

Foi utilizada a metodologia **Kanban**, aplicada através da aba **GitHub Projects**, permitindo:

- Visualização clara do fluxo de trabalho
- Organização das tarefas em colunas:
  - To Do
  - In Progress
  - Done
- Acompanhamento contínuo do progresso do projeto
- Facilidade na adaptação a mudanças de escopo

---

## 🗂️ Estrutura do Projeto

├── src/
│ ├── init.py
│ └── app.py
│
├── tests/
│ ├── conftest.py
│ └── test_tasks.py
│
├── .github/
│ └── workflows/
│ └── ci.yml
│
├── .gitignore
└── README.md


---

## ⚙️ Funcionalidades Implementadas

- Criação de tarefas
- Validação de entrada (não permitir tarefas sem título)
- Definição de prioridade (ex: baixa, média, alta)
- Listagem de tarefas
- Testes unitários para validação das funcionalidades

---

## 🧪 Testes Automatizados

Os testes automatizados foram implementados utilizando **Pytest**, com o objetivo de garantir a qualidade e o correto funcionamento das funcionalidades principais do sistema.

### Testes realizados:
- Criação de tarefas com título válido
- Validação de erro ao criar tarefa sem título
- Verificação da prioridade da tarefa

Os testes são executados automaticamente tanto localmente quanto pelo pipeline de integração contínua.

---

## 🔁 Integração Contínua (CI)

Foi configurado um pipeline de **Integração Contínua** utilizando **GitHub Actions**, que executa automaticamente os testes sempre que ocorre um push ou pull request para a branch `main`.

O workflow garante:
- Execução automática dos testes
- Detecção precoce de erros
- Maior confiabilidade do código

---

## 🔄 Gestão de Mudanças (Simulação de Mudança de Escopo)

Durante o desenvolvimento do projeto, foi simulada uma mudança de escopo solicitada pelo cliente:

### 🔧 Mudança realizada:
- **Adição de prioridade às tarefas**

### 📄 Justificativa:
A startup de logística identificou a necessidade de destacar tarefas críticas para melhorar a tomada de decisões e o gerenciamento do fluxo de trabalho.

### 🧠 Impacto da mudança:
- Criação de novo card no Kanban
- Atualização do código
- Criação de novos testes automatizados
- Registro da mudança no histórico de commits

Essa mudança demonstra a flexibilidade da metodologia ágil e a importância da adaptação contínua durante o desenvolvimento de software.

---

## ▶️ Como Executar o Projeto Localmente

1️⃣ Clonar o repositório
git clone https://github.com/Daldim/Construindo-um-Projeto-agil-da-Gestao-ao-Controle-de-Qualidade.git

2️⃣ Acessar a pasta do projeto
cd Construindo-um-Projeto-agil-da-Gestao-ao-Controle-de-Qualidade

3️⃣ Instalar as dependências
pip install pytest

4️⃣ Executar os testes
pytest

## 📋 Requisitos Funcionais

- O sistema deve permitir a criação de tarefas com título obrigatório
- O sistema deve permitir a definição de prioridade das tarefas
- O sistema deve permitir a listagem das tarefas cadastradas
- O sistema deve impedir o cadastro de tarefas sem título
- O sistema deve validar automaticamente as regras de negócio por meio de testes

## 🔄 Mudança de Escopo

Durante o desenvolvimento do projeto, foi identificada a necessidade de permitir a listagem das tarefas cadastradas, funcionalidade não prevista inicialmente.

Essa mudança de escopo resultou na implementação de um novo método para listagem de tarefas, bem como a criação de testes automatizados para garantir seu funcionamento, refletindo a adaptação contínua comum em projetos ágeis.


📌 Considerações Finais

Este projeto permitiu aplicar, de forma prática, os principais conceitos da Engenharia de Software, incluindo metodologias ágeis, versionamento, automação de testes, integração contínua e gestão de mudanças. A experiência reflete situações reais do mercado de tecnologia, reforçando a importância da organização, qualidade e adaptabilidade no desenvolvimento de software.
