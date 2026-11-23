import os

LETTER = b"A"

def write_letter(letter, output_path):
    if letter != b"A" or len(letter) != 1:
        raise ValueError("letter must be exactly one byte: 'A'")
    parent = os.path.dirname(output_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(output_path, "wb") as f:
        f.write(letter)
    os.chmod(output_path, 0o644)

def resolve_output_path():
    """Return the output path: ENTRY_OUTPUT overrides the full path;
    otherwise MAKEFUN_OUTPUT_DIR (set by the grader to /output) or
    /output is the directory, and the file is always entry.txt."""
    if "ENTRY_OUTPUT" in os.environ:
        return os.environ["ENTRY_OUTPUT"]
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(out_dir, "entry.txt")

def main():
    write_letter(LETTER, resolve_output_path())

if __name__ == "__main__":
    main()
