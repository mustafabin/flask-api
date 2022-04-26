from flask import Flask, request, jsonify
from models import *
from playhouse.shortcuts import model_to_dict, dict_to_model

app = Flask(__name__)

@app.route('/carperson/', methods=['GET', 'POST'])
@app.route('/searchbyname/<name>', methods=['GET', 'PUT', 'DELETE'])
def endpoint(name=None):
    if request.method == 'GET':
        if name:
            return jsonify(model_to_dict(Person.get(Person.name == name)))
        else:
            peopleList = []
            for person in Person.select():
                peopleList.append(model_to_dict(person))
            return jsonify(peopleList)

    if request.method == 'PUT':
        req = request.get_json()
        Person.update(req).where(Person.name == name).execute()  # Execute the query, returning number of rows updated.
        return jsonify(model_to_dict(Person.get(Person.name == name)))


    if request.method == 'POST':
        new_person = dict_to_model(Person, request.get_json())
        new_person.save()
        return jsonify({"success": True})

    if request.method == 'DELETE':
        return jsonify(Person.get(Person.name == name).delete_instance())

@app.route('/bestcar/', methods=['GET'])
def bestcar():
    return jsonify({"car":"Toyata rav4"})
app.run(debug=True)