import numpy as np
from face_detection import detect_faces


def test_no_faces_in_blank_image():
    image = np.zeros((400, 400, 3), dtype=np.uint8)

    result_image, faces = detect_faces(image)

    assert result_image is not None
    assert len(faces) == 0