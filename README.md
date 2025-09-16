# image-captioning-and-segmentation with VOC2012-
📚 Image Captioning Project – Requirements
✅ Python Version:

Python 3.8 or higher

✅ Required Python Libraries:

Pillow

matplotlib

Install karne ka command:

pip install Pillow matplotlib

✅ Required Files & Folders Structure:

1️⃣ dataset/archive/VOC2012_train_val/JPEGImages/
 → Folder containing all images in .jpg format.

2️⃣ dataset/archive/captions.txt
 → Text file containing image filename and caption in this format:
  image_name.jpg <tab> startseq caption text endseq

 Example lines:
  2008_008681.jpg startseq a man riding a horse on the beach endseq
  2008_008682.jpg startseq a dog playing with a ball endseq

3️⃣ display_caption.py
 → Python script file that randomly selects an image and shows its caption.

✅ How to Run:

Install required libraries:

pip install Pillow matplotlib


Make sure folder structure and files are correct.

Run the script:

python display_caption.py

✅ Notes:

Captions in the file may contain special tokens like startseq and endseq. These are automatically removed by the script before displaying.

Random image and caption will be displayed each time script runs.
