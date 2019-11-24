#!/usr/bin/env python

import os
import json
import urllib.request

ROOT = os.path.dirname(os.path.abspath(__file__))
DB_FILE = os.path.join(ROOT, 'problems.json')


def main():
    req = urllib.request.Request(
        "https://leetcode.com/api/problems/all/",
        headers={
            'User-Agent':
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'
        },
    )

    problems = []
    with urllib.request.urlopen(req) as f:
        js = json.loads(f.read())
        for p in js['stat_status_pairs']:
            difficulty = {
                1: 'easy',
                2: 'medium',
                3: 'hard',
            }.get(p['difficulty']['level'], 'unknown')

            problems.append({
                'id': p['stat']['frontend_question_id'],
                'title': p['stat']['question__title'],
                'slug': p['stat']['question__title_slug'],
                'difficulty': difficulty,
            })

        problems.sort(key=lambda x: x['id'])

    with open(DB_FILE, 'wt') as f:
        json.dump(problems, f, indent=4)

    print(f'Database built: {DB_FILE}')


if __name__ == '__main__':
    main()
