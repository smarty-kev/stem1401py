"""
Do research on how to update the content of a specified line
Solution examples
"""

"""
readlines() -> only for small files (otherwise, can crash the system)
readline() -> good to save memory, but that the only benefit
read in chunks -> read(size)
1MB = 1024*1024
"""


# read multiple lines
def read_in_chunks(file_path, chunk_size=1024*1024):
    file_object = open(file_path)
    while True:
        chunk_data = file_object.read(chunk_size)
        if not chunk_data:
            break
        yield chunk_data


def read_file_lines(file_path, line_start=1, line_end=-1):
    content_list = list()
    i = 1
    for chunk in read_in_chunks(file_path, 1024*1024*10):
        for tmp in chunk.split('\n'):
            if line_end != -1:
                if i >= line_start and i <= line_end:
                    content_list.append(tmp)
            else:
                if i >= line_start:
                    content_list.append(tmp)
            i += 1
    return content_list


# main
filepath = 'file5_mode_r.txt'
content = read_file_lines(filepath, line_start=2, line_end=4)
print(content)
