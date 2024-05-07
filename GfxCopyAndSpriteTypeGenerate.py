import shutil
import os
# 复制dds文件
IO_path = r"C:\Users\21186\Documents\Paradox Interactive\Hearts of Iron IV\mod\SCW\IO"
in_file_path = r"C:\Users\21186\Documents\Paradox Interactive\Hearts of Iron IV\mod\SCW\IO\in.txt"
copy_gfx_file = r'C:\Users\21186\Documents\Paradox Interactive\Hearts of Iron IV\mod\SCW\IO\in'
copy_gfx_file_to_path = r'C:\Users\21186\Documents\Paradox Interactive\Hearts of Iron IV\mod\SCW\IO\out'
with open(in_file_path, "r", encoding="utf-8") as f:
    line = f.readline()
    while line:
        if line[0] == '\n' or line[0] == '#':
            line = f.readline()
            continue
        shutil.copy(copy_gfx_file + r'\core.dds', copy_gfx_file_to_path + '\\' + line[:-1] + '.dds')
        line = f.readline()
# 写入interface
gfx_file_path = r"C:\Users\21186\Documents\Paradox Interactive\Hearts of Iron IV\mod\SCW\IO\in"
# folder_path_out = r"gfx\interface\technologies"
folder_path_out = r"gfx\interface\equipmentdesigner\naval\modules\icons"
out_file_path = r"C:\Users\21186\Documents\Paradox Interactive\Hearts of Iron IV\mod\SCW\IO\out.txt"

out_text = 'spriteTypes = {\n'

for filename in os.listdir(copy_gfx_file_to_path):
    if filename.find('core') != -1:
        continue
    texture_file_path = folder_path_out + "/" + filename
    name = 'GFX_' + filename[:-4] + '_medium'
    # name = 'GFX_SMI_' + filename[:-4]

    out_text += '    spriteType = {\n        name = "%s"\n        textureFile = "%s"\n    }\n' % (name, texture_file_path)
out_text += '}'
out_text = out_text.replace('\\', '/')
with open(out_file_path, "w", encoding="utf-8") as variable_name_w:
    variable_name_w.write(out_text)
print(out_text)
