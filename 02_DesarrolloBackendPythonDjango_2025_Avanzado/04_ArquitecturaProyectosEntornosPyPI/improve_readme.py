import re
import os

file_path = r'c:\Users\GlenaCDNP-Leonard\Documents\CursosBackendPython\02_DesarrolloBackendPythonDjango_2025_Avanzado\04_ArquitecturaProyectosEntornosPyPI\README.MD'

with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
toc = ["## Tabla de Contenidos\n"]
in_code_block = False

# Regex for questions (simple heuristic)
question_pattern = re.compile(r'^\*{0,2}¿.*?\?\*{0,2}$')

for line in lines:
    stripped = line.strip()
    
    # 1. Handle Code Blocks
    if stripped.startswith('```'):
        if not in_code_block:
            # Start of block
            if len(stripped) == 3: # Just ```
                new_lines.append('```python\n')
            else:
                new_lines.append(line) # Already has lang or is generic
            in_code_block = True
        else:
            # End of block
            new_lines.append(line)
            in_code_block = False
        continue
    
    if in_code_block:
        new_lines.append(line)
        continue

    # 2. Handle Headers for TOC
    if stripped.upper().startswith('## CLASE'):
        header_text = stripped.replace('#', '').strip()
        anchor = header_text.lower().replace(' ', '-').replace(':', '').replace('.', '').replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u')
        toc.append(f"- [{header_text}](#{anchor})\n")
        new_lines.append(f"\n{stripped}\n") # Ensure spacing
        continue

    # 3. Handle Questions (Make Bold)
    if question_pattern.match(stripped):
        clean_text = stripped.replace('*', '')
        new_lines.append(f"\n**{clean_text}**\n")
        continue

    new_lines.append(line)

# Insert TOC
# Find where to insert TOC. Usually after the metadata table or Intro.
# Let's look for the first "## CLASE" and insert before it.
insert_idx = 0
for i, line in enumerate(new_lines):
    if line.strip().upper().startswith('## CLASE'):
        insert_idx = i
        break

if insert_idx > 0:
    final_content = new_lines[:insert_idx] + ['\n'] + toc + ['\n'] + new_lines[insert_idx:]
else:
    final_content = toc + ['\n'] + new_lines

# Write back
with open(file_path, 'w', encoding='utf-8') as f:
    f.writelines(final_content)

print("README.md updated successfully.")
