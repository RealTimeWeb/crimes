import unittest
from python.src import crimes


class TestCrimeDatabase(unittest.TestCase):

    def test_get_crime_info_online(self):

        crimes.connect()

        keys = ['AggravatedAssault', 'Burglary', 'ForcibleRape', 'LarcenyTheft',
                'Murder', 'Population', 'Property', 'Total', 'VehicleTheft',
                'Violent', 'Year']

        # Test getting one stock
        crime_info = crimes.get_crime_information("Year>1990 and Murder>24600")
        self.assertTrue(isinstance(crime_info, list))

        for dict_item in crime_info:

            intersection = set(keys).intersection(dict_item)
            self.assertEqual(11, len(intersection))