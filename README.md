# Projeto Prático: Verificação Formal de Programas via Asserções

**Disciplina:** Matemática Discreta  
**Professor:** Dr. Edjard Mota  
**Instituição:** Instituto de Computação – Universidade Federal do Amazonas (Icomp/UFAM)  
**Data:** Junho de 2026

---

## Identificação da Equipe

- **Membro 1:** Daniel Alexandre Oliveira Aguilar - 22554079
- **Membro 2:** Gabriel Owen Salignac Azevedo - 22554037
- **Membro 3:** João Victor Souza da Silva - 22554139
- **Membro 4:** Pedro Ribeiro Bavaresco - 22550963
- **Membro 5:** Yuri Yasuya Sales Takano - 22550964

---

## Descrição do Projeto

Este repositório contém a solução do projeto prático de Verificação Formal de Programas utilizando a primitiva `assert` do Python. O objetivo do trabalho é aplicar conceitos de lógica matemática, como **Invariantes de Loop**, **Princípio da Indução** e **Funções Variantes**, diretamente no espaço de execução de algoritmos imperativos.

O projeto está estruturado em duas partes principais:

1. **Problema Escolhido (Problema 4):** Instrumentação, análise de falha e correção do algoritmo de Busca por Interpolação Linear.
2. **Problema Extra:** Proposta, instrumentação e correção de um novo algoritmo externo à lista original (Algoritmo de Euclides para MDC).

---

## Estrutura do Repositório

```text
├── README.md                      # Relatório completo e documentação do projeto
├── problema_4/                    # Diretório do problema regulamentar
│   └── busca_interpolacao.py      # Implementação com bug, instrumentada e corrigida
└── problema_extra/                # Diretório do algoritmo extra escolhido
    └── mdc_euclides.py            # Implementação com bug, instrumentada e corrigida
```

---

## 1. Problema 4: Busca por Interpolação Linear de Limites

### A. Especificação Lógico-Matemática

- **Pré-condição:** Array A estruturado sobre uma Ordem Total e estritamente crescente.
- **Pós-condição:** Retorna o índice `idx` onde `A[idx] == v`, ou `-1` caso o elemento esteja ausente.
- **Métrica de Espaço e Progresso:** Estreitamento de subespaços lógicos baseados na tricotomia de domínios ordenados.
- **Função Variante Proposta (V_state):** `high - low`, representando a distância entre os limites de busca, que deve diminuir estritamente até chegar a 0.

### B. Análise de Falha (O Bug do Código Quebrado)

Ao executar o código original com o conjunto de dados fornecido (`A = [10, 20, 30, 40, 50]` e `v = 25`), o programa disparou um `AssertionError` na **Asserção de Decremento (Passo 4)**.

- **Razão Aritmética/Geométrica:** O código original atualizava os limites fazendo `low = pos` ou `high = pos`. Como o elemento `25` não está no array, a estimativa matemática da interpolação calculava repetidamente o mesmo ponto de pivô (`pos`). Como esse ponto não era excluído do subespaço de busca, a distância `high - low` permanecia inalterada, a função variante deixava de decrescer e o algoritmo entraria em um loop infinito caso não fosse interrompido pela asserção de terminação.

### C. Por que a Correção Resolve?

A correção consistiu em atualizar os limites para `low = pos + 1` ou `high = pos - 1`. Como o elemento na posição `pos` já foi testado e não é igual a `v`, ele é descartado com segurança. Isso garante que o subespaço delimitado por `[low, high]` encolha em pelo menos uma unidade a cada iteração, fazendo com que a função variante decresça estritamente (`V_new < V_old`), provando a terminação do algoritmo em tempo finito.

---

## 2. Problema Extra: Máximo Divisor Comum (MDC) de Euclides

### A. Especificação Lógico-Matemática

- **Pré-condição:** `a > 0` e `b > 0`.
- **Pós-condição:** Retorna o maior divisor comum entre `a` e `b`.
- **Função Variante Proposta (V_state):** `V(state) = b`. Pelo Teorema do Resto de Euclides, o resto da divisão de `a` por `b` é sempre estritamente menor que `b` (`a % b < b`). Portanto, a variante deve diminuir estritamente até atingir o valor 0.

### B. Análise de Falha (O Bug Proposital)

Foi introduzido um erro de progresso onde as variáveis eram atualizadas de forma linear e sequencial (`a = b; b = a % b`).

- **Explicação do Bug:** Como `a` recebia o valor de `b` antes do cálculo do resto, a expressão seguinte tornava-se efetivamente `b % b`, fazendo com que `b` fosse zerado prematuramente no primeiro passo. Isso quebrava o decremento natural e a manutenção correta do estado do Algoritmo de Euclides, violando a corretude do passo indutivo.

### C. Por que a Correção Resolve?

Utilizando a atribuição simultânea do Python (`a, b = b, a % b`), garantimos que o valor original de `a` seja utilizado no cálculo do módulo antes de ser sobrescrito por `b`. Isso preserva o passo indutivo do Algoritmo de Euclides, assegurando que o divisor `b` diminua estritamente a cada iteração até atingir o caso base (`b = 0`).

---

## Resultados dos Testes Executados

Abaixo estão as saídas reais obtidas no terminal que comprovam o funcionamento das asserções e a validação das correções.

### Output do Problema 4 (`busca_interpolacao.py`)

```text
Executando Bloco de Testes (Problema 4)

Tentando rodar o código original com bug...
Sucesso no teste de falha! Asserção capturou o bug esperado:
  Mensagem do erro: Erro: Loop em execucao infinita (sem progresso)!

-------------------------------------------------
Tentando rodar o código corrigido...
Sucesso! O código corrigido terminou sem estourar nenhuma asserção.
  Resultado retornado: -1 (Significa elemento ausente)
  Buscando o valor 40: Retornou índice 3
```

### Output do Problema Extra (`mdc_euclides.py`)

```text
Executando Bloco de Testes (Problema Extra - MDC)

Tentando rodar o MDC original com bug...

-------------------------------------------------
Tentando rodar o MDC corrigido...
Sucesso. O código corrigido terminou sem estourar nenhuma asserção.
  Resultado retornado: MDC(48, 18) = 6
```