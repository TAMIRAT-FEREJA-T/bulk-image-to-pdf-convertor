# pip install pillow tqdm


import os
from PIL import Image
import logging
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm

# Set up logging
logging.basicConfig(filename='process_log.txt', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def find_images(folder):
    """Find all image files in the specified folder and its subfolders."""
    images = []
    for root, _, files in os.walk(folder):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                images.append(os.path.join(root, file))
    return images


def create_pdf_in_batches(image_list, output_pdf, batch_size=50):
    """Create a PDF from a list of image files in batches to handle memory efficiently."""
    if not image_list:
        logging.warning("No images found for PDF creation.")
        return

    try:
        batches = [image_list[i:i + batch_size] for i in range(0, len(image_list), batch_size)]
        first_image = Image.open(batches[0][0]).convert('RGB')
        
        for batch in batches:
            images = [Image.open(img).convert('RGB') for img in batch]
            first_image.save(output_pdf, save_all=True, append_images=images)
        
        logging.info(f"PDF created successfully: {output_pdf}")
    except Exception as e:
        logging.error(f"Error creating PDF from images in batches: {e}")


def compress_image(image_path):
    """Compress image to reduce file size."""
    try:
        img = Image.open(image_path)
        img.save(image_path, "JPEG", quality=185)  # Adjust quality as needed
    except Exception as e:
        logging.warning(f"Skipping compression for {image_path} due to {e}")


def process_folder(dir_name, output_folder):
    """Process a single folder to create a PDF."""
    try:
        image_files = find_images(dir_name)
        if image_files:
            logging.info(f"Processing folder: {dir_name} with {len(image_files)} images.")
            output_pdf_path = os.path.join(output_folder, f"{os.path.basename(dir_name)}.pdf")

            # Skip already processed folders
            if os.path.exists(output_pdf_path):
                logging.info(f"PDF already exists for folder {dir_name}. Skipping...")
                return

            # Compress images
            for img_path in tqdm(image_files, desc=f"Compressing images in {dir_name}"):
                compress_image(img_path)

            # Create PDF
            create_pdf_in_batches(image_files, output_pdf_path)
        else:
            logging.warning(f"No images found in folder: {dir_name}")
    except Exception as e:
        logging.error(f"Error processing folder {dir_name}: {e}")


def main():
    base_folder_path = './files'  # Change this to your base folder path
    output_folder = 'final_pdf_combined'

    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Get all subfolders to process
    subfolders = [os.path.join(root, dir_name) for root, dirs, _ in os.walk(base_folder_path) for dir_name in dirs]

    # Use ThreadPoolExecutor for parallel processing
    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(process_folder, folder, output_folder) for folder in subfolders]
        for future in futures:
            future.result()  # Wait for all threads to finish

    # Generate summary log
    generate_summary_log()


def generate_summary_log():
    """Generate a summary log of the processing."""
    try:
        with open("process_log.txt", "r") as log_file:
            log_data = log_file.read()
        print("\nProcessing Summary:\n")
        print(log_data)
    except Exception as e:
        logging.error(f"Error generating summary log: {e}")


if __name__ == "__main__":
    main()


