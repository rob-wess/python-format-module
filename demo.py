#!/usr/bin/python3

from main_pkg import format

# Formatting Variables
success = "\033[0;32mSUCCESS\033[0m"   # Green
fail = "\033[0;31mFAIL\033[0m"         # Red
warning = "\033[0;33mWARNING\033[0m"   # Yellow
blank = "\033[0;39mNULL\033[0m"        # White

title = 'System Checks'
heading = format.Task('', '', title);
heading.PrintTitle();

## First Task (success)
message = 'Check system for something'
task = format.Task(message, success, title);
task.PrintMessage()

## Second Task (fail)
message = 'Check something else'
task = format.Task(message, fail, title);
task.PrintMessage()

## Third Task
task = format.Task('Foo Bar', warning, '');
task.PrintMessage()


