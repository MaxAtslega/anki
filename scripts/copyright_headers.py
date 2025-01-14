# Copyright: Ankitects Pty Ltd and contributors
# License: GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html

import os
import sys
from pathlib import Path

nonstandard_header = {
    "pylib/anki/_vendor/stringcase.py",
    "pylib/anki/importing/pauker.py",
    "pylib/anki/importing/supermemo_xml.py",
    "pylib/anki/statsbg.py",
    "pylib/tools/protoc-gen-mypy.py",
    "python/pyqt/install.py",
    "qt/aqt/mpv.py",
    "qt/aqt/winpaths.py",
    "qt/package/build.rs",
    "qt/package/src/main.rs",
}

ignored_folders = [
    "bazel-",
    "qt/forms",
    "node_modules",
]

if not os.path.exists("WORKSPACE"):
    print("run from workspace root")
    sys.exit(1)

found = False
for dirpath, dirnames, fnames in os.walk("."):
    dir = Path(dirpath)

    ignore = False
    for folder in ignored_folders:
        if folder in dirpath:
            ignore = True
            break
    if ignore:
        continue

    for fname in fnames:
        for ext in ".py", ".ts", ".rs", ".svelte":
            if fname.endswith(ext):
                path = dir / fname
                with open(path) as f:
                    top = f.read(256)
                    if not top.strip():
                        continue
                    if str(path) in nonstandard_header:
                        continue
                    if fname.endswith(".d.ts"):
                        continue
                    if "Ankitects Pty Ltd and contributors" not in top:
                        print("missing standard copyright header:", path)
                        found = True

if found:
    sys.exit(1)
