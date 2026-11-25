#!/usr/bin/env python3
"""Angry Judge: The Short Rant Contest — entry program.

Writes one short rant (the tournament winner from candidates.md) to
entry.txt inside the grader's output directory. Pure standard library:
the grading image ships no third-party packages.

The rant, in one breath: a CAPTCHA demands proof of humanity, the human
fails it twice, and the machines turn out to be in no hurry at all.
"""

import os
import sys

# The winning rant, kept as its three sentences so each one can be read
# (and, in the build session, scored) on its own. Joined with single
# spaces they reproduce the submitted text exactly.
SENTENCES = [
    "The CAPTCHA asked me to prove I'm not a robot by finding traffic lights, and I failed twice.",
    "Somewhere a machine is doing my job flawlessly while I sit here, a human, unable to identify a bus.",
    "The robots aren't coming. They're waiting for me to finish the test.",
]

RANT = " ".join(SENTENCES)


def check_gate(text):
    """Mirror the sealed gate: UTF-8 text of 1 to 400 characters,
    not only white space. Fail loudly here rather than be invalid there."""
    assert 1 <= len(text) <= 400, f"rant is {len(text)} characters"
    assert text.strip(), "rant is only white space"
    text.encode("utf-8")  # raises if it ever stops being encodable


def output_candidates():
    """Directories to try for the output file, best first."""
    dirs = []
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env_dir:
        dirs.append(env_dir)
    dirs.append("/output")
    dirs.append(os.path.join(os.getcwd(), "output"))
    return dirs


def main():
    check_gate(RANT)
    for directory in output_candidates():
        try:
            os.makedirs(directory, exist_ok=True)
            path = os.path.join(directory, "entry.txt")
            with open(path, "w", encoding="utf-8") as handle:
                handle.write(RANT)
            print(RANT)
            return 0
        except OSError:
            continue
    print("could not write entry.txt anywhere", file=sys.stderr)
    return 1


if __name__ == "__main__":
    sys.exit(main())
