# projeto1
Projeto 1 Compex - Lucia e Maria

## Sobre o Desafio

Nesse desafio você deve criar uma API simples utilizando as tecnologias que tem mais afinidade ou que quer utilizar pra trabalhar a médio prazo. A API consiste em um gerenciador de tarefas onde deve ser possível:

- Adicionar uma nova tarefa.
- Listar as tarefas criadas.
- Marcar e desmarcar uma tarefa como concluída.
- Remover uma tarefa da listagem.
- Mostrar o progresso de conclusão das tarefas.

## Formato da Task

```tsx
Interface Task {
	id: string;
	name: string;
	isDone: boolean;
}
```

## Regras de Negócio

- Não deve ser possível criar duas tarefas iguais.
- Não deve ser possível alterar uma tarefa que não existe.
- Não deve ser possível remover uma tarefa que não existe.
