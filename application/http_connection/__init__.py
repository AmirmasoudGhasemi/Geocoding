import urllib.request
import urllib.parse
from application.http_connection.response import Response

class HttpConnection:
	def get_url(self, host, path, parameters):
		full_url = '{0}{1}?{2}'.format(host, path, urllib.parse.urlencode(parameters))
		try:
			request_handler = urllib.request.urlopen(full_url)
		except urllib.request.URLError as e:
			return Response(None, e)
		else:
			return Response(request_handler, None)
