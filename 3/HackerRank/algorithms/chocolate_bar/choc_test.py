from absl.testing import absltest
from absl.testing import parameterized
from typing import Any, Dict, List
from choc import splitter
import sys
#sys.tracebacklimit = 0


class UnitTests(parameterized.TestCase):

    @parameterized.named_parameters(
        {
            'testcase_name': 'Unable to split into that many groups',
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
                'value': [2,1],
            }
        },{
            'testcase_name': 'small groups',
            'bar': [1,1,2],
            'groups': 2,
            'want': {
                'value': [2,2],
            }
        },{
            'testcase_name': '2 groups with 2:3 split',
            'bar': [1,1,2,1],
            'groups': 2,
            'want': {
                'value': [2,3],
            }
        },{
            'testcase_name': '2 groups with 4:3 split',
            'bar': [1,1,2,1,2],
            'groups': 2,
            'want': {
                'value': [4,3],
            }
        },{
            'testcase_name': '3 groups with large diff',
            'bar': [1,16,2,15,4],
            'groups': 3,
            'want': {
                'value': [17,17,4],
            }
        },
        )
    def testBreak(self, bar: List[int], groups: int,  want: Dict[str,Any]):
        if 'exception' in want:
            with self.assertRaises(want['exception']):
                splitter(bar,groups)
        else:
            self.assertItemsEqual(want['value'], splitter(bar, groups))
    

if __name__ == '__main__':
    absltest.main()
