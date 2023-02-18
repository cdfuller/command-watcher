# command-watcher

A script for continously running a shell command and printing the output when it's changed

## Usage
```
$ ./command_watcher.py --help
usage: command-watcher [-h] [-i INTERVAL] command

positional arguments:
  command               the command to run

optional arguments:
  -h, --help            show this help message and exit
  -i INTERVAL, --interval INTERVAL
                        interval in seconds to run the command, default: 2.5
```

### Examples
* Running a sql command every 10 seconds
```bash
$ ./command_watcher.py -i 10 psql -d db-name -c 'SELECT COUNT(*) FROM "users";'
```

## TODO
* Add alias support by adding shell support to subprocess.run
  * Do I need to check to see which shell the user is currently using?
