#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File: test_towerlib.py
#
# Copyright 2018 Ilija Matoski
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to
#  deal in the Software without restriction, including without limitation the
#  rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
#  sell copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#  FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
#  DEALINGS IN THE SOFTWARE.
#

"""
test_towerlib_configuration
----------------------------------
Tests for `towerlib` module.

.. _Google Python Style Guide:
   http://google.github.io/styleguide/pyguide.html

"""

from betamax.decorator import use_cassette
from unittest import TestCase
from .helpers import get_tower
from towerlib import AuthFailed
from requests import Session
from towerlib import Tower as TowerOriginal


__author__ = '''Ilija Matoski <imatoski@schubergphilis.com>'''
__docformat__ = '''google'''
__date__ = '''2018-05-25'''
__copyright__ = '''Copyright 2018, Ilija Matoski'''
__credits__ = ["Ilija Matoski"]
__license__ = '''MIT'''
__maintainer__ = '''Ilija Matoski'''
__email__ = '''<imatoski@schubergphilis.com>'''
__status__ = '''Development'''  # "Prototype", "Development", "Production".

TOWER_VERSION = '6.1.0.0'
TOWER_NAME = 'tower'


class TestTowerlibCommon(TestCase):

    # @use_cassette('auth_failed_init', record='once')
    # def test_fail_auth(self, session):
    #     with self.assertRaises(Exception) as context:
    #         get_tower(session, user='none', password='what')
    #     self.assertRaises(Exception, context.exception)

    @use_cassette('configuration', record='once')
    def test_configuration(self, session):
        tower = get_tower()
        tower.session = session
        self.assertIsNotNone(tower)
        data = tower.configuration
        self.assertEqual(data.version, TOWER_VERSION)

    # @use_cassette('cluster', record='once')
    # def test_cluster(self, session):
    #     tower = get_tower()
    #     tower.session = session
    #     self.assertIsNotNone(tower)
    #     data = tower.cluster
    #     self.assertEqual(data.version, TOWER_VERSION)
    #     self.assertEqual(data.name, TOWER_NAME)
#
