from absl.testing import absltest
from absl.testing import parameterized
from compression import compress

import sys
sys.tracebacklimit = 0


class UnitTests(parameterized.TestCase):
    @parameterized.named_parameters(
        {
            'testcase_name': 'some replacements',
            'input': 'aabcccccaaa',
            'want': 'a2b1c5a3',
        }, {
            'testcase_name': 'replacement is longer',
            'input': 'abcde',
            'want': 'abcde',
        })
    def testSalutations(self, input, want):
        self.assertEqual(compress(input), want)


if __name__ == '__main__':
    absltest.main()
