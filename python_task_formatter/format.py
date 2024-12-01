import os

# Module-level constants for formatting
SUCCESS = "\033[0;32mSUCCESS\033[0m"   # Green
FAIL = "\033[0;31mFAIL\033[0m"         # Red
WARNING = "\033[0;33mWARNING\033[0m"   # Yellow
BLANK = "\033[0;39mNULL\033[0m"        # White
INFO = "\033[0;34mINFO\033[0m"         # Blue

class Task:

    def __init__(self, message, result, title):
        self.message = message
        self.result = result
        self.title = title

    def PrintMessage(self):
        dot = u'\u25Cf '
        termWidth = os.get_terminal_size()
        termSizePrint = termWidth.columns - 23
        messageLeng = (len(self.message))
        fullPrint = termSizePrint - messageLeng - 7
        periods = "." * fullPrint
        spaces = ' ' * 8
        fullString = spaces + dot + self.message + periods + self.result
        print('{:^0s}'.format(fullString))

    def PrintTitle(self):
        print("\n\033[1m" + self.title + "\033[0m\n")