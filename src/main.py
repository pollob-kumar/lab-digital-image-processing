from pathlib import Path
from PIL import Image

# Path (image jekhane ache tar bose path)
BASE_DIR = Path(r"E:\Pollob\Lab - Digital Image Processing\Satellite_Image_Enhancement")

# folder name and imageName
input_path = BASE_DIR / "input" / "Lenna_(test_image).png"
# output jekhane save hobe
output_dir = BASE_DIR / "output"
# jodi oporer line er output thake tahole true
output_dir.mkdir(exist_ok=True)

# output path a resize pic save korar jonno
output_path = output_dir / "resized.png"


print(BASE_DIR)
print(input_path)


# Read image (open korlam)
img = Image.open(input_path)

# Resize (resize korlam)
resized = img.resize((300, 300))

# Save (save korlam)
resized.save(output_path)

# sob thik thakle done dekhane and output path dekhabe
print("Done!")
print(output_path)