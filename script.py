from geopy.geocoders import Nominatim
import json

class Finder():
        def __init__ (self, file_path):
            self.data = []
            self.geolocator = Nominatim(user_agent="my_user_agent")
            self.location_data = {}
            with open(file_path) as input_file:
                for line in input_file:
                    self.data.append(line.strip())


        def get_location_data(self):
            for location in self.data:
                loc = self.geolocator.geocode(location)
                self.location_data[location] = \
                        {"lat": loc.latitude, "long": loc.longitude, "coordinate": (loc.latitude, loc.longitude)}

        def output_location_data(self, output_file_path):
            if self.location_data == {}:
                self.get_location_data()
            json_location_data = json.dumps(self.location_data, indent=4)
            with open(output_file_path, "w") as output_file:
                output_file.write(json_location_data)

            print(json_locatin_data)


finder = Finder("input.txt")
finder.output_location_data("output.txt")

