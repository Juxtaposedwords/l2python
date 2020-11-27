from absl.testing import absltest
from absl.testing import parameterized
from mocky import Example
from unittest import mock
from typing import Any, Dict
import requests


class UnitTests(parameterized.TestCase):
    @parameterized.named_parameters({
        'testcase_name': 'happy path',
        'get_resp': 301,
        'want': {
            'value': 301,
        },
    })
    @mock.patch.object(requests, 'get')
    def testDivisor(self, fake_get, get_resp: int, want: Dict[str, Any]):
        fake_session = mock.Mock()
        fake_session.status_code = get_resp
        fake_get.return_value = fake_session
        self.assertEqual(want['value'], Example().Get(""))


if __name__ == '__main__':
    absltest.main()
