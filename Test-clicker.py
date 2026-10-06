#!/usr/bin/env python3
"""Simple GUI autoclicker. Install its click backend with: python -m pip install pyautogui"""

import threading
import time
import tkinter as tk
from tkinter import messagebox

try:
	import pyautogui
except ImportError:
	pyautogui = None


class AutoClicker:
	def __init__(self, root):
		self.root = root
		self.root.title("AutoClicker")
		self.root.resizable(False, False)
		self.running = threading.Event()

		tk.Label(root, text="Click interval (seconds):").pack(padx=18, pady=(16, 4))
		self.interval = tk.StringVar(value="0.1")
		tk.Entry(root, textvariable=self.interval, width=12, justify="center").pack()

		self.button = tk.Button(root, text="Start", width=14, command=self.toggle)
		self.button.pack(pady=12)
		self.status = tk.Label(root, text="Stopped")
		self.status.pack(pady=(0, 14))
		root.protocol("WM_DELETE_WINDOW", self.close)

	def toggle(self):
		if self.running.is_set():
			self.running.clear()
			self.button.config(text="Start")
			self.status.config(text="Stopped")
			return

		try:
			delay = float(self.interval.get())
			if delay <= 0:
				raise ValueError
		except ValueError:
			messagebox.showerror("Invalid interval", "Enter a number greater than zero.")
			return

		if pyautogui is None:
			messagebox.showerror(
				"Missing dependency", "Install pyautogui with: python -m pip install pyautogui"
			)
			return

		self.running.set()
		self.button.config(text="Stop")
		self.status.config(text="Clicking at the current pointer position")
		threading.Thread(target=self.click_loop, args=(delay,), daemon=True).start()

	def click_loop(self, delay):
		while self.running.is_set():
			pyautogui.click()
			if self.running.wait(delay):
				break

	def close(self):
		self.running.clear()
		self.root.destroy()


if __name__ == "__main__":
	window = tk.Tk()
	AutoClicker(window)
	window.mainloop()
