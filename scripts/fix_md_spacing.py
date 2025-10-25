"""Fix markdown spacing for Games101 lecture files.

Rules applied:
- Ensure a blank line before any heading (lines starting with '#').
- Ensure blank line before and after fenced code blocks (```), and before/after indented code blocks.
- Ensure images (lines containing ![...](...)) are on their own line with a blank line before and after.
- Normalize multiple blank lines down to a single blank line.

Run from repository root: python scripts/fix_md_spacing.py
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGET_DIR = ROOT / 'docs' / 'Games101'

md_files = list(TARGET_DIR.rglob('*.md'))

heading_re = re.compile(r'^(#{1,6})\s')
image_re = re.compile(r'!\[.*?\]\(.*?\)')
code_fence_re = re.compile(r'^(```|~~~)')


def fix_content(text: str) -> str:
    lines = text.splitlines()
    out = []
    in_code = False

    for i, line in enumerate(lines):
        stripped = line.rstrip()

        # detect code fence start/end
        if code_fence_re.match(stripped):
            if not in_code:
                # ensure blank line before code fence
                if out and out[-1].strip() != '':
                    out.append('')
                out.append(stripped)
                in_code = True
                continue
            else:
                out.append(stripped)
                in_code = False
                # ensure blank line after code fence
                out.append('')
                continue

        if in_code:
            out.append(line)
            continue

        # headings: ensure blank line before
        if heading_re.match(stripped):
            if out and out[-1].strip() != '':
                out.append('')
            out.append(stripped)
            continue

        # images: put them on their own line, ensure blank lines around
        if image_re.search(stripped):
            # if current line contains other text besides the image, try to separate
            img_only = stripped.strip()
            # ensure blank line before
            if out and out[-1].strip() != '':
                out.append('')
            out.append(img_only)
            # ensure blank line after
            out.append('')
            continue

        # lists (start with -, *, + or numbered) - ensure previous line not merged with paragraph when necessary
        if re.match(r'^(\s*[-*+]\s+|\s*\d+\.\s+)', stripped):
            if out and out[-1].strip() == '':
                out.append(stripped)
            else:
                # if previous line is text, keep it but add blank line before list
                if out and out[-1].strip() != '':
                    out.append('')
                out.append(stripped)
            continue

        # regular line
        out.append(stripped)

    # normalize multiple blank lines -> single blank line
    normalized = []
    prev_blank = False
    for line in out:
        if line.strip() == '':
            if not prev_blank:
                normalized.append('')
            prev_blank = True
        else:
            normalized.append(line)
            prev_blank = False

    # ensure file ends with a single newline
    return '\n'.join(normalized).rstrip() + '\n'


def main():
    changed = []
    for md in md_files:
        # only process lecture files from 3 onward: match file names that contain 'Lecture - ' and a leading number >=3
        name = md.name
        m = re.match(r'Lecture - (\d+)', name)
        if m:
            num = int(m.group(1))
            if num < 3:
                continue
        else:
            # include other files under Games101 (like 作业) as well
            pass

        text = md.read_text(encoding='utf-8')
        new = fix_content(text)
        if new != text:
            md.write_text(new, encoding='utf-8')
            changed.append(str(md.relative_to(ROOT)))

    if changed:
        print('Modified files:')
        for p in changed:
            print('-', p)
    else:
        print('No changes needed.')


if __name__ == '__main__':
    main()
