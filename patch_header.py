# Trying to learn the concept of a patch using a sample Git header

patch_header = "@@ -25,3 +40,5 @@"

header_parts = patch_header.split(" ")
print(header_parts)

for part in header_parts:
    if part.startswith("+"):
        part = part.split(",")
        line_no = part[0][1:]

        print(line_no)
        print(part)


"""

🧠 What your code demonstrates

For:

@@ -25,3 +40,5 @@

you first get:

['@@', '-25,3', '+40,5', '@@']

Then you identify:

+40,5

Split it:

['+40', '5']

Then:

i[0][1:]

removes the +:

40

So:

40 → starting line number in the new file
5  → number of lines in the hunk

"""


"""
GitHub API patch
      ↓
Understand Git diff format
      ↓
Understand @@ header
      ↓
Extract new-file starting line
      ↓
Track lines
      ↓
Identify added lines
      ↓
Scan added code for secrets


"""
