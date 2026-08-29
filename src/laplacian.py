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
output_path = os.path.join(output_folder, "laplacian.jpg")


# =========================
# 2. Read Image
# =========================

# Image ta read korbe cv2.imread() use kore, "0" dara bujhai grayscale hisabe read kora and "img" variable a store korbe
img = cv2.imread(input_path, 0)

# Check korche, jodi image na thake tahole program exit hoye jabe.
if img is None:
    print("Image not found!")
    exit()


# Laplacian mask-a "-1" value ache, tai negative value handle korar jonno image-ke int32 te convert kora hocche
img = img.astype(np.int32)


# =========================
# 3. Get Image Size
# =========================

# Image er row and column ber kora. "shape"-use kore image size ber kora. ex: 500 × 800 (500 rows, 800 columns)
rows, cols = img.shape


# =========================
# 4. Create Output Image
# =========================

# Original image-er moto akoi size-er empty image create kora, jekhane pore filtered result rakha hobe
# "np.zeros((rows, cols))" eta rows × cols size-er ekta array create kore jar sob value 0
# "dtype=np.uint8" pixel values-ke 8-bit unsigned integer hisabe rakhbe
output = np.zeros((rows, cols), dtype=np.uint8)


# =========================
# 5. Create 3x3 Laplacian Mask
# =========================

# 3x3 Laplacian mask. Ei mask edge detect korar jonno use kora hoy.
mask = [
    [0, -1, 0],
    [-1, 4, -1],
    [0, -1, 0]
]


# =========================
# 6. Apply Laplacian Filter
# =========================

# "i" row er jonno. "range(1, rows - 1)" eta diye img er 'first & last' row bad diya hocche tai "i=1" theke start kora hoiche. karon border pixel-a kaj kora jabe na.
for i in range(1, rows - 1):

    # "j" column er jonno. "range(1, cols - 1)" eta diye img er 'first & last' column bad diya hocche "j=1" theke start kora hoiche. karon border pixel-a kaj kora jabe na.
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

        # Laplacian calculation-er por temp-er value negative ba 255-er beshi hote pare.
        # Tai value-ke 0 theke 255 er moddhe rakha hocche.
        temp = max(0, min(255, temp))

        # Filter korar por temp-er value "output" empty image-a store kora.
        output[i, j] = temp


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

print("Laplacian filtering completed.")
print("Output saved at:", output_path)