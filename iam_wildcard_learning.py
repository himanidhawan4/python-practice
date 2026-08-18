"""
Python Progress Record
Topic: IAM Wildcard Detection

I worked on this while building the IAM wildcard check
for my DevSecOps security gate project.

Things I practiced:
- Regular expressions
- Multiline strings
- splitlines()
- for loops
- if conditions
- startswith()
- continue
- string slicing
- re.match()

The main thing I learned was how to combine these basic
Python concepts to process a GitHub PR patch and detect
IAM wildcard permissions.
"""


import re


"""
1. Regular Expression

I learned how to create a regex pattern for detecting
Action or Resource with a wildcard value.
"""

pattern = r'\s*(Action|Resource)\s*(=|:)\s*"\*"'

text = 'Action = "*"'

if re.match(pattern, text):
    print("IAM wildcard found")


"""
2. Multiline Strings

I learned how triple quotes can be used to store
multiple lines of text in a single string.

This was useful for representing a GitHub PR patch.
"""

patch = """@@ -0,0 +1,5 @@
+Action = "*"
+Resource = "*"
+Effect = "Allow"
"""


"""
3. splitlines()

I learned how to convert a multiline string into
individual lines so that I can process each line.
"""

lines = patch.splitlines()


"""
4. for loop and startswith()

I learned how to go through each line and check
whether it starts with a particular character.

In a Git diff, "+" represents an added line.
"""

for line in lines:

    if line.startswith("+"):
        print("Added line:", line)


"""
5. String slicing

I learned how to remove the first character from
a string using [1:].

Here it removes the "+" from an added Git diff line.
"""

for line in lines:

    if line.startswith("+"):

        content = line[1:]

        print("Actual content:", content)


"""
6. continue

I learned how continue can be used to skip the
current iteration of a loop.
"""

for line in lines:

    if line.startswith("@@"):
        continue

    print(line)


"""
7. Combining the concepts

Finally, I combined the concepts together.

I check only added lines, remove the "+" from them,
and then use regex to check whether Action or Resource
contains a wildcard.
"""

for line in lines:

    if line.startswith("+"):

        content = line[1:]

        if re.match(pattern, content):
            print("Wildcard detected:", content.strip())
