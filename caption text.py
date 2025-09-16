import os
import random

# Example folder path where images are
images_dir = 'D:/image captioning- CNN (ANKIT)/dataset/archive/VOC2012_train_val/JPEGImages/'

# Output captions.txt file
output_file = 'D:/image captioning- CNN (ANKIT)/dataset/archive/captions.txt'

# Dummy captions (you can modify these as per real captions)
dummy_captions = [
    "startseq a man riding a horse on the beach endseq",
    "startseq a dog playing with a ball endseq",
    "startseq a person holding an umbrella in the rain endseq"
]

# Get list of image files
image_files = [f for f in os.listdir(images_dir) if f.endswith('.jpg')]

with open(output_file, 'w', encoding='utf-8') as f:
    for img_file in image_files:
        caption = random.choice(dummy_captions)
        f.write(f"{img_file}\t{caption}\n")

print(f"✅ captions.txt created with {len(image_files)} lines")
