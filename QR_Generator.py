import os
from PIL import Image
import qrcode


def get_non_empty_input(prompt):
  """Ensures the user enters non-empty text."""
  while True:
    value = input(prompt).strip()
    if value:
      return value
    print("Input cannot be empty. Please try again.")


def get_qr_payload():
  """Prompts the user to choose a data type and formats the QR string."""
  print("\nSelect QR Code Data Type:")
  print("  1. Plain Text")
  print("  2. Website URL")
  print("  3. Wi-Fi Credentials")
  print("  4. vCard Contact Details")

  while True:
    choice = input("Enter choice (1-4): ").strip()
    if choice == "1":
      return get_non_empty_input("Enter plain text: ")

    elif choice == "2":
      url = get_non_empty_input("Enter website URL (e.g., https://example.com): ")
      if not url.startswith(("http://", "https://")):
        url = "https://" + url
      return url

    elif choice == "3":
      ssid = get_non_empty_input("Enter Wi-Fi Network Name (SSID): ")
      encryption = (
          input("Enter security type (WPA/WEP/nopass) [default WPA]: ")
          .strip()
          .upper()
          or "WPA"
      )
      password = (
          ""
          if encryption == "NOPASS"
          else get_non_empty_input("Enter Wi-Fi Password: ")
      )
      return f"WIFI:S:{ssid};T:{encryption};P:{password};;"

    elif choice == "4":
      full_name = get_non_empty_input("Enter Full Name: ")
      phone = get_non_empty_input("Enter Phone Number: ")
      email = input("Enter Email Address (optional): ").strip()
      org = input("Enter Organization/Company (optional): ").strip()

      vcard = [
          "BEGIN:VCARD",
          "VERSION:3.0",
          f"FN:{full_name}",
          f"TEL;TYPE=CELL:{phone}",
      ]
      if email:
        vcard.append(f"EMAIL:{email}")
      if org:
        vcard.append(f"ORG:{org}")
      vcard.append("END:VCARD")
      return "\n".join(vcard)

    else:
      print("Invalid choice. Please enter 1, 2, 3, or 4.")


def get_error_correction():
  """Lets the user select an error correction level."""
  levels = {
      "L": qrcode.constants.ERROR_CORRECT_L,  # ~7% recovery
      "M": qrcode.constants.ERROR_CORRECT_M,  # ~15% recovery
      "Q": qrcode.constants.ERROR_CORRECT_Q,  # ~25% recovery
      "H": qrcode.constants.ERROR_CORRECT_H,  # ~30% recovery
  }
  print("\nSelect Error Correction Level:")
  print("  L - Low (~7% recovery)")
  print("  M - Medium (~15% recovery)")
  print("  Q - Quartile (~25% recovery)")
  print("  H - High (~30% recovery) [Recommended]")

  while True:
    choice = input("Enter level (L/M/Q/H) [default H]: ").strip().upper() or "H"
    if choice in levels:
      return levels[choice]
    print("Invalid level. Choose L, M, Q, or H.")


def get_border_thickness():
  """Gets a valid integer for QR border thickness."""
  while True:
    val = input("Enter border thickness (1-20) [default 4]: ").strip()
    if not val:
      return 4
    if val.isdigit() and 1 <= int(val) <= 20:
      return int(val)
    print("Please enter a number between 1 and 20.")


def get_output_filename():
  """Gets output filename and validates PNG or JPEG extension."""
  raw_name = get_non_empty_input("Enter output filename (without extension): ")
  while True:
    fmt = (
        input("Choose image format (PNG / JPEG) [default PNG]: ")
        .strip()
        .upper()
        or "PNG"
    )
    if fmt == "PNG":
      return f"{raw_name}.png", "PNG"
    elif fmt in ("JPEG", "JPG"):
      return f"{raw_name}.jpg", "JPEG"
    else:
      print("Invalid format. Please enter PNG or JPEG.")


def generate_qr_code(
    data, filename, img_format, fill_color, back_color, border, error_level
):
  """Generates, customizes, and saves the QR code image via Pillow."""
  qr = qrcode.QRCode(
      version=None,
      error_correction=error_level,
      box_size=10,
      border=border,
  )
  qr.add_data(data)
  qr.make(fit=True)

  # Generate Pillow image
  pil_img = qr.make_image(
      fill_color=fill_color, back_color=back_color
  ).get_image()

  # JPEG does not support alpha transparency, so convert to RGB
  if img_format == "JPEG":
    pil_img = pil_img.convert("RGB")

  pil_img.save(filename, format=img_format)
  return os.path.abspath(filename)


def main():
  print("=== Advanced Custom QR Code Generator ===")

  data = get_qr_payload()
  error_level = get_error_correction()
  border = get_border_thickness()

  fill_color = (
      input("Enter QR fill color (name or hex, default 'black'): ").strip()
      or "black"
  )
  back_color = (
      input("Enter background color (name or hex, default 'white'): ").strip()
      or "white"
  )

  filename, img_format = get_output_filename()

  try:
    saved_path = generate_qr_code(
        data, filename, img_format, fill_color, back_color, border, error_level
    )
    print(f"\nSuccess! {img_format} QR code saved at:\n{saved_path}")
  except ValueError as e:
    print(
        f"\nError: Invalid color provided ({e}). Use standard names or hex"
        " codes like #1A2B3C."
    )


if __name__ == "__main__":
  main()
