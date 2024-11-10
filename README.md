# Workshop de Testes com PyTest

Curso: Desenvolvimento de Software Multiplataforma - Fatec Araras

Disciplina: Qualidade e Testes de Software

Tema do Workshop: Testes na prática



## 1. Objetivo

Este repositório contém os arquivos e exemplos de código usados no workshop de testes, apresentado na disciplina de Qualidade e Testes de Software. O objetivo é introduzir conceitos de testes automatizados, nessa apresentação em Python, usando o framework PyTest para escrever, organizar e executar testes.



## 2. Conteúdo da Apresentação

- Introdução ao PyTest: O que é e como instalar.
- Estrutura dos Testes: Como organizar e nomear arquivos de teste.
- Conceitos Básicos: Escrevendo e executando testes simples.
- Fixtures e Mocks: Configurações automáticas e simulação de objetos.
- Cobertura de Código: Medindo e gerando relatórios de cobertura com pytest-cov.



## 3. Estrutura do Projeto

project_root/

├── src/          # Código principal

├── tests/        # Arquivos de teste

├── README.md     # Este documento

└── requirements.txt  # Dependências do projeto



## 4. Como Rodar os Testes

Instale as dependências:

    pip install -r requirements.txt

Rode os testes e veja a cobertura:

    pytest --cov=src --cov-report term-missing --cov-report html



## 5. Exemplos

A pasta tests/ contém exemplos de código abordados no workshop, cobrindo conceitos básicos e avançados.



## 6. Referências

<a href="https://docs.pytest.org/en/stable/">Documentação Oficial do PyTest</a>
