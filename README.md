# 🖼️ F5 Steganography in Python

This project is a simple implementation of **F5-style steganography**, where text is hidden inside images by modifying pixel values. It supports both **encoding** (hiding text in an image) and **decoding** (extracting hidden text from an image).

---

## 📦 Requirements

- **Python 3.10+**  
- Install dependencies with:

```bash
pip install pillow matplotlib numpy
```

---

## ▶️ Usage

### 1️⃣ Encoding text into an image

Run the script:

```bash
python f5.py
```

**Steps:**

1. A file dialog will open → select a **PNG image**.  
2. Enter the **output filename** (e.g., `hidden.png`).  
3. Enter the **text** you want to hide.  
4. The program saves a **new image** with the hidden data.  
5. Decoding runs immediately to verify the hidden text.  

---

### 2️⃣ Decoding text from an encoded image

Run the standalone decoder script:

```bash
python f5_decode.py
```

**Steps:**

1. A file dialog will open → select the **encoded image**.  
2. The program will **extract and display the hidden text**.  

---

## 🔐 Notes

- ⚠️ This is a **demo/educational project** – not secure for real cryptographic use.  
- 🖼️ Use **PNG images** (lossless format). JPEG compression may destroy hidden data.  
- 📍 The **positions list** is required for decoding in the current implementation (automatically managed during encoding).  
