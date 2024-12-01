#!/usr/bin/python3
from main_pkg.format import Task, SUCCESS, FAIL, WARNING, INFO, BLANK

title = 'System Checks'
heading = Task('', '', title);
heading.PrintTitle();

## Successful Task
message = 'Check system for something'
task = Task(message, SUCCESS, title);
task.PrintMessage()

## Failed Task
message = 'Check something else'
task = Task(message, FAIL, title);
task.PrintMessage()

## Warning
task = Task('Foo Bar', WARNING, '');
task.PrintMessage()

## Info
Task('Informational', INFO, '').PrintMessage()
Task('Informational', BLANK, '').PrintMessage()
