from absl.testing import absltest
from absl.testing import parameterized


   @parameterized.named_parameters(
       {
           'testcase_name': 'one and only one',
           'num_count': 1,
           'name': 'foo',
           'want' : ['hello, foo']})
    def testSalutations(self, num_count, name, want):
        got = salutations(num_count,name)
        self.assertEqual(got, want)