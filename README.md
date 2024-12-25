Scanned Document to PDF Converter
This repository contains a Python script designed to automate the conversion of scanned document images into PDFs. It efficiently processes a large number of images (e.g., 8000+) using multithreading, batch processing, and image compression to ensure optimal performance.

Features
Batch Processing: Handles image processing in batches to minimize memory usage.
Multithreading: Uses ThreadPoolExecutor for concurrent folder processing.
Image Compression: Reduces file sizes for efficient storage and faster processing.
Progress Tracking: Displays progress bars using tqdm for better visibility.
Error Handling: Logs warnings and errors for troubleshooting.
Skips Already Processed Folders: Ensures no duplicate PDFs are created.
Summary Log: Generates a detailed log file (process_log.txt) of the process.
Requirements
Before running the script, ensure you have the following installed:

Python 3.6+
Required Python libraries:

pip install pillow tqdm
How to Use
Clone this repository:


git clone https://github.com/yourusername/scanned-document-to-pdf.git
cd scanned-document-to-pdf
Place your image folders inside the ./files directory. Each subfolder will be processed as a separate PDF.

Run the script:
python script_name.py
Output PDFs will be saved in the final_pdf_combined directory.

Script Structure
find_images(folder): Recursively scans a folder for image files.
create_pdf_in_batches(image_list, output_pdf, batch_size): Creates PDFs in batches to handle large image sets.
compress_image(image_path): Compresses images to reduce file sizes.
process_folder(dir_name, output_folder): Handles processing of a single folder.
generate_summary_log(): Creates a summary of the process from the log file.
Example
Input Folder Structure:
Copy code
files/
├── Folder1/
│   ├── image1.jpg
│   ├── image2.png
│   └── ...
├── Folder2/
│   ├── imageA.jpeg
│   ├── imageB.bmp
│   └── ...
Output Folder Structure:
Copy code
final_pdf_combined/
├── Folder1.pdf
├── Folder2.pdf
Troubleshooting
No PDFs Generated:

Ensure the files/ directory contains subfolders with valid image files.
Memory Issues:

Reduce the batch_size in the create_pdf_in_batches function.
Corrupted Images:

Check the logs in process_log.txt for skipped or corrupted files.
Contributions
Feel free to fork this repository, submit issues, or create pull requests to improve functionality or fix bugs.

License
This project is open-source and available under the MIT License.

Author
Tamirat fereja
For any questions or feedback, contact me at tamiratfereja1029@gmail.com 






