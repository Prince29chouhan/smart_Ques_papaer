# Contour Detection with OpenCV

This project demonstrates how to detect contours in an image using OpenCV. It calculates and displays the centroid and area of each contour found in the image.

## Requirements

- Python 3.6+
- OpenCV
- numpy

## Installation

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/Prince29chouhan/smart_Ques_papaer.git
    cd contour-detection
    ```

2. **Install Required Libraries:**
    ```bash
    pip install opencv-python numpy
    ```

3. **Prepare the Image:**
    - Add the image you want to process to the `images` directory. Ensure the image is named `contours.png` or update the script with the correct image name.

## Usage

1. **Running the Script:**
    ```bash
    python contour_detection.py
    ```
    - The script loads the specified image in grayscale.
    - It applies a binary threshold to the image and detects contours.
    - For each contour, it calculates the centroid and area, then prints these details.
    - The script draws the contours and centroids on the image and displays the result.

## Project Overview

### Load and Preprocess the Image

The script loads the image in grayscale and applies a binary threshold to prepare it for contour detection.

### Find and Process Contours

The script uses OpenCV's `findContours` function to detect contours in the thresholded image. It calculates the centroid and area for each contour using image moments.

### Display Results

The script draws the detected contours and their centroids on the image, then displays the image with this information.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
