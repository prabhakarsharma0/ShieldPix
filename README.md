# ShieldPix 🛡️
> **AI Image Defense & Anti-Deepfake Tool**

ShieldPix is an AI-powered image protection application designed to defend personal photos against unauthorized AI scraping and deepfake manipulation. Built with **PyTorch** and **ResNet50**, it injects an imperceptible adversarial defense layer that obstructs facial feature extraction while retaining high visual fidelity.

---

## ✨ Key Features
* **Biometric Defense:** Disrupts facial feature recognition models used by unauthorized AI scrapers.
* **High Visual Quality:** Retains HD clarity with a **0.98+ SSIM** (Structural Similarity Index) score.
* **Interactive Dashboard:** Real-time customization of protection intensity via Gradio UI.
* **CLI & Web Support:** Run seamless protection via command line or graphical interface.

---

## 🛠️ Tech Stack
* **Language:** Python 3.10+
* **Deep Learning:** PyTorch, Torchvision
* **Metrics & Processing:** Scikit-Learn, OpenCV, NumPy
* **Interface:** Gradio
* **Deployment:** Hugging Face Spaces

---

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone [https://github.com/prabhakarsharma0/ShieldPix.git](https://github.com/prabhakarsharma0/ShieldPix.git)
cd ShieldPix
