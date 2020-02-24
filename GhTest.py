'''
GhTest.py
David Tsu
testing gh.py
'''

import unittest
import unittest.mock
import gh

class TestGh(unittest.TestCase):
    ''' for testing Gh.py '''

    @unittest.mock.patch('requests.get')
    def test_fetch_repo1(self, mock_me):
        ''' to test fetch_repo using Mock '''
        o = [{'name': 'hellogitworld'},
             {'name': 'helloworld'},
             {'name': 'Mocks'},
             {'name': 'Project1'},
             {'name': 'threads-of-life'}]
        mock_me.return_value.json.return_value = [{'name': 'hellogitworld'},
                                                  {'name': 'helloworld'},
                                                  {'name': 'Mocks'},
                                                  {'name': 'Project1'},
                                                  {'name': 'threads-of-life'}]
        self.assertEqual(gh.fetch_repo('https://api.github.com/users/richkempinski/repos'), o)

    @unittest.mock.patch('requests.get')
    def test_fetch_repo2(self, mock_me):
        ''' to test fetch_repo using Mock '''
        mock_me.return_value.json.return_value = 25
        self.assertRaises(ValueError, gh.fetch_repo, 'https://api.github.com/users/richkempinski/repos')

    @unittest.mock.patch('requests.get')
    def test_fetch_commit1(self, mock_me):
        ''' to test fetch_commit using Mock '''
        mock_me.return_value.json.return_value = [{'message': 'commit_1'},
                                                  {'message': 'commit_2, fixed readme'},]
        self.assertEqual(gh.fetch_commit('https://api.github.com/users/richkempinski/hellogitworld/commits'), 2)

    @unittest.mock.patch('requests.get')
    def test_fetch_commit2(self, mock_me):
        ''' to test fetch_commit using Mock '''
        mock_me.return_value.json.return_value = 25
        self.assertRaises(ValueError, gh.fetch_commit, 'https://api.github.com/users/richkempinski/hellogitworld/commits')

"""
    def test_get_data(self):
        ''' tests for get_data method'''
        o = {
            'hellogitworld': 2,
            'helloworld': 2,
            'Mocks': 2,
            'Project1': 2,
            'threads-of-life': 2
        }
        self.assertEqual(gh.get_data('richkempinski'), o)
"""

if __name__ == '__main__':
    print('Running gh_test.py testing suite.')
    unittest.main(exit = False, verbosity=2)