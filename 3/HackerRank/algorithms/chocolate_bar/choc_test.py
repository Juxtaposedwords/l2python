from absl.testing import absltest
from absl.testing import parameterized
from typing import Any, Dict
from choc import splitter


class UnitTests(parameterized.TestCase):

    @parameterized.named_parameters(
        {
            'testcase_name': 'Exception due to split count being greather than possible options',
            'bar' : [10,2],
            'groups': 5,
            'want' : {
                'exception': ArithmeticError,
            },
        },{
            'testcase_name': 'choose earliest split when all things are equal',
            'bar': [1,1,1],
            'groups': 2,
            'want': {
                'value': [1],
            }
        },{
            'testcase_name': 'Happy path: smallest possible',
            'bar': [1,1,2],
            'groups': 2,
            'want': {
                'value': [1],
            }
        })
    def testBreak(self, bar: int, groups: int,  want: Dict[str,Any]):
        if 'exception' in want:
            with self.assertRaises(want['exception']):
                splitter(bar,groups)
        else:
            self.assertEqual(want['value'], splitter(bar, groups))
    

if __name__ == '__main__':
    absltest.main()
