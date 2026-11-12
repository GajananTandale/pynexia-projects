import os
import qrcode


def get_non_empty_input(prompt):
    """Ensures the user enters valid, non-empty text or a URL."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input cannot be empty. Please try again.")


def sanitize_filename(filename):
    """Ensures the output filename ends with .png."""
    if not filename.lower().endswith(".png"):
        filename += ".png"
    return filename


def generate_qr_code(data, filename, fill_color="black", back_color="white"):
    """Generates and saves a customized QR code image."""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color=fill_color, back_color=back_color)
    img.save(filename)
    return os.path.abspath(filename)


def main():
    print("=== Custom QR Code Generator ===\n")

    data = get_non_empty_input("Enter the text or URL for the QR code: ")
    raw_filename = get_non_empty_input("Enter output filename (e.g., my_qr): ")
    filename = sanitize_filename(raw_filename)

    fill_color = input("Enter QR color (press Enter for black): ").strip() or "black"
    back_color = input("Enter background color (press Enter for white): ").strip() or "white"

    try:
        saved_path = generate_qr_code(data, filename, fill_color, back_color)
        print(f"\nSuccess! QR code saved at:\n{saved_path}")
    except ValueError as e:
        print(f"\nError: Invalid color name provided ({e}). Please use standard color names or hex codes.")


if __name__ == "__main__":
    main()
