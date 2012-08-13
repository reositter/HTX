#!/usr/bin/env python

import sublime
import sublime_plugin
import os

class RestartZpider(sublime_plugin.TextCommand):
    def run(self, edit, **args):
        os.system('net stop "Zpider Fusion Service"')
        os.system('net start "Zpider Fusion Service"')