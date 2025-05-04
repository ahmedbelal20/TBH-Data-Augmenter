# TBH Data Augmentation Generator

**TBH Data Augmentation Generator** is a Python-based GUI application that allows you to quickly apply various augmentation techniques to images for dataset expansion. This tool is ideal for machine learning practitioners and computer vision researchers looking to enrich their training data with minimal coding effort.

![TBH Data Augmentor](https://github.com/user-attachments/assets/4ed0d325-4014-4b3b-9bc6-081f5f2c0835)

---

## ✨ Features

- 📁 Easy image input and output handling
- 🎛️ Intuitive GUI built with Tkinter
- 🔄 Augmentation operations:
  - Random **Translation**
  - Random **Rotation**
  - Random **Scaling**
  - Random **Flipping**
  - Random **Blurring**
- 🖼️ Image preview using `matplotlib`
- 💾 Saves generated images in a new output directory

---

## 🚀 Getting Started

### 🔧 Requirements

- Python 3.x
- OpenCV (`cv2`)
- NumPy
- Matplotlib

Install the required packages using pip:

```bash
pip install opencv-python numpy matplotlib
```

---

## ▶️ Running the App
1- Clone the repository:
```bash
git clone https://github.com/your-username/tbh-data-augmentation.git
cd tbh-data-augmentation
```
2- Ensure you have an ```Input``` folder in the root directory and place your input image inside it.
3- Run the script:
```bash
python tbh_data_augmentation_generator.py
```
4- The GUI will open. Fill in the required fields:
  - Input image name (e.g., example.jpg)
  - Number of output images
  - Output folder name (optional, only if saving is enabled)
  - Select the transformations to apply
  - Click Generate

---

## 📁 Project Structure
```
.
├── Input/                   # Folder containing input image(s)
├── tbh_data_augmentation_generator.py
└── README.md
```

---

## 📝 Notes
- All generated images are resized to 300x300 pixels.
- The transformations are applied in the following order:
Translation → Rotation/Scaling → Flipping → Blurring
- Output filenames are numbered sequentially (e.g., 0.png, 1.png, ...)

---

## 📌 Limitations
- No batch processing — single image input at a time.
- Image format must be readable by OpenCV (e.g., JPG, PNG).
