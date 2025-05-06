# part1_sku_mapper/gui.py

import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
from sku_mapper import SKUMapper

class SKUApp:
    def __init__(self, root):
        self.root = root
        self.root.title("WMS SKU Mapper")

        self.load_btn = tk.Button(root, text="Load Sales File", command=self.load_file)
        self.load_btn.pack()

        self.map_btn = tk.Button(root, text="Map SKUs", command=self.map_skus)
        self.map_btn.pack()

    def load_file(self):
        path = filedialog.askopenfilename(initialdir=r"C:\Users\aadit\OneDrive\Documents\OneDrive\Desktop\Wms_project\part1_sku_mapper", title="Select Sales File")
        self.sales_df = pd.read_excel(path)
        messagebox.showinfo("Loaded", f"{len(self.sales_df)} rows loaded.")

    def map_skus(self):
        mapper = SKUMapper("src/Book1.xlsx")  # Assuming this contains your SKU→MSKU mappings
        mapped_df = mapper.map_skus(self.sales_df)
        mapped_df.to_excel("output_mapped.xlsx", index=False)
        messagebox.showinfo("Done", "Mapped SKUs saved to output_mapped.xlsx")

if __name__ == "__main__":
    root = tk.Tk()
    app = SKUApp(root)
    root.mainloop()
