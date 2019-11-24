#!/usr/bin/env python

import os
import sys
import json
from argparse import ArgumentParser

ROOT = os.path.dirname(os.path.abspath(__file__))
DB_FILE = os.path.join(ROOT, 'problems.json')


def parse_args():
    """Parse CLI tool options.
    """
    parser = ArgumentParser()
    parser.add_argument('problem_id', type=int)
    parser.add_argument('--field', type=str, help='extract field value')
    parser.add_argument('--markdown',
                        type=bool,
                        default=False,
                        help='print markdown content')
    parser.add_argument('--context',
                        type=str,
                        help='additional context to lookup')

    return parser.parse_args()


def lookup(problem_id: int, context: str = None):
    if context:
        # Find in context first.
        obj = json.loads(context)
        if int(obj.get('id', -1)) == problem_id:
            return obj

    with open(DB_FILE, 'r') as f:
        problems = json.load(f)

    index = {int(x['id']): x for x in problems}

    return index.get(problem_id)


def main():
    opts = parse_args()
    problem = lookup(opts.problem_id, context=opts.context)
    if not problem:
        sys.exit('Problem Not Found')

    # Add field "url" to problem.
    problem['url'] = f'https://leetcode.com/problems/{problem["slug"]}/'

    if opts.field:
        # Print field value only.
        value = problem.get(opts.field)
        if value is None:
            sys.exit('Field Not Found')
        print(value)
        return

    if opts.markdown is True:
        print(f'[{problem["id"]} - {problem["title"]}]({problem["url"]})')
        return

    print(json.dumps(problem, indent=4))


if __name__ == '__main__':
    main()
