---
paths:
  - ".coder/**"
---

# Coder templates

The template for this repo lives in `.coder/templates/blog` and contains `main.tf`.

```bash
# Push a template from the current directory, which must contain main.tf
coder templates push -y template-name

# Push a template from a named directory
cd /path/to/templates/parent && coder templates push -d template-folder -y template-name

# Push with an update message
coder templates push -d template-folder -y -m "Update description" template-name

# This repo
cd .coder/templates && coder templates push -d blog -y blog
```

The template name goes at the END of the command. `-d` names the directory holding `main.tf`, and you must run the command from that directory's parent. `-y` skips the confirmation prompt.

These forms are wrong and fail:

- `coder templates push blog .coder/templates/blog/` — wrong argument order.
- `coder templates push --directory .coder/templates/blog/ blog` — wrong flag syntax.
