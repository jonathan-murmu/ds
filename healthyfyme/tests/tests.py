import unittest
from n_slots import get_next_n_slots
from tests.test_data import (
    SAMPLE_INPUT_OUTPUTS_1, SAMPLE_INPUT_OUTPUTS_2, SAMPLE_INPUT_OUTPUTS_3,
    time_of_run_1, time_of_run_2, time_of_run_3
)


class TestNSlot(unittest.TestCase):
    def test_get_next_n_slots(self):
        for ip, expected_output in SAMPLE_INPUT_OUTPUTS_1:
            output = get_next_n_slots(ip, time_of_run_1)
            self.assertEqual(
                output, expected_output,
                'Incorrect next slot implementation for {0}'.format(time_of_run_1))
        
        # Time of run falls in between the week
        for ip, expected_output in SAMPLE_INPUT_OUTPUTS_2:
            output = get_next_n_slots(ip, time_of_run_2)
            self.assertEqual(
                output, expected_output,
                'Incorrect next slot implementation for {0}'.format(time_of_run_2))
        
        # Time of run falls in between the week and in between of the input times
        for ip, expected_output in SAMPLE_INPUT_OUTPUTS_3:
            output = get_next_n_slots(ip, time_of_run_3)
            self.assertEqual(
                output, expected_output,
                'Incorrect next slot implementation for {0}'.format(time_of_run_3))


def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestNSlot('test_get_next_n_slots'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())

#python3 -m unittest tests