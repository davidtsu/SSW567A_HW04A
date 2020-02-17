'''
gh_test.py
David Tsu
testing gh.py
'''

import unittest
import gh

class TestGh(unittest.TestCase):
    ''' for testing gh.py '''
    def test_get_data(self):
        ''' tests for get_data method '''
        o = {
            'hellogitworld': 2,
            'helloworld': 2,
            'Mocks': 2,
            'Project1': 2,
            'threads-of-life': 2
        }
        self.assertEqual(gh.get_data('richkempinski'), o)

if __name__ == '__main__':
    print('Running gh_test.py testing suite.')
    unittest.main(exit = False, verbosity=2)