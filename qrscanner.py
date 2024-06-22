import qrcode

print("Generating QR code...")
myqr = qrcode.make("https://www.youtube.com/watch?v=PyDn2gU9DJo&t=4s")

print("Saving QR code to myqr.png...")
myqr.save("myqr.png")

print("QR code generated and saved successfully.")