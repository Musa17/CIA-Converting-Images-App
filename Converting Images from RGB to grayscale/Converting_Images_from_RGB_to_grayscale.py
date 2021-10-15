import cv2

# Load image
originalImage = cv2.imread('Pikachu.jpg')

# Show original image
cv2.namedWindow('Original image')
cv2.imshow('Original image', originalImage)

cv2.waitKey(0)
cv2.destroyAllWindows()

rows = originalImage.shape[0]
columns = originalImage.shape[1]
canals = originalImage.shape[2]


print ("Please wait a little bit ...")

# Convert RGB image to grayscale image
for k in range(0, canals):
	for i in range(0, rows):
		for j in range(0, columns):
			(b, g, r) = originalImage[i, j]
			originalImage[i, j] = (0.299 * r) + (0.587 * g) + (0.114 * b)

newImage = originalImage

# Show new image			
cv2.namedWindow('New image')
cv2.imshow('New image', newImage)

cv2.waitKey(0)
cv2.destroyAllWindows()