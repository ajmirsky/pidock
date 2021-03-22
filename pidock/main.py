import sys
import subprocess
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

scripts = {
    'extract': os.path.join(dir_path, 'support/1-extract.sh'),
    'build': os.path.join(dir_path, 'support/2-build.sh'),
    'compose': os.path.join(dir_path, 'support/3-compose.sh'),
    'flash': os.path.join(dir_path, 'support/4-flash.sh'),
}


def run_script(script, args=[]):
    command = ['/bin/bash', scripts[script]] + args

    proc = subprocess.Popen(command)
    proc.wait()
    if proc.returncode == 0:
        return True
    else:
        print('Encountered error {} running {}'.format(
            proc.returncode,
            script
        ))
        return False


def main(args):
    dev_prompt_actions = ['all', 'flash']
    if args.action in dev_prompt_actions:
        print(
            'WARNING: This will overwrite the contents of {}'.format(
                args.dev
            )
        )
        response = input('Proceed? [y/N]: ')
        if response.lower() != 'y':
            print('aborting')
            return

    all_actions = [
        ('extract', lambda: run_script('extract', [args.img])),
        ('build', lambda: run_script('build', [args.passwd])),
        ('compose', lambda: run_script('compose', [args.host])),
        ('flash', lambda: run_script('flash', [args.device])),
    ]

    actions = None
    if args.action == 'all':
        actions = all_actions
    else:
        actions = [a for a in all_actions if a[0] == args.action]

    for action in actions:
        print('Doing {}'.format(action[0]))
        if not action[1]():
            print('Failed {}'.format(action[0]))
            break
