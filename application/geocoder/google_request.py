
class GoogleRequest:
	def __init__(self, address, http_connection):
		self.address = address
		self.http_connection = http_connection
		self.PATH = '/maps/api/geocode/json'
		self.HOST = 'https://maps.googleapis.com'

	def perform_request(self):
		response = self.http_connection.get_url(self.HOST, self.PATH, self.params())
		return response

	def params(self):
		return {
			"address": self.address
		}

	def extract_coordinates_from_response(self, response):
		data = response.json()
		if len(data['results']) > 0:
			return data['results'][0]['geometry']['location']
		else:
			return None
