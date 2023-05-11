import qrcode

# Asking user for the URL to encode
URL = input("Enter the URL to Generate the QR code: ")

# Encoding data using make() function
img = qrcode.make(URL)

# Saving as an image file
img.save('QR-Code.png')

# Displaying message that the QR code is generated and saved locally
print("QR code generated and saved as QR-Code.png")
