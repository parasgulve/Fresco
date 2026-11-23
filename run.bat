@echo off
echo Starting Fresco - Neural Style Transfer...
echo.
echo GPU Status:
.\venv\Scripts\python.exe -c "import torch; print('CUDA Available:', torch.cuda.is_available()); print('GPU:', torch.cuda.get_device_name(0) if torch.cuda.is_available() else 'No GPU')"
echo.
echo Starting Streamlit...
.\venv\Scripts\streamlit.exe run main.py
