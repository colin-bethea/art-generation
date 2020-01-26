from google_images_download import google_images_download

response = google_images_download.googleimagesdownload()

arguments = {"keywords":"mountains", "format": "jpg", "size": "large", "aspect_ratio": "square", "limit": 1000}
paths = response.download(arguments)
print(paths)