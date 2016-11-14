import sys
sys.path.append('../')
from data_parsing.CSV_data_parser import UnitConverter
import unittest

class UnitConverterTest(unittest.TestCase):
    def testDateConvert(self):
        inp = '2015-08-21'
        resulteu = UnitConverter.convertToOpen('lastupdate', inp, 'eu')
        resultnasa = UnitConverter.convertToOpen('lastupdate', inp, 'nasa')
        expected = '15/08/21'
        self.assertEqual(resulteu, expected)
        self.assertEqual(resultnasa,expected)

    def testConvertEURA(self):
        inp = '45.7625'
        resulteu = UnitConverter.convertToOpen('rightascension', inp, 'eu')
        expected = '3.00000 3.00000 3.00000'
        self.assertEqual(resulteu, expected)

    def testConvertEUDEC(self):
        inp = '45.7625'
        resulteu = UnitConverter.convertToOpen('declination', inp, 'eu')
        expected = '3.00000 3.00000 3.00000'
        self.assertEqual(resulteu, expected)

    def testConvertNASARA(self):
        inp = '03h03m03s'
        resultnasa = UnitConverter.convertToOpen('rightascension', inp, 'nasa')
        expected = '03 03 03'
        self.assertEqual(resultnasa, expected)

    def testConvertNASADEC(self):
        inp = '-03h03m03s'
        resultnasa = UnitConverter.convertToOpen('declination', inp, 'nasa')
        expected = '-03 03 03'
        self.assertEqual(resultnasa, expected)

if __name__ == '__main__':
    unittest.main(exit=False)