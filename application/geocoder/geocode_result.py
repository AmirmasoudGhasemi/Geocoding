
class Geocode_result:
    def __init__(self, google_request, here_request):

        # check "google" geocoding response
        response = google_request.perform_request()
        self.google_code=response.code
        if self.google_code is 200:                             #google is successful
            self.google_coordinate = google_request.extract_coordinates_from_response(response)
            if self.google_coordinate is None: #double-check Google request
                self.google_code  = 503
        else:                                                   #google is not successful
            self.google_coordinate = None


        # check "here" geocoding response:
        response = here_request.perform_request()
        self.here_code = response.code
        if response.code is 200:                                #here is successful
            self.here_coordinate = here_request.extract_coordinates_from_response(response)
            if self.here_coordinate is None: #double-check here request
                self.here_code  = 503
        else:
            self.here_coordinate = None

