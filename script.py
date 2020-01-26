from google_images_download import google_images_download

response = google_images_download.googleimagesdownload()

arguments = {"keywords":"mountains", "format": "png, jpg", "size": "large, medium", "aspect_ratio": "square"}
paths = response.download(arguments)
print(paths)