import os
from rembg import remove, new_session
from PIL import Image

# CONFIGURATION
INPUT_FOLDER = "input_images"
OUTPUT_FOLDER = "output_images"
ALLOWED_EXTENSIONS = ('.jpg', '.jpeg', '.png', '.webp', '.bmp')

def get_user_choice():
    """
    Displays a menu and returns the selected model name based on user input.
    """
    print("\n" + "="*55)
    print("   BACKGROUND REMOVER - SELECT MODE")
    print("="*55)
    print(" 1. [SMART]   General Use (Model: isnet-general-use)")
    print("              Best for: People, products, complex scenes")
    print("")
    print(" 2. [PRECISE] Base Model  (Model: u2net)")
    print("              Best for: Logos, flags, simple graphics")
    print("-" * 55)
    
    choice = input("Enter 1 or 2: ").strip()
    
    if choice == "1":
        return "isnet-general-use", "SMART (isnet-general-use)"
    elif choice == "2":
        return "u2net", "PRECISE (u2net)"
    else:
        print("\nInvalid input. Defaulting to SMART mode.")
        return "isnet-general-use", "SMART (isnet-general-use)"

def batch_remove_background():
    # Get user preference
    model_name, model_display_name = get_user_choice()

    # Check folders
    if not os.path.exists(INPUT_FOLDER):
        print(f"\nError: Input folder '{INPUT_FOLDER}' not found.")
        print("Creating folder...")
        os.makedirs(INPUT_FOLDER)
        return

    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)

    # Get file list
    files = [f for f in os.listdir(INPUT_FOLDER) if f.lower().endswith(ALLOWED_EXTENSIONS)]
    total = len(files)

    if total == 0:
        print(f"\nFolder '{INPUT_FOLDER}' is empty.")
        return

    print(f"\nFound {total} images.")
    print(f"Loading model [{model_display_name}]... Please wait.")
    
    # Initialize session with the selected model
    try:
        current_session = new_session(model_name)
    except Exception as e:
        print(f"Error loading model: {e}")
        return

    print("-" * 55)

    # Processing loop
    for i, filename in enumerate(files, 1):
        input_path = os.path.join(INPUT_FOLDER, filename)
        
        name_without_ext = os.path.splitext(filename)[0]
        output_filename = f"{name_without_ext}.png"
        output_path = os.path.join(OUTPUT_FOLDER, output_filename)

        try:
            msg = f"[{i}/{total}] Processing: {filename}..."
            print(msg.ljust(100), end="\r")
            
            input_image = Image.open(input_path)
            
            # Pass the custom session to the remove function
            output_image = remove(input_image, session=current_session)
            
            output_image.save(output_path)
            
        except Exception as e:
  
            err_msg = f"\nError processing {filename}: {e}"
            print(err_msg.ljust(100))

    print(f"\n\n" + "="*55)
    print(f"Done! Processed images are in: {OUTPUT_FOLDER}")
    input("Press Enter to exit...")

if __name__ == "__main__":
    batch_remove_background()