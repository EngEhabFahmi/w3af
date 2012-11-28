'''
test_list_kernel_modules.py

Copyright 2012 Andres Riancho

This file is part of w3af, w3af.sourceforge.net .

w3af is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation version 2 of the License.

w3af is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with w3af; if not, write to the Free Software
Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
'''
from plugins.attack.payloads.payloads.tests.payload_test_helper import PayloadTestHelper
from plugins.attack.payloads.payload_handler import exec_payload


class test_list_kernel_modules(PayloadTestHelper):

    EXPECTED_RESULT = set(['ext2', 'lp', 'snd', 'parport_pc', 'vesafb'])

    def test_list_kernel_modules(self):
        result = exec_payload(self.shell, 'list_kernel_modules', use_api=True)
        self.assertTrue(set(
            result.keys()).issuperset(self.EXPECTED_RESULT), result.keys())
