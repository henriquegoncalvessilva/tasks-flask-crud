from flask import Flask, jsonify, request

from models.task import Task

app = Flask(__name__)

tasks = []
task_id_control = 1


@app.route("/tasks", methods=["POST"])
def create_task():

    data = request.get_json()
    new_task = Task(
        id=len(tasks) + 1,
        title=data["title"],
        description=data.get("description", ""),
    )
    tasks.append(new_task)

    return jsonify({"message": "Nova tarefa adicionada"})


@app.route("/tasks", methods=["GET"])
def get_tasks():
    task_list = [task.to_dict() for task in tasks]

    response = {"tasks": task_list, "total_tasks": len(task_list)}

    return jsonify(response)


@app.route("/tasks/<int:id>", methods=["GET"])
def get_task_by_id(id):
    for task in tasks:
        if task.id == id:
            return jsonify(task.to_dict())

    return jsonify({"message": "A task informada não foi encontrada"}), 404


@app.route("/tasks/<int:id>", methods=["PUT"])
def update_task(id):
    task = None
    if id is None:
        return jsonify({"message": "Informe qual task você está querendo editar."}), 404

    for t in tasks:
        if t.id == id:
            task = t

    if task is None:
        return jsonify({"message": "Tarefa não encontrada"}), 404

    data = request.get_json()

    task.title = data["title"]
    task.description = data["description"]
    task.completed = data["completed"]

    return jsonify({"message": "Tarefa atualizada com SUCESSO"})


@app.route("/tasks/<int:id>", methods=["DELETE"])
def delete_task(id):
    task = None
    for t in tasks:
        if t.id == id:
            task = t
            break

    if not task:
        return jsonify({"message": "Não foi possível encontrar a atividade"}), 404

    tasks.remove(task)

    return jsonify({"message": "Tarefa deletada com SUCESSO"})


if __name__ == "__main__":
    app.run(debug=True)
