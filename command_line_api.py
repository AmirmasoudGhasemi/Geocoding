
from application.geocoder import Geocoder
from application.http_connection import HttpConnection


def perform_geocoding():
    http_connection = HttpConnection()
    geocoder = Geocoder(http_connection)
    address = input('What is the address?')
    if len(address) is 0:
        return None
    geocode_result = geocoder.geocode(address)
    return geocode_result



while True:
    interest = input('do you want to continue?[y/n]')
    while interest is not 'y' and interest is not 'n':
        interest = input('please just answer with y or n. do you want to continue?[y/n]')
    if interest is 'n':
        break
    elif interest is 'y':
        geocode_result = perform_geocoding()
        if geocode_result is None:
            print({
                'message': 'Please provide an address to geocode your request query string'})
        elif geocode_result.google_code is not 200 and geocode_result.here_code is not 200:
            print({
                'message': 'There are no geocoding services available for this address. Try again later.'})
        elif geocode_result.google_code is 200:
            print(geocode_result.google_coordinate)
        elif geocode_result.here_code is 200:
            print(geocode_result.here_coordinate)


