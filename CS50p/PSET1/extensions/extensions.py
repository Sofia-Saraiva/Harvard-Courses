text = input("File name: ")
text = text.lower()
text = text.replace(" ", "")

if ".gif" in text:
    print("image/gif")
elif ".jpg" in text:
    print("image/jpeg")
elif ".jpeg" in text:
    print("image/jpeg")
elif ".png" in text:
    print("image/png")
elif ".pdf" in text:
    print("application/pdf")
elif ".zip" in text:
    print("application/zip")
elif ".txt" in text:
    print("text/plain")
else:
    print("application/octet-stream")

