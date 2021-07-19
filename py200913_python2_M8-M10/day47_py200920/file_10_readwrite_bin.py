"""

"""

import base64

with open("pic1.jpg", 'rb') as f:
    image_data = f.read()
    base64_data = base64.b64encode(image_data) # using base64
    print(base64_data)

f2 = open("imgfile", "w+")
f2.write(str(base64_data))
f2.close()
