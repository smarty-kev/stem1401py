"""
1. Download a big file
>50MB
CSV download, Video
2. open and read this big file
by chunk
3. comparing with read(), readlines()
"""


# read in chunks function
def read_in_chunks(file_path, chunk_size=1024*1024):
    file_object = open(file_path, "r")
    while True:
        chunk_data = file_object.read(chunk_size)
        if not chunk_data:
            break
        yield chunk_data


# using read() in chunks method
try:
    print(read_in_chunks("NCDB_2015.csv"), type(read_in_chunks("NCDB_2015.csv")))
except FileNotFoundError as fe:
    print(fe)
except Exception as e:
    print(e)


# normal readlines() method
with open("NCDB_2015.csv", "r") as csv_file:
    content = csv_file.readlines()
    # print(content, type(content))
    csv_file.close()
