from absl.testing import absltest
from absl.testing import parameterized
from sample import divisor


class UnitTests(parameterized.TestCase):
    @parameterized.named_parameters(
        {
            'testcase_name': 'Divided by zero',
            'input': 0,
            'want': {
                'exception': ZeroDivisionError,
            },
        }, {
            'testcase_name': 'Happy path',
            'input': 12,
            'want': {
                'got': 1,
            },
        })
    def testDivisor(self, input: int, want: dict):
        if 'exception' in want:
            with self.assertRaises(want['exception']):
                divisor(input)
        else:
            self.assertEqual(want['got'], divisor(input))


if __name__ == '__main__':
    absltest.main()
