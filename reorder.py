import os

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

order = [
    "blog-reforma-calderas.html",
    "blog-optimiza-caldera.html",
    "blog-corrida-financiera.html",
    "blog-checklist.html"
]

def get_file_for_line(line):
    for f in order:
        if f in line:
            return f
    return None

for f_name in html_files:
    try:
        with open(f_name, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            
        new_lines = list(lines)
        
        i = 0
        while i < len(new_lines) - 3:
            files_found = []
            lines_dict = {}
            
            is_block = True
            for j in range(4):
                f_match = get_file_for_line(new_lines[i+j])
                if f_match and f_match not in files_found:
                    files_found.append(f_match)
                    lines_dict[f_match] = new_lines[i+j]
                else:
                    is_block = False
                    break
                    
            if is_block and len(files_found) == 4:
                # We found a block of 4 lines! Sort them
                for j in range(4):
                    new_lines[i+j] = lines_dict[order[j]]
                i += 4
            else:
                i += 1

        with open(f_name, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)
    except Exception as e:
        print(f"Error on {f_name}: {e}")

print("Done reordering")
