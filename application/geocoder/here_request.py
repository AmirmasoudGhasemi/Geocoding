import json
class HereRequest:
	def __init__(self, address, http_connection):
		self.config_loader()
		self.address = address
		self.http_connection = http_connection
		self.HOST = 'https://geocoder.cit.api.here.com'
		self.PATH = '/6.2/geocode.json'

	def config_loader(self):
		secrets_file = open('./secrets.json')
		self.config = json.loads(secrets_file.read())
		secrets_file.close()

	def perform_request(self):
		response = self.http_connection.get_url(self.HOST, self.PATH, self.params())

		return response

	def params(self):
		return {
			"searchtext": self.address,
			"app_id": self.config['here_app_id'],
			"app_code": self.config['here_app_code']
		}

	def extract_coordinates_from_response(self, response):
		json_data = response.json()
		if  len(json_data['Response']['View']) > 0 :

			coordinates = json_data['Response']['View'][0]['Result'][0]['Location']['DisplayPosition']
			return {
				'lat': coordinates['Latitude'],
				'lng': coordinates['Longitude']
			}
		else:
			return None


