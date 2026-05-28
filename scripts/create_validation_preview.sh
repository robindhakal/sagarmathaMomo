#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
guid="$(uuidgen | tr '[:upper:]' '[:lower:]')"
preview_dir="$repo_root/validation-previews/$guid"
base_url="${PAGES_BASE_URL:-https://robindhakal.github.io/sagarmathaMomo}"

mkdir -p "$preview_dir"
cp "$repo_root/index.html" "$preview_dir/index.html"

perl -0pi -e 's#(<meta name="viewport" content="[^"]+" />)#$1\n  <base href="../../" />#' "$preview_dir/index.html"

printf '%s/validation-previews/%s/\n' "${base_url%/}" "$guid"
