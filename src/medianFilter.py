import cv2
import numpy as np
import os


# =========================
# 1. Input and Output Path
# =========================

# Parent Path
# "../" eta mane current folder theke ek dhap oporer folder.
input_folder = "../input"
output_folder = "../output"


# Image er name, Parent Path er vitore
input_path = os.path.join(input_folder, "Lenna_(test_image).png")
output_path = os.path.join(output_folder, "median_filtered.jpg")


# =========================
# 2. Read Image
# =========================

# Image ta read korbe cv2.imread() use kore.
# "0" dara bujhai grayscale (2ta value) hisabe image read kora.
img = cv2.imread(input_path, 0)


# Check korche, jodi image na thake tahole program exit hoye jabe.
if img is None:
    print("Image not found!")
    exit()


# =========================
# 3. Get Image Size
# =========================

# img.shape theke image er total row ebong column ber kora.
rows, cols = img.shape


# =========================
# 4. Create Empty Output Image
# =========================

# Original image er moto same size er ekta empty image create kora.
# Prothome sob pixel er value 0 thakbe.
output = np.zeros((rows, cols), dtype=np.uint8)


# =========================
# 5. Apply Median Filter
# =========================

# "i" row er jonno.
# "range(1, rows - 1)" eta diye image er first & last row
# bad diya "i=1" theke start kora hoiche.
# Karon 3x3 mask er jonno border pixel-a kaj kora jabe na.
for i in range(1, rows - 1):

    # "j" column er jonno.
    # "range(1, cols - 1)" eta diye image er first & last column
    # bad diya "j=1" theke start kora hoiche.
    for j in range(1, cols - 1):

        # 3x3 neighborhood er 9ta pixel ekta list-a store kora.
        pixels = [
            img[i-1, j-1],
            img[i-1, j],
            img[i-1, j+1],

            img[i, j-1],
            img[i, j],
            img[i, j+1],

            img[i+1, j-1],
            img[i+1, j],
            img[i+1, j+1]
        ]


        # =========================
        # 6. Sort the 9 Pixel Values
        # =========================

        # 9ta pixel value choto theke boro krome sajano hobe.
        # Built-in sorted() function use na kore manually sort kora hocche.
        for x in range(8):

            for y in range(8 - x):

                # Jodi ager value porer value theke boro hoy,
                # tahole duita value swap kora hobe.
                if pixels[y] > pixels[y + 1]:

                    temp = pixels[y]
                    pixels[y] = pixels[y + 1]
                    pixels[y + 1] = temp


        # =========================
        # 7. Find Median Value
        # =========================

        # 9ta value sort korar por middle value holo index 4.
        # Tai pixels[4] holo Median value.
        median = pixels[4]


        # Filter korar por median value "output" empty image-a store kora.
        output[i, j] = median


# =========================
# 8. Create Output Folder
# =========================

# Output folder na thakle automatically create korbe.
os.makedirs(output_folder, exist_ok=True)


# =========================
# 9. Save Output Image
# =========================

# Filtered image-ta output folder-a save kora.
cv2.imwrite(output_path, output)


print("Median filtering completed.")
print("Output saved at:", output_path)