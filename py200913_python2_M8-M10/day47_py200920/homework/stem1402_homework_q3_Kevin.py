"""
3. Write a Python program to append text to a file and display the text.
"""

try:
    f = open("text_Kevin.txt", "a+")

    content = "This is the new content to add."
    f.write(content)
    print(f"[{content}] was added to the file [text_Kevin.txt]")
except FileNotFoundError as fe:
    print(fe)

except Exception as e:
    print(e)

finally:
    f.close()
