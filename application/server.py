from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import json
from application.geocoder import Geocoder
from application.http_connection import HttpConnection

class Server(BaseHTTPRequestHandler):
	def do_GET(self):
		geocode_result = self.perform_geocoding()

		if geocode_result is None:
			self.send_json(400, {
				'message': 'Please provide an address to geocode your request query string (e.g. "?address=Google%20Headquarters")'
			})
		elif geocode_result.google_code is not 200 and geocode_result.here_code is not 200:
			self.send_json(503, {
				'message': 'There are no geocoding services available for this address. Try again later.'
			},)
		elif geocode_result.google_code is 200:
			self.send_json(200, geocode_result.google_coordinate)
		elif geocode_result.here_code is 200:
			self.send_json(200, geocode_result.here_coordinate)
		return

	def perform_geocoding(self):
		http_connection = HttpConnection()
		geocoder = Geocoder(http_connection)
		uri = urlparse(self.path)
		query = parse_qs(uri.query)

		if query.get('address') is None:
			return None

		geocode_result = geocoder.geocode(query['address'][0])
		return geocode_result

	def send_json(self, http_status_code, data):
		response_text = json.dumps(data)
		self.send_response(http_status_code)
		self.end_headers()
		self.wfile.write(response_text.encode('utf-8'))
		return