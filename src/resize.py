import cv2
import numpy as np
import os


# =========================
# 1. Input and Output Path
# =========================

input_folder = "input"
output_folder = "output"

input_path = os.path.join(input_folder, "image.png")
output_path = os.path.join(output_folder, "resized.jpg")


# =========================
# 2. Read Image
# =========================

img = cv2.imread(input_path)

if img is None:
    print("Image not found!")
    exit()


# =========================
# 3. Get Original Image Size
# =========================

rows, cols, channels = img.shape

print("Original Size:", cols, "x", rows)


# =========================
# 4. Resize Factor
# =========================

scale = 2

new_rows = rows * scale
new_cols = cols * scale


# =========================
# 5. Create Output Image
# =========================

output = np.zeros(
    (new_rows, new_cols, channels),
    dtype=np.uint8
)


# =========================
# 6. Nearest Neighbor Resize
# =========================

for i in range(new_rows):

    for j in range(new_cols):

        # Find corresponding pixel
        # from original image

        old_i = int(i / scale)
        old_j = int(j / scale)

        output[i, j] = img[old_i, old_j]


# =========================
# 7. Create Output Folder
# =========================

os.makedirs(output_folder, exist_ok=True)


# =========================
# 8. Save Resized Image
# =========================

cv2.imwrite(output_path, output)


print("Image resizing completed.")
print("New Size:", new_cols, "x", new_rows)
print("Output saved at:", output_path)