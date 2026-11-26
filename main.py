"""Funniest sign on a haunted server room door.

The joke is the twist: the room is not haunted by a ghost, but by
the previous admin, who never really left. He kept root access,
he can still read the mail, and he silently grades every password
that goes past him. The sign on the door is effectively his own
notice to whoever walks in next.
"""

import os

# The single sign line. Kept as one plain string so the output is
# byte-for-byte identical on every run.
SIGN_LINE = (
    "WARNING: Haunted by the previous admin. "
    "He still has root, he reads your email, "
    "and he judges your passwords."
)

MAX_CHARS = 120


def checked_line():
    """Return the sign line after enforcing the bounty limits."""
    text = SIGN_LINE.strip()
    if not text:
        raise ValueError("entry line must not be only whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError(
            "entry line is %d characters, over the %d limit"
            % (len(text), MAX_CHARS)
        )
    return text


def main():
    os.umask(0o022)
    line = checked_line()
    out_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(line + "\n")
    # Only the output FILE is made world-readable. The /output
    # directory itself is root-owned in the grader, so it is
    # never chmodded here.
    os.chmod(out_path, 0o644)


if __name__ == "__main__":
    main()
