# [765. Minimizar a Propagação de Malware(Minimize Malware Spread)](https://leetcode.com/problems/minimize-malware-spread/)

**Dificuldade:** Difícil  
**Tópicos:** Grafos
**Descrição:**

Você recebe uma rede de `n` nós representada como uma matriz de adjacência  `n x n` chamada `graph`, onde o `i-ésimo` nó está diretamente conectado ao `j-ésimo` nó se `graph[i][j] == 1`.

Alguns nós em `initial` estão inicialmente infectados por um malware. Sempre que dois nós estão diretamente conectados, e pelo menos um desses dois nós está infectado pelo malware, ambos os nós serão infectados. Essa propagação de malware continuará até que nenhum outro nó possa ser infectado dessa maneira.

Suponha que `M(initial)` seja o número final de nós infectados na rede inteira após a propagação do malware parar. Você irá remover exatamente um nó da lista `initial`.

Retorne o nó que, se removido, minimizará `M(initial)`. Se múltiplos nós puderem ser removidos para minimizar `M(initial)`, retorne o nó com o menor índice.

Observação: Note que se um nó for removido da lista `inicial` de nós infectados, ele ainda poderá ser infectado posteriormente devido à propagação do malware.

---

## Exemplos:

### Exemplo 1:

**Entrada:** `graph = [[1,1,0],[1,1,0],[0,0,1]], initial = [0,1]`

**Saída:** `0`

### Exemplo 2:

**Entrada:** `graph = [[1,0,0],[0,1,0],[0,0,1]], initial = [0,2]`

**Saída:** `0`

### Exemplo 3:

**Entrada:** `graph = [[1,1,1],[1,1,1],[1,1,1]], initial = [1,2]`

**Saída:** `1`

---

## Restrições:

- `n == graph.length`
- `n == graph[i].length​`
- `2 <= n <= 300`
- `graph[i][j]` é `0` ou `1`.
- `graph[i][j] == graph[j][i]`
- `graph[i][i] == 1`
- `1 <= initial.length <= n`
- `0 <= initial[i] <= n - 1`
- Todos os inteiros em `initial` são únicos.