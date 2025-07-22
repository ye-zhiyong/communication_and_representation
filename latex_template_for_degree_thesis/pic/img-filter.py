import numpy as np
import cv2

input_image_path = 'input-filter.png'  
image = cv2.imread(input_image_path, cv2.IMREAD_COLOR)


if image is None:
    print(f"Error: Unable to load image {input_image_path}")
    exit()


mean_filtered_image = cv2.blur(image, (5, 5))


median_filtered_image = cv2.medianBlur(image, 5)


gaussian_filtered_image = cv2.GaussianBlur(image, (5, 5), 0)


output_mean_path = 'mean_filtered.png'
output_median_path = 'median_filtered.png'
output_gaussian_path = 'gaussian_filtered.png'

cv2.imwrite(output_mean_path, mean_filtered_image)
cv2.imwrite(output_median_path, median_filtered_image)
cv2.imwrite(output_gaussian_path, gaussian_filtered_image)

print(f"Filtered images saved as {output_mean_path}, {output_median_path}, and {output_gaussian_path}")
