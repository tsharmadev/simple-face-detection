# Simple Face Detection System

A beginner-friendly Computer Vision project that detects human faces in uploaded images using **OpenCV** and the **Haar Cascade Classifier**.

The application provides a simple **Streamlit web interface** where users can upload an image, detect faces, view the results, see the number of detected faces, and download the processed image.

---

## 📌 Project Overview

Face detection is one of the basic applications of Computer Vision. This project demonstrates how a pre-trained Haar Cascade classifier can be used to identify human faces in an image.

The project focuses on understanding the basic Computer Vision workflow:

**Image Input → Image Processing → Face Detection → Result Visualization → Output Download**

---

## 🎯 Objectives

- Detect human faces from uploaded images.
- Understand basic image processing using OpenCV.
- Use a pre-trained Haar Cascade classifier.
- Display detected faces using bounding boxes.
- Count the number of detected faces.
- Allow users to download the processed image.
- Provide a simple and user-friendly interface using Streamlit.

---

## ✨ Features

- Upload images in JPG, JPEG, or PNG format.
- Automatic face detection using OpenCV.
- Bounding boxes around detected faces.
- Display the original image.
- Display the processed image with detected faces.
- Show the total number of detected faces.
- Download the face-detection result.
- Basic input validation and error handling.

---

## 🛠️ Technologies Used

- **Python**
- **OpenCV**
- **NumPy**
- **Streamlit**
- **Pillow**
- **Pytest**

### Face Detection Method

The project uses the **Haar Cascade Classifier**:

`haarcascade_frontalface_default.xml`

No custom machine learning model is trained in this project. A pre-trained Haar Cascade classifier is used to keep the implementation simple and efficient.

---

## 📂 Project Structure

```text
simple-face-detection/
│
├── app.py
├── face_detection.py
├── image_utils.py
├── config.py
├── test_face_detection.py
├── haarcascade_frontalface_default.xml
├── requirements.txt
├── README.md
├── statement.md
│
├── sample_images/
└── screenshots/
