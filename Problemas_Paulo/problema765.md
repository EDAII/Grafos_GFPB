# [765. Casais de Mãos Dadas(Couples Holding Hands)](https://leetcode.com/problems/couples-holding-hands/)

**Dificuldade:** Difícil  
**Tópicos:** Grafos
**Descrição:**

Existem `n` casais sentados em `2n` assentos dispostos em uma fileira e eles querem dar as mãos.

As pessoas e os assentos são representados por um array de inteiros chamado `row`, onde `row[i]` é o ID da pessoa sentada no `i-ésimo` assento. Os casais são numerados em ordem, sendo o primeiro casal `(0, 1)`, o segundo casal  `(2, 3)` e assim por diante, sendo o último casal `(2n - 2, 2n - 1)`.

Retorne o número mínimo de trocas necessárias para que cada casal esteja sentado lado a lado. Uma troca consiste em escolher quaisquer duas pessoas, que então se levantam e trocam de assento.

---

## Exemplos:

### Exemplo 1:

**Entrada:** `row = [0,2,1,3]`

**Saída:** `1`

**Explicação:** `Precisamos apenas trocar a segunda pessoa (row[1]) e a terceira pessoa (row[2]).`

### Exemplo 2:

**Entrada:** `row = [3,2,0,1]`

**Saída:** `0`

**Explicação:**  `Todos os casais já estão sentados lado a lado.`

---

## Restrições:

- `2n == row.length`
- `2 <= n <= 30​​​​​​​`
- `0 <= row[i] < 2n`
- Todos os elementos de `row` são únicos.