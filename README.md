---
title: Smart OCR
emoji: 📄
colorFrom: indigo
colorTo: teal
sdk: gradio
sdk_version: 4.27.0
app_file: app.py
license: apache-2.0
---

# Smart OCR (MVP)

Upload a document (receipt, invoice, etc.). It segments and extracts text using a simulated segmentation pipeline and OCR.

## Usage

1. Upload an image file
2. Click submit
3. Text is extracted and displayed

Runs on Hugging Face Spaces (free tier CPU). Future version will support SAM2 (Meta’s segmentation model) and GPU for better accuracy.
