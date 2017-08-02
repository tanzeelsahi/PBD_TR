

import unittest

from process_changes import Commit

class TestCommits(unittest.TestCase):

    def setUp(self):
        
        self.data = Commit()

    def test_first_commit(self):
        commit = get_commit_comment(self.data)
        self.assertEqual('Thomas', commit[0]['author'])
        self.assertEqual('r1551925', commit[0]['revision'])

if __name__ == '__main__':
    unittest.main()