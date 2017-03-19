#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Johan Tell
# Copyright (c) 2017 Johan Tell
#
# License: MIT
#

"""This module exports the Dogma plugin class."""

from SublimeLinter.lint import Linter, util


class Dogma(Linter):
    """Provides an interface to dogma."""

    syntax = ('Elixir', 'elixir')
    cmd = 'mix dogma --format=flycheck @'
    executable = 'elixir'
    version_args = '--version'
    version_re = r'(?P<version>\d+\.\d+\.\d+)'
    version_requirement = '>= 0.1'
    regex = (
        r'^.+?:(?P<line>\d+):((?P<col>\d+):)? '
        r'(?:(?P<error>[W])|(?P<warning>[R|F|C])): '
        r'(?P<message>.+)$'
    )
    multiline = False
    line_col_base = (1, 1)
    tempfile_suffix = None
    error_stream = util.STREAM_BOTH
    selectors = {}
    word_re = None
    defaults = {}
    inline_settings = None
    inline_overrides = None
    comment_re = None
