"""
TBH DATA AUGMENTATION GENERATOR
"""

import os
import cv2
import numpy as np
import tkinter as tk
import random
import matplotlib.pyplot as plt

# Plot the image using plt.imshow
def plot_image(img):
    if img.ndim > 2:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        plt.imshow(img)
    else:
        plt.imshow(img, cmap="gray")
    plt.show()

# Resize the image to 300 x 300 pixels
def resize_image(img):
    resized_image = cv2.resize(img, (300,300))
    return(resized_image)

# Translate the image randomly
def translate_image(img):
    warp_x = random.randint(1, 75)
    warp_y = random.randint(1, 75)
    translation_matrix = np.float32([[1,0,warp_x],[0,1,warp_y]])
    translated_image = cv2.warpAffine(img, translation_matrix, (img.shape[1],img.shape[0]))
    return(translated_image)

# Rotate the image randomly
def rotate_and_scale_image(img, rotation, scaling):
    angle = random.randint(5, 355)
    center = (img.shape[1]//2, img.shape[0]//2)
    scale = random.uniform(0.6, 1.6)
    if rotation == 0:
        angle = 0
    if scaling == 0:
        scale = 1.0
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, scale)
    rotated_image = cv2.warpAffine(img, rotation_matrix, (img.shape[1],img.shape[0]))
    return(rotated_image)

#Flip the image randomly
def flip_image(img):
    flip = random.randint(-1,1)
    flipped_image = cv2.flip(img, flip)
    return(flipped_image)

# Blur the image randomly
def blur_image(img):
    size = random.randint(5,30)
    blurred_image = cv2.blur(img, ksize=(size,size))
    return(blurred_image)

# Generate a dataset based on the given inputs
def generate_images():
    # Retrieve tkinter variables
    input_image_name = tk_input_image_name.get()
    output_number = tk_output_number.get()
    output_folder = tk_output_folder.get()
    translation = tk_translation.get()
    rotation = tk_rotation.get()
    flipping = tk_flipping.get()
    scaling = tk_scaling.get()
    blurring = tk_blurring.get()
    save = tk_save.get()
    # Input directory and image
    input_folder = "Input"
    input_image_path = input_folder + "/" + input_image_name
    input_image = cv2.imread(input_image_path)
    # Entry validation
    if input_image is None:
        print("Image could not be located, please re-check the name and click generate again")
        print(input_image_path)
        return
    output_number = int(output_number)
    if int(output_number) == False:
        print("Invalid output images number, please make sure you insert an integer and click generate again")
        return
    # Resize and plot the input image
    input_image = resize_image(input_image)
    print("Input image:")
    plot_image(input_image)
    # Create ouput directory if save is checked
    if save == 1:
        while True:
            try:
                os.mkdir(output_folder)
                break
            except:
                print("Output directory name either already exists or field left empty, please choose a unique directory name and click generate")
                return
        print('Output directory created')
    # Operations
    for x in range(output_number):
        image = input_image.copy()
        if translation == 1:
            image = translate_image(image)
        if rotation == 1 or scaling == 1:
            image = rotate_and_scale_image(image, rotation, scaling)
        if flipping == 1:
            image = flip_image(image)
        if blurring == 1:
            image = blur_image(image)
        if save == 1:
            print('{}.png'.format(x))
            cv2.imwrite('{}/{}.png'.format(output_folder, x),image)
        plot_image(image)
    return

if __name__ == "__main__" :
    # Window
    root = tk.Tk()
    root.geometry("550x350")
    root.title("TBH Data Augmentation Generator")
    root.grid_columnconfigure(0, minsize=250)
    for x in range (6):
        root.grid_rowconfigure(x, minsize=50)
    # Labels
    tk.Label(root, text="Input image name:").grid(row=0)
    tk.Label(root, text="Number of required output images:").grid(row=1)
    tk.Label(root, text="Output folder name:").grid(row=2)
    tk.Label(root, text="Please tick the required operations:").grid(row=3)
    # Text Entries
    tk_input_image_name = tk.Entry(root)
    tk_output_number = tk.Entry(root)
    tk_output_folder = tk.Entry(root)
    tk_input_image_name.grid(row=0, column=1)
    tk_output_number.grid(row=1, column=1)
    tk_output_folder.grid(row=2, column=1)
    # Checkbox variables
    tk_translation = tk.IntVar()
    tk_rotation = tk.IntVar()
    tk_flipping = tk.IntVar()
    tk_scaling = tk.IntVar()
    tk_blurring = tk.IntVar()
    tk_save = tk.IntVar()
    # Checkboxes
    tk.Checkbutton(root, text="Translation", variable = tk_translation).grid(row=3, column=1, sticky=tk.W)
    tk.Checkbutton(root, text="Rotation", variable = tk_rotation).grid(row=3, column=2, sticky=tk.W)
    tk.Checkbutton(root, text="Flipping", variable = tk_flipping).grid(row=4, column=1, sticky=tk.W)
    tk.Checkbutton(root, text="Scaling", variable = tk_scaling).grid(row=4, column=2, sticky=tk.W)
    tk.Checkbutton(root, text="Blurring", variable = tk_blurring).grid(row=5, column=1, sticky=tk.W)
    tk.Checkbutton(root, text="Save to folder", variable = tk_save).grid(row=2, column=2, sticky=tk.W)
    # Buttons
    generate_button = tk.Button(root, text='Generate', command=generate_images)
    quit_button = tk.Button(root, text='Quit', command=root.destroy)
    generate_button.grid(row=6, column=0, pady=10)
    quit_button.grid(row=6, column=2, sticky=tk.W, pady=10)
    # Main loop
    root.mainloop()