from flask import render_template, redirect, request
from settings import app, db
from db_api import api


@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/devices/<int:device_id>', methods=['GET'])
def get_device(device_id):
    return api.get_device(device_id)


@app.route('/devices', methods=['POST'])
def create_device():
    device_data = request.get_json()
    return api.create_device(device_data)


@app.route('/devices/<int:device_id>', methods=['PUT'])
def update_device(device_id):
    updated_device_data = request.get_json()
    return api.update_device(device_id, updated_device_data)


@app.route('/devices/<int:device_id>', methods=['DELETE'])
def delete_device(device_id):
    return api.delete_device(device_id)


@app.route('/batteries/<int:battery_id>', methods=['GET'])
def get_battery(battery_id):
    return api.get_battery(battery_id)


@app.route('/batteries', methods=['POST'])
def create_battery():
    battery_data = request.get_json()
    return api.create_battery(battery_data)


@app.route('/batteries/<int:battery_id>', methods=['PUT'])
def update_battery(battery_id):
    updated_battery_data = request.get_json()
    return api.update_battery(battery_id, updated_battery_data)


@app.route('/batteries/<int:battery_id>', methods=['DELETE'])
def delete_battery(battery_id):
    return api.delete_battery(battery_id)



if __name__ == '__main__':
    with app.app_context():
        database.create_all()
    app.run()
