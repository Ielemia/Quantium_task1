import unittest
from quantium_task4 import app  # Replace with your actual Dash app file name

class TestDashApp(unittest.TestCase):
    def test_header_presence(self):
        # Assuming that 'header' is the id of the HTML element in the layout
        self.assertIsNotNone(app.layout['header'])

        

    def test_visualization_presence(self):
        self.assertIsNotNone(app.layout['sales-graph'])

    def test_region_picker_presence(self):
        self.assertIsNotNone(app.layout['region-radio'])

if __name__ == '__main__':
    unittest.main()
