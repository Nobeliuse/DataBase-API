from settings import db
from models import Device, Battery
from flask import jsonify


class DeviceAPI:

	@staticmethod
	def get_device(device_id):
		device = Device.query.get(device_id)
		if device:
			return jsonify({'id': device.id, 'title': device.title, 'batteries': [b.title for b in device.batteries]}), 200
		else:
			return jsonify({'error': 'Устройство не найдено'}), 404

	@staticmethod
	def create_device(device_data):
		device = Device(title=device_data['title'])
		if len(device_data['battery_id']) > 5:
			return jsonify({'error': 'Максимальное количество аккумуляторов - 5'}), 400

		if device_data['battery_id']:
			for one_battery in device_data['battery_id']:
				battery = Battery.query.get(one_battery)
				device.batteries.append( battery )
		db.session.add(device)
		db.session.commit()
		return jsonify({'id': device.id, 'title': device.title}), 201

	@staticmethod
	def update_device(device_id, updated_device_data):
		device = Device.query.get(device_id)
		if len(updated_device_data['battery_id']) > 5:
			return jsonify({'error': 'Максимальное количество аккумуляторов - 5'}), 400

		if device:
			device.title = updated_device_data['title']
			if updated_device_data['battery_id']:
				device.batteries = []
				for one_battery in updated_device_data['battery_id']:
					battery = Battery.query.get(one_battery)
					device.batteries.append( battery )

			db.session.commit()
			return jsonify({'message': 'Данные об устройстве успешно обновлены'}), 200
		else:
			return jsonify({'error': 'Произошла ошибка во время обновления записи'}), 404

	@staticmethod
	def delete_device(device_id):
		device = Device.query.get(device_id)
		if device:
			db.session.delete(device)
			db.session.commit()
			return jsonify({'message': 'Устройство удалено!'}), 200
		else:
			return jsonify({'error': 'Произошла ошибка во время удаления записи'}), 404


class BatteryAPI:

	@staticmethod
	def get_battery(battery_id):
		battery = Battery.query.get(battery_id)
		if battery:
			return jsonify({'id': battery.id, 'title': battery.title, 'device': battery.device_id}), 200
		else:
			return jsonify({'error': 'Аккумулятор не найден'}), 404

	@staticmethod
	def create_battery(battery_data):
		battery = Battery(title=battery_data['title'])
		db.session.add(battery)
		db.session.commit()
		return jsonify({'id': battery.id, 'title': battery.title}), 201

	@staticmethod
	def update_battery(battery_id, updated_battery_data):
		battery = Battery.query.get(battery_id)
		if battery:
			battery.title = updated_battery_data['title']
			db.session.commit()
			return jsonify({'message': 'Данные об аккумуляторе успешно обновлены'}), 200
		else:
			return jsonify({'error': 'Произошла ошибка во время обновления записи'}), 404

	@staticmethod
	def delete_battery(battery_id):
		battery = Battery.query.get(battery_id)
		if battery:
			db.session.delete(battery)
			db.session.commit()
			return jsonify({'message': 'Аккумулятор удален'}), 200
		else:
			return jsonify({'error': 'Произошла ошибка во время удаления записи'}), 404


class DataBaseAPI(DeviceAPI, BatteryAPI):
	pass


api = DataBaseAPI()
