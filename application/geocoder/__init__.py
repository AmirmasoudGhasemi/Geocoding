from application.geocoder.google_request import GoogleRequest
from application.geocoder.here_request import HereRequest
from application.geocoder.geocode_result import Geocode_result

class Geocoder:
	def __init__(self, http_connection):
		self.http_connection = http_connection

	def geocode(self, address):
		google_request = GoogleRequest(address, self.http_connection)

		here_request = HereRequest(address, self.http_connection)
		geocode_result = Geocode_result(google_request,here_request)
		return geocode_result
