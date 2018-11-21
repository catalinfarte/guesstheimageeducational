from PIL import ImageTk, Image
import predictor
import tkinter as tk

window = tk.Tk()
window.title("What's in the image?")
window.geometry("1000x400")
window.configure(background='grey')
img = ImageTk.PhotoImage(Image.open("1.jpg"))
imageLabel = tk.Label(window, image=img)
imageLabel.place(x=0, y=0)

predictionsList = predictor.guessTheImage()  # Aplicatia incepe in momentul acesta procesul de a ghicii imaginea.
counter = 0

for prediction, possibility in predictionsList.items():
    label = tk.Label(window, text=str(prediction) + " : " + str(possibility), background='grey')
    label.place(x=800, y=10 + (30 * counter))
    counter += 1

window.mainloop()