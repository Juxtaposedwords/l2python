from absl.testing import absltest
from absl.testing import parameterized
from hello import Salutations

class AddedValueTests(parameterized.TestCase):
    @parameterized.named_parameters(
        {
        'testcase_name': 'one and only one',
        'num_count': 1,
        'name': 'foo',
        'want' : ['hello, '],})
    def testSalutations(self, num_count, name, want):
        got = Salutations(num_count,name)
        self.assertEqual(got, want)