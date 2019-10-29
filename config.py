# Copyright 2016 Hewlett Packard Enterprise Development Company, L.P.
#
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

import sys
import os
from pathlib import Path
# Load up the cfg module, which contains all the classes and methods
# you'll need.
from oslo_config import cfg

# Define an option group
horizon_group = cfg.OptGroup(name='horizon',
                         title='Horizon dashboard')

HorizonGroup = [
    cfg.StrOpt('url',
               help="URL to Horizon dashboard. In general, it is an address of proxy node"
               "or public address"),
    cfg.StrOpt('admin_username',
               help="Username for an administrative user"),
    cfg.StrOpt('admin_password',
               help="Password to use for an administrative user"),
]

# Register your config group
cfg.CONF.register_group(horizon_group)

# Register your options within the config group
cfg.CONF.register_opts(HorizonGroup, group=horizon_group)

# Process command line arguments.  The arguments tell CONF where to
# find your config file, which it loads and parses to populate itself.
cfg.CONF(sys.argv[1:])
