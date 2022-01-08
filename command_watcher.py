#!/usr/bin/env python3
import argparse
import os
import shlex
import subprocess
import sys
import time

from datetime import datetime

class CommandWatcher:

    def __init__(self, command, interval, **kwargs):
        self.command = command
        self.interval = interval
        self.iterations = kwargs.get('iterations', -1)
        self.execution_count = 0

    def loop(self):
        while True:
            if self.execution_count - self.iterations:
                break
            else:
                self.execute()


    def execute(self):
        self.execution_count += 1


    def __repr__(self):
        command = shlex.join(self.command)
        return f"<CommandWatcher {self.interval}s cmd: {command}>" 


def forever(command, interval, repeat=False):
    print(f"Running command: {' '.join(command)}")
    previous = ""
    last_changed_time = None

    while True:
        completed = subprocess.run(command, capture_output=True, text=True)

        if repeat:
            print(completed.stdout, end='')

        elif completed.stdout != previous:
            last_changed_time = datetime.now()
            previous = completed.stdout

            print(f"\nChanged at {last_changed_time}")
            print(completed.stdout, end='')

        else:
            print('.', end='', flush=True)

        if completed.stderr:
            print("Error")
            print(completed.stderr)

        time.sleep(interval)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--interval', help="interval in seconds to run the command, default: 2.5", default=2.5, type=float)
    parser.add_argument('command', help="the command to run")
    parser.add_argument('command_args', nargs=argparse.REMAINDER, help=argparse.SUPPRESS)
    args = parser.parse_args()

    script = args.command
    command_args = args.command_args
    interval = args.interval
    
    cw = CommandWatcher([args.command] + args.command_args, interval)
    print(cw)

    try:
        forever([args.command] + args.command_args, interval)
    except KeyboardInterrupt:
        print("\nGoodbye!")
        sys.exit(0)
