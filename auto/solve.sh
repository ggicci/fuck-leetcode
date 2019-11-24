#!/usr/bin/env bash

set -o errexit
set -o pipefail
set -o nounset

SCRIPT_ROOT="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PROJECT_ROOT="$( dirname "${SCRIPT_ROOT}" )"
PROBLEMS_DB="${SCRIPT_ROOT}/problems.json"
LOOKUP="${SCRIPT_ROOT}/lookup.py"

usage() {
  >&2 echo "
  Usage: $0 <problem-number>
"
}

main() {
  local number="${1:-notset}"

  if [[ "${number}" == "" ]]; then
    usage
    exit 1
  fi

  # Check whether the problem number exists.
  local problem_json
  problem_json="$( "${LOOKUP}" "${number}" )" || exit $?

  local problem_id="$( "${LOOKUP}" "${number}" --context "${problem_json}" --field "id" )"
  local problem_title="$( "${LOOKUP}" "${number}" --context "${problem_json}" --field "title" )"
  local problem_slug="$( "${LOOKUP}" "${number}" --context "${problem_json}" --field "slug" )"
  local problem_difficulty="$( "${LOOKUP}" "${number}" --context "${problem_json}" --field "difficulty" )"

  local problem_dir="${PROJECT_ROOT}/leetcode-${problem_id}"
  mkdir -p "${problem_dir}"

  local solution_py="${problem_dir}/solution.py"

  # Detect clipboard content.
  local content="$( pbpaste )"

  if [[ "$( echo "${content}" | grep "class Solution:" )" == "" ]]; then
    content="" # reset
  fi

  if [[ ! -f "${solution_py}" ]]; then
    echo "# Leetcode Problem
#  - id: ${problem_id}
#  - title: ${problem_title}
#  - url: https://leetcode.com/problems/${problem_slug}/
#  - difficulty: ${problem_difficulty}

${content}
" > "${solution_py}"
  fi

  # Edit it.
  vim "${solution_py}"


  # Format it.
  yapf -vv --style google -i "${solution_py}"
}

main "$@"

