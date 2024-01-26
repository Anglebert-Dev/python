import qrcode

def generate_qr_code(data, output_file):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(output_file)

if __name__ == "__main__":
    website_url = "https://fastbreakt.com/"
    # website_url = "https://elogearts.com/"
    pdf_url = "https://assets.ctfassets.net/nkydfjx48olf/5qFMF3mvitLMahX67i7iOb/028229996c13cbc27a0538f055a41b46/php_cookbook.pdf"

    website_qr_file = "website_qr.png"
    pdf_qr_file = "pdf_qr.png"

    generate_qr_code(website_url, website_qr_file)
    generate_qr_code(pdf_url, pdf_qr_file)

    print(f"Website QR Code saved to: {website_qr_file}")
    print(f"PDF QR Code saved to: {pdf_qr_file}")
