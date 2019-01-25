import unittest
from hm import get_next_n_slots, SAMPLE_INPUT_OUTPUTS, time_of_run


class TestNSlot(unittest.TestCase):
    def test_get_next_n_slots(self):
        for ip, expected_output in SAMPLE_INPUT_OUTPUTS:
            output = get_next_n_slots(ip, time_of_run)
            self.assertEqual(
                output, expected_output,
                'Incorrect next slot implementation')

def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestNSlot('test_get_next_n_slots'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())

#python3 -m unittest tests