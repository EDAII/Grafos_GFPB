# [2092. Encontrar Todas as Pessoas com o Segredo (Find All People With Secret)](https://leetcode.com/problems/find-all-people-with-secret/description/?envType=problem-list-v2&envId=graph)  
**Dificuldade:** Difícil  
**Tópicos:** Grafos, União-Find (Disjoint Set), Ordenação, Simulação de Eventos  

---

## Descrição

Você recebe um inteiro `n` indicando que há `n` pessoas numeradas de `0` a `n - 1`.  
Também recebe uma matriz inteira 2D `meetings` onde `meetings[i] = [x_i, y_i, time_i]` indica que a pessoa `x_i` e a pessoa `y_i` têm uma reunião no instante `time_i`. Uma pessoa pode participar de múltiplas reuniões ao mesmo tempo. Por fim, recebe um inteiro `firstPerson`.

A pessoa `0` tem um segredo e inicialmente compartilha esse segredo com a pessoa `firstPerson` no tempo `0`. O segredo passa a ser compartilhado toda vez que ocorre uma reunião envolvendo uma pessoa que já conhece o segredo. Mais formalmente, para cada reunião, se uma pessoa `x_i` conhece o segredo no instante `time_i`, então ela compartilhará o segredo com `y_i`, e vice-versa.

Os segredos são compartilhados **instantaneamente**. Ou seja, uma pessoa pode **receber** o segredo em um instante e **compartilhá-lo** com outras pessoas em outras reuniões que ocorram **no mesmo instante**.

Retorne uma lista com todas as pessoas que conhecem o segredo **após todas as reuniões**. Você pode retornar a resposta em qualquer ordem.

---

## Exemplo 1

Input: n = 6, meetings = [[1,2,5],[2,3,8],[1,5,10]], firstPerson = 1
Output: [0,1,2,3,5]
Explanation:
At time 0, person 0 shares the secret with person 1.
At time 5, person 1 shares the secret with person 2.
At time 8, person 2 shares the secret with person 3.
At time 10, person 1 shares the secret with person 5.​​​​
Thus, people 0, 1, 2, 3, and 5 know the secret after all the meetings.

## Exemplo 2

Input: n = 4, meetings = [[3,1,3],[1,2,2],[0,3,3]], firstPerson = 3
Output: [0,1,3]
Explanation:
At time 0, person 0 shares the secret with person 3.
At time 2, neither person 1 nor person 2 know the secret.
At time 3, person 3 shares the secret with person 0 and person 1.
Thus, people 0, 1, and 3 know the secret after all the meetings.

## Exemplo 3

Input: n = 5, meetings = [[3,4,2],[1,2,1],[2,3,1]], firstPerson = 1
Output: [0,1,2,3,4]
Explanation:
At time 0, person 0 shares the secret with person 1.
At time 1, person 1 shares the secret with person 2, and person 2 shares the secret with person 3.
Note that person 2 can share the secret at the same time as receiving it.
At time 2, person 3 shares the secret with person 4.
Thus, people 0, 1, 2, 3, and 4 know the secret after all the meetings.

## Restrições 

- `2 <= n <= 10^5`  
- `1 <= meetings.length <= 10^5`  
- `meetings[i].length == 3`  
- `0 <= x_i, y_i <= n - 1`  
- `x_i != y_i`  
- `1 <= time_i <= 10^5`  
- `1 <= firstPerson <= n - 1`