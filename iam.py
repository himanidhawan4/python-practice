# cook your dish here
# cook your dish here
import re
value_hint1= r'\s*(Action|Resource)\s*(=|:)\s*"\*"'
value_hint2= r'\s*(Action|Resource)\s*(=|:)\s*"\*"'

patch = "@@ -0,0 +1,16 @@\n+resource \"aws_iam_policy\" \"sample_policy\" {\n+  name        = \"sample-pr-policy\"\n+  description = \"Sample IAM policy for security gate testing\"\n+\n+  policy = jsonencode({\n+    Version = \"2012-10-17\"\n+\n+    Statement = [\n+      {\n+        Effect   = \"Allow\"\n+        Action   = \"*\"\n+        Resource = \"*\"\n+      }\n+    ]\n+  })\n+}"
print(patch.splitlines())
patch=patch.splitlines()
for line in patch:
    print(line)
    if line.startswith(('-','+++','---','#')):
        continue
    elif line.startswith("@@"):
        line.split(" ")
        for i in line:
           if i.startswith("+"):
              i.split(",")
              lineno=i[0][1:]
    elif line.startswith("+") and not line.startswith("+++"):
        if re.match(value_hint,patch):
            
                
        
        
        

"""
line='@@ -0,0 +1,16 @@'
if line.startswith("@@"):
    line = line.split(" ")
    print(line)
    for i in line:
        if i.startswith("+"):
            i = i.split(",")
            print(i)
            lineno = int(i[0][1:])

    print(lineno)
"""
