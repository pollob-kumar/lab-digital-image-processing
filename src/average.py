import cv2
import numpy as np
import os


# =========================
# 1. Input and Output Path
# =========================

input_folder = "input"
output_folder = "output"

input_path = os.path.join(input_folder, "image.png")
output_path = os.path.join(output_folder, "average_filtered.jpg")


# =========================
# 2. Read Image
# =========================

img = cv2.imread(input_path, 0)

if img is None:
    print("Image not found!")
    exit()


# =========================
# 3. Get Image Size
# =========================

rows, cols = img.shape


# =========================
# 4. Create Output Image
# =========================

output = np.zeros((rows, cols), dtype=np.uint8)


# =========================
# 5. Create 3x3 Average Mask
# =========================

mask = [
    [1/9, 1/9, 1/9],
    [1/9, 1/9, 1/9],
    [1/9, 1/9, 1/9]
]


# =========================
# 6. Apply Average Filter
# =========================

for i in range(1, rows - 1):

    for j in range(1, cols - 1):

        temp = (
            img[i-1, j-1] * mask[0][0]
            + img[i-1, j] * mask[0][1]
            + img[i-1, j+1] * mask[0][2]

            + img[i, j-1] * mask[1][0]
            + img[i, j] * mask[1][1]
            + img[i, j+1] * mask[1][2]

            + img[i+1, j-1] * mask[2][0]
            + img[i+1, j] * mask[2][1]
            + img[i+1, j+1] * mask[2][2]
        )

        output[i, j] = temp


# =========================
# 7. Create Output Folder
# =========================

os.makedirs(output_folder, exist_ok=True)


# =========================
# 8. Save Output Image
# =========================

cv2.imwrite(output_path, output)

print("Average filtering completed.")
print("Output saved at:", output_path)