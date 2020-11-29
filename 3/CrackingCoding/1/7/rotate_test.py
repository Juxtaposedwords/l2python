from absl.testing import absltest
from absl.testing import parameterized
from rotate import rotate_return


class UnitTests(parameterized.TestCase):
    @parameterized.named_parameters(
        {
            'testcase_name': '2x2',
            'input': [
                [0, 0],
                [0, 1],
            ],
            'want': [
                [0, 0],
                [1, 0],
            ],
        }, {
            'testcase_name': '3x3',
            'input': [
                [1, 0, 1],
                [0, 1, 1],
                [0, 1, 1],
            ],
            'want': [
                [0, 0, 1],
                [1, 1, 0],
                [1, 1, 1],
            ],
        })
    def testRotate(self, input, want):
        self.assertEqual(rotate_return(input), want)


if __name__ == '__main__':
    absltest.main()
