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