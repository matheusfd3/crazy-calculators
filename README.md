# Crazy Calculators

Este é um projeto desenvolvido com o objetivo de demonstrar como a aplicação de **boas práticas de código** pode gerar um sistema sustentável, simples, facilmente escalável e de fácil manutenção.

O projeto é composto por três rotas principais, cada uma utilizando uma calculadora diferente para realizar operações específicas. Ele explora conceitos básicos de design de código e arquitetura de software.

## O que foi aplicado:

### 1. **Design de Código**
   - Uso de **tipagem** para documentar e orientar a construção de funções e métodos.
   - Organização do código com **métodos públicos e privados**, favorecendo a separação de responsabilidades.

### 2. **Estruturação do Projeto**
   - Criação de um projeto organizado em pastas e módulos, facilitando a manutenção e escalabilidade.
   - Uso de **Blueprints do Flask** para organizar rotas e funcionalidades.

### 3. **Testes Unitários**
   - Implementação de testes com **PyTest** para verificar a funcionalidade das calculadoras.
   - Utilização de **mocks** para simular dependências externas, como bibliotecas.

### 4. **Injeção de Dependências e Interfaces**
   - Implementação de **interfaces** para desacoplar dependências e aumentar a flexibilidade do projeto.
   - Uso de uma estrutura de **padrão de fábrica** para gerenciar a criação de objetos.

### 5. **Tratamento de Erros**
   - Criação de respostas amigáveis para erros com mensagens personalizadas e códigos de status HTTP apropriados.
   - Definição de exceções customizadas, como "unprocessable entity" e "bad request".


Adicionalmente, o projeto inclui exemplos práticos da implementação dos **design patterns Facade e Factory**, aplicados em pequenas partes do código.

---

## 🚀 Objetivo

Demonstrar como boas práticas de design e desenvolvimento podem resultar em um projeto sustentável, facilitando a leitura, a manutenção e a escalabilidade.
