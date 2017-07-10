# -*- coding: utf-8 -*-

from giftwrap.utilities import *
from nose.tools import *

"""Tests for string_ending_in_period"""


def test__string_ending_in_period__empty__returns_empty():
    """utilities.string_ending_in_period('') returns ''
    """

    assert string_ending_in_period('') == ''


def test__string_ending_in_period__whitespace__returns_empty():
    """utilities.string_ending_in_period(<whitespace>) returns ''
    """

    assert string_ending_in_period(' \r\t\n') == ''


def test__string_ending_in_period__period__returns_period():
    """utilities.string_ending_in_period('.') returns '.'
    """

    assert string_ending_in_period('.') == '.'


def test__string_ending_in_period__ends_in_period__ends_in_period():
    """utilities.string_ending_in_period('Test.') returns 'Test.'
    """

    assert string_ending_in_period('Test.') == 'Test.'


def test__string_ending_in_period__ends_in_period_whitespace__ends_in_period():
    """utilities.string_ending_in_period('Test. ') returns 'Test.'
    """

    assert string_ending_in_period('Test. ') == 'Test.'


def test__string_ending_in_period__doesnt_end_in_period__ends_in_period():
    """utilities.string_ending_in_period('Test') returns 'Test.'
    """

    assert string_ending_in_period('Test') == 'Test.'


def test__string_ending_in_period__ends_in_whitespace__ends_in_period():
    """utilities.string_ending_in_period('Test \\r\\n\\t') returns 'Test.'
    """

    assert string_ending_in_period('Test \r\n\t') == 'Test.'
