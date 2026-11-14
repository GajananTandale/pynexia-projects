# Custom QR Code Generator

A Python command-line application that converts text or URLs into customizable, high-error-correction QR code PNG images. Built as part of the **Pynexia Tech Python Programming Virtual Internship**.

## Features
* **High Error Correction:** Uses `ERROR_CORRECT_H` so QR codes remain scannable even if partially covered or printed at smaller sizes.
* **Custom Colors:** Supports custom foreground and background colors using standard color names or hex codes.
* **Smart File Naming:** Automatically appends `.png` if omitted by the user and validates empty inputs.

## Tech Stack
* **Language:** Python 3.x
* **Libraries:** `qrcode`, `Pillow` (PIL)

## Installation & Setup
1. Navigate to the project folder:
   ```bash
   cd qr-generator
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## How to Run
Run the script from your terminal:
```bash
python qr_generator.py
```

### Example Input
```text
Enter the text or URL for the QR code: https://github.com
Enter output filename (e.g., my_qr): repo_qr
Enter QR color (press Enter for black):
Enter background color (press Enter for white):
```
