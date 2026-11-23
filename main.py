import os
import tempfile

LETTER = b"A"

def write_letter(letter, output_path):
    if letter != b"A" or len(letter) != 1:
        raise ValueError("letter must be exactly one byte: 'A'")
    parent = os.path.dirname(output_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    fd, tmp_path = tempfile.mkstemp(dir=parent or ".")
    try:
        with os.fdopen(fd, "wb") as f:
            f.write(letter)
        os.replace(tmp_path, output_path)
    except BaseException:
        try:
            os.unlink(tmp_path)
        except OSError:
            pass
        raise

def resolve_output_path():
    """Return the output path, honouring ENTRY_OUTPUT if set."""
    return os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")

def main():
    write_letter(LETTER, resolve_output_path())

if __name__ == "__main__":
    main()
