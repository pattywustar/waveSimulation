import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, RadioButtons
from matplotlib.animation import FuncAnimation

# === 初始參數 ===
num_points = 50  # 縱波用點數，不要太多
x = np.linspace(0, 4 * np.pi, 500)
x_particles = np.linspace(0, 4 * np.pi, num_points)  # 縱波粒子位置

amplitude = 1
frequency = 1
speed = 1
wave_type = 'Transverse'

fig, ax = plt.subplots()
plt.subplots_adjust(left=0.25, bottom=0.35)

# 繪製橫波線條
line, = ax.plot(x, amplitude * np.sin(frequency * x), lw=2)

# 縱波用多條垂直線代表粒子
vertical_lines = [ax.plot([xp, xp], [-0.5, 0.5], color='b')[0] for xp in x_particles]

ax.set_xlim(0, 4 * np.pi)
ax.set_ylim(-2, 2)
ax.set_title('Wave Simulation (Transverse or Longitudinal)')
ax.set_xlabel('Position')
ax.set_ylabel('Displacement')

# 滑桿區域
amp_ax = plt.axes([0.25, 0.25, 0.65, 0.03])
freq_ax = plt.axes([0.25, 0.20, 0.65, 0.03])
speed_ax = plt.axes([0.25, 0.15, 0.65, 0.03])

amp_slider = Slider(amp_ax, 'Amplitude', 0.1, 2.0, valinit=amplitude)
freq_slider = Slider(freq_ax, 'Frequency', 0.1, 5.0, valinit=frequency)
speed_slider = Slider(speed_ax, 'Speed', 0.1, 5.0, valinit=speed)

# 波型選擇
radio_ax = plt.axes([0.025, 0.5, 0.15, 0.15])
radio = RadioButtons(radio_ax, ['Transverse', 'Longitudinal'])

def update(frame):
    A = amp_slider.val
    f = freq_slider.val
    v = speed_slider.val
    t = frame / 20
    k = 2 * np.pi * f

    if wave_type == 'Transverse':
        y = A * np.sin(k * (x - v * t))
        line.set_data(x, y)
        for vl in vertical_lines:
            vl.set_visible(False)
        line.set_visible(True)
        ax.set_ylabel('Displacement')

    else:
        # 縱波：隱藏橫波線，顯示多條垂直線擠壓效果
        line.set_visible(False)
        for i, xp in enumerate(x_particles):
            dx = A * np.sin(k * (xp - v * t))
            vertical_lines[i].set_xdata([xp + dx, xp + dx])
            vertical_lines[i].set_visible(True)
        ax.set_ylabel('No Vertical Displacement')

    return [line] + vertical_lines

def change_wave(label):
    global wave_type
    wave_type = label
    fig.canvas.draw_idle()

radio.on_clicked(change_wave)

ani = FuncAnimation(fig, update, interval=30)

plt.show()
