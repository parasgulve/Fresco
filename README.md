# 🎨 Neural Style Transfer — Real-Time Artistic Image Stylization

A deep learning application that transforms ordinary photographs into stunning artwork using **Neural Style Transfer**. Built with **PyTorch** and served through an interactive **Streamlit** web interface with GPU acceleration.

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-2.5-EE4C2C?logo=pytorch&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.51-FF4B4B?logo=streamlit&logoColor=white)
![CUDA](https://img.shields.io/badge/CUDA-12.1-76B900?logo=nvidia&logoColor=white)

---

## 📌 Overview

This project implements the **Fast Neural Style Transfer** algorithm based on the paper [*Perceptual Losses for Real-Time Style Transfer and Super-Resolution*](https://arxiv.org/abs/1603.08010) by Johnson et al. Unlike optimization-based methods that take minutes per image, this approach uses a **feed-forward transformer network** to stylize images in a single forward pass — achieving **real-time performance**.

### Key Highlights

- ⚡ **Real-time inference** — stylize any image in under a second on GPU
- 🖼️ **29 pre-trained artistic styles** including Picasso, Mosaic, Starry Night, Cubism, and more
- 🌐 **Interactive web UI** via Streamlit with side-by-side comparison
- 🔥 **GPU accelerated** with automatic CUDA detection
- 🧠 **Custom training pipeline** to create your own artistic styles

---

## 🏗️ Architecture

```
Input Image ──► TransformerNet (Feed-Forward CNN) ──► Stylized Output
                        │
                   Training Phase:
                        │
              ┌─────────┴──────────┐
              ▼                    ▼
        Content Loss          Style Loss
        (VGG16 relu2_2)      (Gram Matrices)
```

| Component | Description |
|-----------|-------------|
| **TransformerNet** | Feed-forward network with convolutional layers, 5 residual blocks, and upsampling layers |
| **VGG16** | Pre-trained feature extractor for computing perceptual content and style losses |
| **Instance Normalization** | Used instead of batch normalization for better stylization quality |
| **Reflection Padding** | Prevents border artifacts in generated images |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- NVIDIA GPU with CUDA support (recommended) or CPU
- Git

### Installation

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/neural-style-transfer.git
cd neural-style-transfer

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
.\venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install PyTorch with CUDA support (adjust cu121 for your CUDA version)
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu121

# For CPU-only:
# pip install torch torchvision

# Install remaining dependencies
pip install -r requirements.txt
```

### Download Pre-trained Models

Pre-trained style models are not included in this repository due to size constraints. Download them and place in the `saved_models/` directory:

> 📥 **[Download Models (Google Drive)](YOUR_DRIVE_LINK_HERE)** — 34 pre-trained `.pth` files (~218 MB total)

### Run the Application

```bash
streamlit run main.py
```

Then open [http://localhost:8501](http://localhost:8501) in your browser.

---

## 🎨 Available Styles

<table>
<tr>
<td align="center"><strong>Candy</strong></td>
<td align="center"><strong>Mosaic</strong></td>
<td align="center"><strong>Rain Princess</strong></td>
<td align="center"><strong>Udnie</strong></td>
</tr>
<tr>
<td align="center"><strong>Picasso</strong></td>
<td align="center"><strong>Starry Night</strong></td>
<td align="center"><strong>Cubism</strong></td>
<td align="center"><strong>Abstract</strong></td>
</tr>
<tr>
<td align="center"><strong>Floral</strong></td>
<td align="center"><strong>Knife Paint</strong></td>
<td align="center"><strong>City</strong></td>
<td align="center"><strong>Eye</strong></td>
</tr>
</table>

*Multiple variations of each style are available, trained at different epochs (4000–32000 iterations) for varying intensity.*

---

## 🧠 Train Your Own Style

You can train a new style model with your own style image:

```bash
python neural_style.py train \
    --dataset path/to/training/images \
    --style-image path/to/style.jpg \
    --save-model-dir saved_models/ \
    --cuda 1 \
    --epochs 2 \
    --batch-size 4 \
    --content-weight 1e5 \
    --style-weight 1e10
```

You can also continue training from an existing model:

```bash
python neural_style.py train \
    --dataset path/to/images \
    --style-image path/to/style.jpg \
    --save-model-dir saved_models/ \
    --pretrained-model saved_models/existing_model.pth \
    --cuda 1
```

---

## 📁 Project Structure

```
neural-style-transfer/
├── main.py               # Streamlit web application
├── style.py              # Model loading and inference logic
├── neural_style.py       # Training and CLI evaluation pipeline
├── transformer_net.py    # TransformerNet architecture (feed-forward CNN)
├── vgg.py                # VGG16 perceptual loss network
├── utils.py              # Image I/O and utility functions
├── requirements.txt      # Python dependencies
├── saved_models/         # Pre-trained .pth model files (not in repo)
└── images/
    └── output-images/    # Generated stylized images
```

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| **PyTorch** | Deep learning framework for model training and inference |
| **Torchvision** | Pre-trained VGG16 and image transformations |
| **Streamlit** | Interactive web interface |
| **Pillow** | Image loading and saving |
| **NumPy** | Numerical operations |
| **CUDA** | GPU acceleration for real-time performance |

---

## 📚 References

- Johnson, J., Alahi, A., & Fei-Fei, L. (2016). [*Perceptual Losses for Real-Time Style Transfer and Super-Resolution*](https://arxiv.org/abs/1603.08010)
- Gatys, L. A., Ecker, A. S., & Bethge, M. (2015). [*A Neural Algorithm of Artistic Style*](https://arxiv.org/abs/1508.06576)
- He, K., et al. (2015). [*Deep Residual Learning for Image Recognition*](https://arxiv.org/abs/1512.03385)
- Odena, A., et al. (2016). [*Deconvolution and Checkerboard Artifacts*](http://distill.pub/2016/deconv-checkerboard/)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

<p align="center">
  Built with ❤️ using PyTorch & Streamlit
</p>
