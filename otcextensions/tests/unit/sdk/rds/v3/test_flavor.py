# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
from openstack.tests.unit import base

from otcextensions.sdk.rds.v3 import flavor

EXAMPLE = {
    "vcpus": "1",
    "ram": 2,
    "spec_code": "rds.mysql.c2.medium.ha",
    "instance_mode": "ha",
    "group_type": "normal",
    "version_name": [
        "8.0"
    ],
    "az_status": {
        "eu-de-02": "normal",
        "eu-de-01": "normal",
        "eu-de-03": "normal"
    },
    "az_desc": {
        "eu-de-02": "eu-de-02",
        "eu-de-01": "eu-de-01",
        "eu-de-03": "eu-de-03"
    }
}


class TestFlavor(base.TestCase):

    def test_basic(self):
        sot = flavor.Flavor()

        self.assertEqual('/flavors/%(datastore_name)s', sot.base_path)
        self.assertEqual('flavors', sot.resources_key)
        self.assertIsNone(sot.resource_key)

        self.assertTrue(sot.allow_list)
        self.assertFalse(sot.allow_fetch)
        self.assertFalse(sot.allow_create)
        self.assertFalse(sot.allow_delete)
        self.assertFalse(sot.allow_commit)
        self.assertDictEqual({'limit': 'limit',
                              'marker': 'marker',
                              'version_name': 'version_name',
                              'spec_code': 'spec_code'},
                             sot._query_mapping._mapping)

    def test_make_it(self):

        sot = flavor.Flavor(**EXAMPLE)
        self.assertEqual(EXAMPLE['spec_code'], sot.spec_code)
        self.assertEqual(EXAMPLE['spec_code'], sot.name)
        self.assertEqual(EXAMPLE['vcpus'], sot.vcpus)
        self.assertEqual(EXAMPLE['ram'], sot.ram)
        self.assertEqual(EXAMPLE['instance_mode'], sot.instance_mode)
        self.assertEqual(EXAMPLE['group_type'], sot.group_type)
        self.assertEqual(EXAMPLE['version_name'], sot.version_name)
        self.assertEqual(EXAMPLE['az_status'], sot.az_status)
        self.assertEqual(EXAMPLE['az_desc'], sot.az_desc)
