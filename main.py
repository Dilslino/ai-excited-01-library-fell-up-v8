"""Copy the bundled entry image to the grader output directory.

Stdlib only. No rendering, no image libraries: the JPEG bytes are
copied verbatim to <MAKEFUN_OUTPUT_DIR>/entry.png.
"""

import os
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.jpg")

    try:
        with open(source, "rb") as handle:
            payload = handle.read()
    except OSError as exc:
        print("error: cannot read entry.jpg: %s" % exc, file=sys.stderr)
        return 1

    if not payload:
        print("error: entry.jpg is empty", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)

    target = os.path.join(out_dir, "entry.png")
    with open(target, "wb") as handle:
        handle.write(payload)

    print("wrote %s (%d bytes)" % (target, len(payload)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
