import torch
from PIL import Image, ImageTk, ImageDraw
from facenet_pytorch import MTCNN

import tkinter as tk
from tkinter import filedialog, messagebox

class CountingFacesApp:
    def __init__(self, app):
        # interface usando tkinter
        self.app = app
        self.app.title("Face Counting App")
        self.mtcnn = MTCNN()
        
        self.min_threshold = tk.Label(app,text="Confiança")
        self.min_threshold.pack()  
        self.threshold = tk.Entry(app, validatecommand=self.app.register((self.validate_value_threshold),'%P'))
        self.threshold.pack()
        self.threshold.insert(0, "0.7")

        self.insert_image = tk.Button(app, text="Escolha a imagem",command=self.upload_imge)
        self.insert_image.pack()

        self.run_button = tk.Button(app, text="Contar faces",command=self.count_faces)
        self.run_button.pack()

        self.image_label = tk.Label(app)
        self.image_label.pack()
        

    def validate_value_threshold(self, min_value_threshold):
        try:
            if(0<= min_value_threshold <= 0.9 or min_value_threshold == ""):
                return True
            return False
        except ValueError:
            return False
        
    def upload_imge(self):
        self.image_path = filedialog.askopenfilename(title="Ao escolher,  clique em abrir ", filetypes=[("Imagens", ".jpg .jpeg .png")])
        if(self.image_path):
            img = Image.open(self.image_path)
            img.thumbnail((432, 432)) 
            self.img_to_tk = ImageTk.PhotoImage(img)
            self.image_label.config(image=self.img_to_tk)
            self.image_label.image = self.img_to_tk
            
    def count_faces(self):
        if(not self.image_path):
            messagebox.showwarning("antes de começar a contagem de faces, escolha uma imagem!")
            return
        try:
            # detectar classe 'face' com  MTCNN - Multi-task Cascaded Convolutional Networks
            img = Image.open(self.image_path)
            boxes, scores = self.mtcnn.detect(img)
            min_threshold = float(self.threshold.get())
            
            # contagem
            filtered_boxes = list()
            if (boxes is not None):
                for i, box in enumerate(boxes):
                    if (scores[i] >= min_threshold):
                        filtered_boxes.append(box)

            num_faces = len(filtered_boxes)
            messagebox.showinfo("Resultado", f"{num_faces} faces detectadas")

            # bbox
            img_draw = img.copy()
            draw = ImageDraw.Draw(img_draw)
            for box in filtered_boxes:
                draw.rectangle(box.tolist(), outline='green', width=4)
                
            img_draw.thumbnail((432, 432))
            self.img_to_tk = ImageTk.PhotoImage(img_draw)
            self.image_label.config(image=self.img_to_tk)
            self.image_label.image = self.img_to_tk
            
        except Exception as e:
            messagebox.showerror(f"Error {e}")

if __name__ == "__main__":
    run = tk.Tk()
    app = CountingFacesApp(run)
    run.mainloop()

        