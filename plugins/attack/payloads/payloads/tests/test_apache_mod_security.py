'''
test_apache_mod_security.py

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


class test_apache_mod_security(PayloadTestHelper):

    EXPECTED_RESULT = {'file': {'/etc/apache2/mods-available/mod-security.conf':
                                u'<IfModule security2_module>\n\t# Default Debian dir for modsecurity\'s persistent data\n\tSecDataDir /var/cache/modsecurity\n\n\t# Include all the *.conf files in /etc/modsecurity.\n\t# Keeping your local configuration in that directory\n\t# will allow for an easy upgrade of THIS file and\n\t# make your life easier\n\tInclude "/etc/modsecurity/*.conf"\n</IfModule>\n'},
                       'version': {u'2.6.3 ': 'Yes'}}

    def test_apache_mod_security(self):
        result = exec_payload(self.shell, 'apache_mod_security', use_api=True)
        self.assertEquals(self.EXPECTED_RESULT, result)
