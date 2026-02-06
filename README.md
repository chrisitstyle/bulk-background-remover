# 🖼️ Bulk Background Remover

A simple, powerful Python tool to remove backgrounds from multiple images at once.
It uses AI (machine learning) to detect the main subject and create a transparent PNG.

## ✨ Features

- **Batch Processing:** Processes all images in a folder automatically.
- **Dual Mode:** Choose the best AI model for your needs:
  - 🧠 **SMART Mode:** Best for portraits, people, products, and complex scenes.
  - 🎯 **PRECISE Mode:** Best for logos, flags, anime, and simple graphics.
- **Interactive CLI:** Simple menu to select the mode.
- **Clean Output:** Automatically handles file naming and terminal output.

## 🚀 Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/chrisitstyle/bulk-background-remover.git
    cd bulk-background-remover
    ```

2.  **Install requirements:**
    Make sure you have Python installed, then run:
    ```bash
    pip install -r requirements.txt
    ```
    _(This will install `rembg`, `Pillow`, and `onnxruntime`)_.

## 🛠️ Usage

1.  **Prepare your images:**
    Place the images you want to process inside the `input_images` folder.
    _(If the folder doesn't exist, the script will create it for you upon the first run)._

2.  **Run the script:**

    ```bash
    python main.py
    ```

3.  **Choose your mode:**
    The script will ask you to select a model:
    - Type `1` for **Smart Mode** (People/Products).
    - Type `2` for **Precise Mode** (Logos/Graphics).

4.  **Done!**
    Check the `output_images` folder for your transparent PNGs.

## 📂 Folder Structure

```text
bulk-background-remover/
├── input_images/       # Put your source images here (JPG, PNG, WEBP...)
├── output_images/      # Processed images will appear here
├── main.py             # The main script
├── requirements.txt    # List of dependencies
└── README.md           # This file
```
