📄 Scanned Document to PDF Converter
Effortlessly convert scanned document images into PDFs! This Python script automates the process, efficiently handling thousands of images (e.g., 8000+) with powerful features like multithreading, batch processing, and image compression.

🌟 Features
🚀 Batch Processing: Minimize memory usage by processing images in batches.
⚡ Multithreading: Utilize ThreadPoolExecutor for fast, concurrent folder processing.
🖼️ Image Compression: Optimize storage with reduced file sizes.
📊 Progress Tracking: Stay informed with tqdm progress bars.
🛡️ Error Handling: Comprehensive logs for troubleshooting.
🔄 Skip Processed Folders: Avoid duplicate PDF creation.
📜 Summary Log: A detailed process log (process_log.txt).
🛠️ Requirements
Prerequisites
Python: Version 3.6 or higher.
Libraries: Install dependencies with:

pip install pillow tqdm
🚀 How to Use
Clone the Repository:


git clone https://github.com/TAMIRAT-FEREJA-T/bulk-image-to-pdf-convertor.git
cd bulk-image-to-pdf-convertor
Prepare Your Files:
Place your image folders in the ./files directory. Each folder will generate a separate PDF.

Run the Script:


python script_name.py
Check Output:
PDFs will be saved in the final_pdf_combined directory.

📂 Folder Structure
Input:

files/
├── Folder1/
│   ├── image1.jpg
│   ├── image2.png
│   └── ...
├── Folder2/
│   ├── imageA.jpeg
│   ├── imageB.bmp
│   └── ...
Output:

final_pdf_combined/
├── Folder1.pdf
├── Folder2.pdf
🧩 Script Overview
find_images(folder): Locate all image files in a folder and its subfolders.
create_pdf_in_batches(image_list, output_pdf, batch_size): Generate PDFs in memory-efficient batches.
compress_image(image_path): Compress individual images for faster processing.
process_folder(dir_name, output_folder): Process a single folder into a PDF.
generate_summary_log(): Summarize the operation in process_log.txt.
🔧 Troubleshooting
❌ No PDFs Generated:
Ensure files/ contains valid subfolders with image files.
🔄 Memory Issues:
Reduce batch_size in the create_pdf_in_batches function.
⚠️ Corrupted Images:
Check logs in process_log.txt for details.
🤝 Contributions
We welcome contributions! Feel free to:

Fork this repository.
Submit issues or feature requests.
Create pull requests to improve the project.
📜 License
This project is open-source and available under the MIT License.

👤 Author
Tamirat Fereja
📧 Email: tamiratfereja1029@gmail.com

🎉 Enjoy seamless PDF creation and streamline your workflow!






