document.addEventListener('DOMContentLoaded', function() {
    const taskInput = document.querySelector('#new-task');
    const addTaskButton = document.querySelector('#add-task');
    const tasksContainer = document.querySelector('.conteudo__taks__main');

    // Carregar tarefas salvas
    const savedTasks = JSON.parse(localStorage.getItem('tasks')) || [];

    function renderTasks() {
        tasksContainer.innerHTML = '';
        if (savedTasks.length === 0) {
            tasksContainer.innerHTML = `
                <div class="conteudo__taks__main_empty">
                    <img src="/assents/Clipboard (1).png" alt="Clipboard">
                    <p><strong>Você ainda não tem tarefas cadastradas</strong></p>
                    <p>Crie tarefas e organize seus itens a fazer</p>
                </div>
            `;
        } else {
            savedTasks.forEach((task, index) => {
                const taskElement = document.createElement('div');
                taskElement.classList.add('task');
                taskElement.innerHTML = `
                    <input type="checkbox" id="task-${index}" ${task.completed ? 'checked' : ''}>
                    <label for="task-${index}" ${task.completed ? 'style="text-decoration: line-through;"' : ''}>${task.text}</label>
                    <button class="remove-task">Remover</button>
                `;
                tasksContainer.appendChild(taskElement);

                // Marcar tarefa como concluída
                taskElement.querySelector('input').addEventListener('change', function() {
                    task.completed = !task.completed;
                    saveTasks();
                    renderTasks();
                });

                // Remover tarefa
                taskElement.querySelector('.remove-task').addEventListener('click', function() {
                    savedTasks.splice(index, 1);
                    saveTasks();
                    renderTasks();
                });
            });
        }
    }

    function saveTasks() {
        localStorage.setItem('tasks', JSON.stringify(savedTasks));
    }

    addTaskButton.addEventListener('click', function(event) {
        event.preventDefault();
        const taskText = taskInput.value.trim();
        if (taskText !== '') {
            savedTasks.push({ text: taskText, completed: false });
            saveTasks();
            renderTasks();
            taskInput.value = '';
        }
    });

    renderTasks();
});
