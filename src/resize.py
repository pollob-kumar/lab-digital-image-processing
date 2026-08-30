import cv2
import numpy as np
import os


# =========================
# 1. Input and Output Path
# =========================

# Parent Path
# "../" eta mane bujhai present-folder theke ek dhap oporer folder. (2-ta folder er jonno "../../input", 3-ta folder er jonno "../../../input")
input_folder = "../input"
output_folder = "../output"

# Image er name, Parent Path er vitore
input_path = os.path.join(input_folder, "Lenna_(test_image).png")
output_path = os.path.join(output_folder, "resized.jpg")


# =========================
# 2. Read Image
# =========================

# Image ta read korbe cv2.imread() use kore and "img" variable-a store korbe
img = cv2.imread(input_path)

# Check korche, jodi image na thake tahole program exit hoye jabe.
if img is None:
    print("Image not found!")
    exit()


# =========================
# 3. Get Original Image Size
# =========================

# Image er row, column and channel ber kora.
# "shape"-use kore image size ber kora. ex: 500 × 800 × 3
# ekhane 500 = rows, 800 = columns and 3 = RGB/BGR color channels
rows, cols, channels = img.shape

print("Original Size:", cols, "x", rows)


# =========================
# 4. Resize Factor
# =========================

# Image-ke 2 gun boro korar jonno scale factor 2 use kora hocche
scale = 2

# New image-er row and column ber kora
new_rows = rows * scale
new_cols = cols * scale


# =========================
# 5. Create Output Image
# =========================

# New size-er ekta empty image create kora, jekhane pore resized result rakha hobe
# "np.zeros()" eta sob value 0 diye new image create kore
# "new_rows, new_cols" dara new image-er size bujhai
# "channels" dara color channel bujhai
# "dtype=np.uint8" pixel values-ke 8-bit unsigned integer hisabe rakhbe
output = np.zeros(
    (new_rows, new_cols, channels),
    dtype=np.uint8
)


# =========================
# 6. Nearest Neighbor Resize
# =========================

# "i" new image-er row er jonno
for i in range(new_rows):

    # "j" new image-er column er jonno
    for j in range(new_cols):

        # New image-er protita pixel-er jonno original image-er corresponding pixel ber kora hocche
        # "int(i / scale)" diye original image-er row ber kora hocche
        # "int(j / scale)" diye original image-er column ber kora hocche
        old_i = int(i / scale)
        old_j = int(j / scale)

        # Original image-er corresponding pixel-ke output image-a store kora
        output[i, j] = img[old_i, old_j]


# =========================
# 7. Create Output Folder
# =========================

# output jekhane save hobe sei path check korbe, na thakle create korbe.
os.makedirs(output_folder, exist_ok=True)


# =========================
# 8. Save Output Image
# =========================

# "output" image-take "output_path" location-a save kora
cv2.imwrite(output_path, output)

print("Image resizing completed.")
print("New Size:", new_cols, "x", new_rows)
print("Output saved at:", output_path)