def get_loc_key():
    out_text = ''
    with open(in_file_path, "r", encoding="utf-8") as f:
        line = f.readline()
        while line:
            if line.find('_desc') != -1:
                line = f.readline()
                continue
            find_key = line.find(':0')
            # line = line.replace(line[find_key:], ' = 1')
            line = line[:find_key]
            out_text += line + '\n'
            print(line)
            line = f.readline()
    with open(out_file_path, "w", encoding="utf-8") as variable_name_w:
        variable_name_w.write(out_text)


get_loc_key()
