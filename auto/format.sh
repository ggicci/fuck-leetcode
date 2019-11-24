#!/usr/bin/env bash
# Format python source files in-place by using yapf tool in google's python
# convention.

set -o errexit
set -o pipefail
set -o nounset


print_usage() {
  echo "
Usage:
  $0 <filename>
"
}

main() {
  local filename="${1:-notset}"

  if [[ "${filename}" == "notset" ]]; then
    print_usage
    exit 1
  fi

  yapf -vv --style google -i "${filename}"
}

main "$@"

