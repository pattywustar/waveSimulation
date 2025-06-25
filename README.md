# 〰️ Wave Simulation / 波動模擬器

這是用 Python 寫的波動模擬程式，可以互動式調整振幅、頻率、波速，還能切換橫波（Transverse）和縱波（Longitudinal）。

This is a Python program simulating waves. You can interactively adjust amplitude, frequency, speed, and switch between transverse and longitudinal waves.

## 💡 功能特色 / Features

- 使用滑桿調整振幅 (Amplitude)、頻率 (Frequency)、速度 (Speed)  
  Adjust amplitude, frequency, and speed using sliders
- 透過按鈕切換橫波和縱波波型  
  Switch between transverse and longitudinal wave types using buttons
- 動畫顯示波的傳播效果，縱波用多條垂直線模擬密疏部  
  Animated wave propagation; longitudinal waves simulated with multiple vertical lines representing compressions and rarefactions
- 使用簡單，適合物理教學或自學波動原理  
  Easy to use, suitable for physics teaching or self-learning wave principles

## 🖥️ 執行環境 / Requirements

- Python 3.x  
- numpy  
- matplotlib

## ✅ 如何執行 / How to run

```bash
pip install numpy matplotlib
python wave.py

## 🔔 提醒 / Note

- 推薦在終端機或命令提示字元執行，不建議直接用部分 IDE 的「Run」功能，避免動畫視窗無法正常顯示
  Recommended to run in terminal or command prompt instead of some IDE’s “Run” button to avoid animation display issues

- 可以自由修改程式碼，加入更多功能或粒子模擬
  Feel free to modify the code to add more features or particle simulations
