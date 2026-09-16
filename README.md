# 🛡️ ShieldPix

### AI Image Defense & Anti-Deepfake Tool

ShieldPix is an AI-powered image protection application designed to defend personal photos against unauthorized AI scraping and deepfake manipulation.

Built with **Python, PyTorch, and ResNet50**, ShieldPix applies an imperceptible adversarial defense layer designed to obstruct facial feature extraction while maintaining high visual fidelity.

---

## ✨ Key Features

* 🛡️ **Biometric Defense**
  Disrupts facial feature recognition models used by unauthorized AI scrapers.

* 🖼️ **High Visual Quality**
  Maintains high visual fidelity with a **0.98+ SSIM (Structural Similarity Index)** score.

* 🎚️ **Interactive Dashboard**
  Customize protection intensity in real time through the Gradio interface.

* 💻 **CLI & Web Support**
  Run image protection through either the command-line interface or the interactive web UI.

---

## 🛠️ Tech Stack

| Category             | Technologies                   |
| -------------------- | ------------------------------ |
| **Language**         | Python 3.10+                   |
| **Deep Learning**    | PyTorch, Torchvision, ResNet50 |
| **Image Processing** | OpenCV, NumPy                  |
| **Metrics**          | Scikit-Learn                   |
| **Interface**        | Gradio                         |
| **Deployment**       | Hugging Face Spaces            |

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/prabhakarsharma0/ShieldPix.git
cd ShieldPix
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Application

#### 🌐 Web UI — Gradio

```bash
python gradio_app.py
```

#### 💻 Command Line Interface

```bash
python app.py
```

---

## 🔄 Workflow

ShieldPix takes an input image and applies an adversarial protection layer designed to interfere with facial feature extraction while preserving the visual appearance of the image.

```text
Input Image
     ↓
Image Processing
     ↓
Adversarial Defense Generation
     ↓
Protected Image
     ↓
AI / Facial Feature Extraction Resistance
```

---

## 📸 Demo

<img width="1882" height="956" alt="image" src="https://github.com/user-attachments/assets/25d81067-3eb7-4f82-bacd-3625d708ed35" />


### CLI Workflow

The CLI can be used to generate protected adversarial images from input photographs.

*Add screenshots or GIFs of the application here.*

### Web Interface

The Gradio interface provides real-time controls for adjusting the protection intensity.

*Add a screenshot of the Gradio dashboard here.*

---

## 📊 Performance

* **SSIM:** 0.98+
* **Visual Quality:** High visual fidelity
* **Protection:** Designed to interfere with facial feature extraction

> Performance values may vary depending on the input image and protection settings.

---

## 📁 Project Structure

```text
ShieldPix/
│
├── app.py
├── gradio_app.py
├── requirements.txt
├── README.md
├── LICENSE
└── ...
```

---

## ☁️ Deployment

ShieldPix can be deployed as a web application using **Hugging Face Spaces** with Gradio.

---

## 📄 License

This project is distributed under the **MIT License**.

See the `LICENSE` file for more information.

---

## 👨‍💻 Author

**Prabhakar Sharma**

GitHub:
https://github.com/prabhakarsharma0
