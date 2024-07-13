# Image Segmentation and Compression
## About:
Image segmentation is a crucial technique in computer vision, enabling more efficient image analysis by simplifying the image’s complexity. This process not only facilitates various applications like object detection and image recognition but also significantly aids in compressing the image size.

This project has been created using the K-Means Algorithm for image segmentation and compression. By clustering similar pixels, the algorithm reduces the image’s detail while preserving essential features, resulting in a compressed version of the original image. This model is deployed using Flask, providing a user-friendly interface for image uploading and segmentation.

## Features:

	Automatic Cluster Calculation: The algorithm can automatically determine the optimal number of clusters for segmentation.
	User-Defined Clusters: Users have the flexibility to specify the number of clusters, directly influencing the level of compression and detail in the segmented image.
	Image Saving: The application saves a copy of the segmented image for easy access and further use.

## How It Works:

		Upload Image: Users can upload an image through the Flask web interface.
		Select Clusters: Users can either allow the algorithm to compute the optimal number of clusters or manually enter their preferred number of clusters.
		Segment and Compress: The application processes the image using K-Means clustering, segmenting it based on the chosen number of clusters.
		Download: The segmented and compressed image is saved, and users can download it directly from the web interface.

## Note:
    Please make sure you have the required libraries installed.
