# YOLOv8 Object Detection with Webcam

This project uses **Ultralytics YOLOv8** for real-time object detection using a laptop webcam.

## Features

- Uses **YOLOv8** (pretrained model) for object detection.
- Runs on both **CPU** and **GPU**.
- Supports **fullscreen display** for better visibility.
- Press **'q'** to exit the detection window.

## Installation

### 1️⃣ Clone the Repository

```sh
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

### 2️⃣ Create a Virtual Environment

```sh
python -m venv yolo_env
```

Activate it:

- **Windows:**
  ```sh
  yolo_env\Scripts\activate
  ```
- **Mac/Linux:**
  ```sh
  source yolo_env/bin/activate
  ```

### 3️⃣ Install Dependencies

```sh
pip install ultralytics opencv-python numpy
```

## Usage

### Run the Object Detection Script

```sh
python yolo_cam.py
```

## Fullscreen Mode

The detection window runs in **fullscreen** mode. Press **'q'** to close it.

## Troubleshooting

- If `ultralytics` is not found, try reinstalling:
  ```sh
  pip install --upgrade ultralytics
  ```
- If the webcam is not detected, ensure it is properly connected and accessible.

## License

This project is under the **MIT License**.

---

### 🔗 Connect with Me

- GitHub: [https://github.com/avishka-hashara](https://github.com/avishka-hashara)
- LinkedIn: www.linkedin.com/in/avishkahashara

Happy Coding! 

