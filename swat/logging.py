#!/usr/bin/env python
# encoding: utf-8
#
# Copyright SAS Institute
#
#  Licensed under the Apache License, Version 2.0 (the License);
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#

'''
SWAT logging functions

'''

from __future__ import print_function, division, absolute_import, unicode_literals

import logging
import sys
from . import config as cf

default_level = 'warning'
default_format = '[%(levelname)s] %(message)s'

# Create global logger
logger = logging.getLogger(__name__)  
logger.setLevel(dict(
    debug=logging.DEBUG,
    info=logging.INFO,
    warning=logging.WARNING,
    error=logging.ERROR,
    critical=logging.CRITICAL,
)[default_level])
handler = logging.StreamHandler(sys.stderr)
handler.setFormatter(logging.Formatter(default_format))
logger.addHandler(handler)