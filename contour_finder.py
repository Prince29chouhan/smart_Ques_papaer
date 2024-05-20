import cv2
import os
import numpy as np

def get_contours_info(image_path):
    # Load the image
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Check if the image was loaded successfully
    if image is None:
        print(f"Error: Unable to load image at {image_path}")
        return

    _, thresh = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

    # Find contours
    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Iterate through contours and calculate centroid and area
    for i, contour in enumerate(contours):
        # Calculate moments for each contour
        M = cv2.moments(contour)

        # Calculate centroid
        if M['m00'] != 0:
            cx = int(M['m10'] / M['m00'])
            cy = int(M['m01'] / M['m00'])
        else:
            cx, cy = 0, 0

        # Calculate area
        area = cv2.contourArea(contour)

        # Print contour details
        print(f"Contour {i+1}: Centroid = ({cx}, {cy}), Area = {area}")

        # Draw the contour and centroid on the image (for visualization)
        cv2.drawContours(image, [contour], -1, (0, 255, 0), 2)
        cv2.circle(image, (cx, cy), 5, (255, 0, 0), -1)

    # Show the image with contours and centroids
    cv2.imshow("Contours", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    image_path = 'images/contours.png'
    get_contours_info(image_path)
