def add_desc(add_desc_mode=None):
    out_text = ''
    with open(in_file_path, "r", encoding="utf-8") as f:
        line = f.readline()
        while line:
            if len(line) < 2:
                line = f.readline()
                continue
            if line.find('_desc') != -1 or line.find('#') != -1:
                line = f.readline()
                continue
            out_text += line[:-1] + '\n'
            print(line[:-1])
            add_desc_str = ''
            if add_desc_mode == 'copy':
                find_key = line.find('"')
                add_desc_str = line[find_key + 1:-2]

            find_key = line.find(':')
            line = line[:find_key]
            desc_line = line + '_desc:0"' + add_desc_str + '"' + '\n'
            out_text += desc_line
            line = f.readline()
            print(desc_line[:-1])
    with open(out_file_path, "w", encoding="utf-8") as variable_name_w:
        variable_name_w.write(out_text)


add_desc('copy')
