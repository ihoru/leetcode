from datetime import datetime
from pathlib import Path

from icecream import IceCreamDebugger


def ic_now():
    return f'{datetime.now().strftime("%H:%M:%S.%f")[:-3]} ic|> '



log_file = open(Path(__file__).parent / 'ic.log', 'a')


def log(value):
    print(value, file=log_file, flush=True)


class MyIceCreamDebugger(IceCreamDebugger):
    contextDelimiter = ' '

    def _formatContext(self, callFrame):
        _, line_number, _ = self._getContext(callFrame)
        return f'line {line_number: 3}'


ic = MyIceCreamDebugger(
    prefix='> ',
    outputFunction=log,
    includeContext=True,
)

log('=' * 100)
