# [2065. Qualidade Máxima de um Caminho (Maximum Path Quality of a Graph)](https://leetcode.com/problems/maximum-path-quality-of-a-graph/description/?envType=problem-list-v2&envId=graph)

**Dificuldade:** Difícil  
**Tópicos:** Grafos, DFS, Backtracking, Caminhos com Restrição de Tempo  

---

## Descrição

Você recebe um grafo **não direcionado** com `n` nós numerados de `0` a `n - 1`.

- `values[i]` é o **valor** associado ao nó `i`.  
- `edges[j] = [u_j, v_j, time_j]` representa uma aresta **bidirecional** entre os nós `u_j` e `v_j`, exigindo `time_j` segundos para percorrê-la.  
- `maxTime` indica o **tempo máximo** permitido para percorrer um caminho.

Um caminho é considerado **válido** se:

1. Começa no nó `0`;  
2. Termina no nó `0`;  
3. Leva **no máximo `maxTime` segundos**;  
4. Pode revisitar qualquer nó quantas vezes forem necessárias.

A **qualidade do caminho** é definida como:

> A soma dos valores dos **nós únicos** visitados. Cada nó contribui no máximo uma vez.

O objetivo é retornar a **qualidade máxima possível** de um caminho válido.

> Observação: cada nó possui no máximo **4 arestas** conectadas a ele. O grafo pode ser desconectado.

---

## Exemplo 1

Input: values = [0,32,10,43], edges = [[0,1,10],[1,2,15],[0,3,10]], maxTime = 49
Output: 75
Explanation:
One possible path is 0 -> 1 -> 0 -> 3 -> 0. The total time taken is 10 + 10 + 10 + 10 = 40 <= 49.
The nodes visited are 0, 1, and 3, giving a maximal path quality of 0 + 32 + 43 = 75.

## Exemplo 2

Input: values = [5,10,15,20], edges = [[0,1,10],[1,2,10],[0,3,10]], maxTime = 30
Output: 25
Explanation:
One possible path is 0 -> 3 -> 0. The total time taken is 10 + 10 = 20 <= 30.
The nodes visited are 0 and 3, giving a maximal path quality of 5 + 20 = 25.

## Exemplo 3

Input: values = [1,2,3,4], edges = [[0,1,10],[1,2,11],[2,3,12],[1,3,13]], maxTime = 50
Output: 7
Explanation:
One possible path is 0 -> 1 -> 3 -> 1 -> 0. The total time taken is 10 + 13 + 13 + 10 = 46 <= 50.
The nodes visited are 0, 1, and 3, giving a maximal path quality of 1 + 2 + 4 = 7.

## Restrições

- `n == values.length`  
- `1 <= n <= 1000`  
- `0 <= values[i] <= 10^8`  
- `0 <= edges.length <= 2000`  
- `edges[j].length == 3`  
- `0 <= u_j < v_j <= n - 1`  
- `10 <= time_j, maxTime <= 100`  
- Cada par `(u_j, v_j)` é único  
- Cada nó tem no máximo 4 conexões  
- O grafo pode ser desconectado  
