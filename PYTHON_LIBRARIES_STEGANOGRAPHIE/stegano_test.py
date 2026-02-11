import cv2
import random
                
"""
    
bits = [
    0,1,0,0,1,0,0,0,   # 'H' = 72
    0,1,1,0,1,0,0,1    # 'i' = 105
]

buffer = 0          # octet en construction
count = 0           # nombre de bits dans buffer
result = bytearray()

for bit in bits:
    buffer = (buffer << 1) | bit
    count += 1

    if count == 8:
        result.append(buffer)
        buffer = 0
        count = 0

print(result)
result = bytearray()
print(result)

# Conversion finale
# message = result.decode("utf-8")
# print(message)  # Hi                
    
'''
#lsb_basic(image, "salut", 32, 2)
len = 16
bin = format(800, '0' + str(len) + 'b')
print(bin)


c = 'c'

code = ord(c)                 # 72
binary = format(800, '32b')  # '01001000'
print(len(binary))
# bits = [int(b) for b in binary]
# print(bits)
print(binary)
for b in binary:
    print(b)

print(binary[30] == '0')

"""

"""
img1 = cv2.imread("../DB_STEGANOGRAPHIE/BOSSbase_1.01/1.pgm", cv2.IMREAD_UNCHANGED)   # ou .jpg, .bmp, etc.

if img1 is None:
    print("Erreur : image non chargée")

print(img1.shape)


img2 = cv2.imread("../DB_STEGANOGRAPHIE/RGB-BMP Steganalysis Dataset/CALTECH-BMP-1500/C0001.bmp", cv2.IMREAD_UNCHANGED)   # ou .jpg, .bmp, etc.

if img2 is None:
    print("Erreur : image non chargée")

print(img2.shape)
"""


cle = 1234
n = 10
rCanal = random.Random(cle)
liste = [rCanal.randint(0, 2) for _ in range(n)]
print(liste)