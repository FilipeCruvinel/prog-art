from tkinter import *
import math
tela = Tk()
tela.title("Prog-art - arte programada")
tela.geometry("1280x720")
def corRGB(r, g, b):
	return f"#{r:02x}{g:02x}{b:02x}"
canvas = Canvas(tela, width = 1280, height = 720, bg = corRGB(255, 255, 255))
canvas.pack()
corFundo = corRGB(255, 255, 225)
corLapis = corRGB(0, 0, 0)
posicao = [640.0, 360.0]
giro = 0
apagados = []
def circulo (raio):
	global posicao
	global giro
	global corFundo
	global corLapis
	global corPinta
	global apagados
	canvas.create_arc((posicao[0] - raio * math.cos(math.radians(giro - 90))) - raio, (posicao[1] + raio * math.sin(math.radians(giro - 90))) - raio, 
			(posicao[0] - raio * math.cos(math.radians(giro - 90))) + raio, (posicao[1] + raio * math.sin(math.radians(giro - 90))) + raio, 
			start = giro - 90, extent = 359, style = "arc", outline = corLapis)
	posicao = [(posicao[0] - raio * math.cos(math.radians(giro - 90))) + raio * math.cos(math.radians(giro - 90 + 359)), 
			(posicao[1] + raio * math.sin(math.radians(giro - 90))) - raio * math.sin(math.radians(giro - 90 + 359))]
	giro = giro + 359
def quadrado (lado):
	global posicao
	global giro
	global corFundo
	global corLapis
	global corPinta
	global apagados
	canvas.create_line(posicao[0], posicao[1], posicao[0] + lado * math.cos(math.radians(giro)), 
			posicao[1] - lado * math.sin(math.radians(giro)), fill = corLapis)
	posicao = [posicao[0] + lado * math.cos(math.radians(giro)), posicao[1] - lado * math.sin(math.radians(giro))]
	giro = giro - 90
	canvas.create_line(posicao[0], posicao[1], posicao[0] + lado * math.cos(math.radians(giro)), 
			posicao[1] - lado * math.sin(math.radians(giro)), fill = corLapis)
	posicao = [posicao[0] + lado * math.cos(math.radians(giro)), posicao[1] - lado * math.sin(math.radians(giro))]
	giro = giro - 90
	canvas.create_line(posicao[0], posicao[1], posicao[0] + lado * math.cos(math.radians(giro)), 
			posicao[1] - lado * math.sin(math.radians(giro)), fill = corLapis)
	posicao = [posicao[0] + lado * math.cos(math.radians(giro)), posicao[1] - lado * math.sin(math.radians(giro))]
	giro = giro - 90
	canvas.create_line(posicao[0], posicao[1], posicao[0] + lado * math.cos(math.radians(giro)), 
			posicao[1] - lado * math.sin(math.radians(giro)), fill = corLapis)
	posicao = [posicao[0] + lado * math.cos(math.radians(giro)), posicao[1] - lado * math.sin(math.radians(giro))]
	giro = giro - 90
def triangulo (lado):
	global posicao
	global giro
	global corFundo
	global corLapis
	global corPinta
	global apagados
	canvas.create_line(posicao[0], posicao[1], posicao[0] + lado * math.cos(math.radians(giro)), 
			posicao[1] - lado * math.sin(math.radians(giro)), fill = corLapis)
	posicao = [posicao[0] + lado * math.cos(math.radians(giro)), posicao[1] - lado * math.sin(math.radians(giro))]
	giro = giro + 120
	canvas.create_line(posicao[0], posicao[1], posicao[0] + lado * math.cos(math.radians(giro)), 
			posicao[1] - lado * math.sin(math.radians(giro)), fill = corLapis)
	posicao = [posicao[0] + lado * math.cos(math.radians(giro)), posicao[1] - lado * math.sin(math.radians(giro))]
	giro = giro + 120
	canvas.create_line(posicao[0], posicao[1], posicao[0] + lado * math.cos(math.radians(giro)), 
			posicao[1] - lado * math.sin(math.radians(giro)), fill = corLapis)
	posicao = [posicao[0] + lado * math.cos(math.radians(giro)), posicao[1] - lado * math.sin(math.radians(giro))]
	giro = giro + 120
def semicirculo (raio):
	global posicao
	global giro
	global corFundo
	global corLapis
	global corPinta
	global apagados
	canvas.create_arc((posicao[0] - raio * math.cos(math.radians(giro - 90))) - raio, (posicao[1] + raio * math.sin(math.radians(giro - 90))) - raio, 
			(posicao[0] - raio * math.cos(math.radians(giro - 90))) + raio, (posicao[1] + raio * math.sin(math.radians(giro - 90))) + raio, 
			start = giro - 90, extent = 180, style = "arc", outline = corLapis)
	posicao = [(posicao[0] - raio * math.cos(math.radians(giro - 90))) + raio * math.cos(math.radians(giro - 90 + 180)), 
			(posicao[1] + raio * math.sin(math.radians(giro - 90))) - raio * math.sin(math.radians(giro - 90 + 180))]
	giro = giro + 180
corFundo = corRGB(175, 175, 175)
canvas.configure(bg = corFundo)
for apagado in apagados:
	canvas.itemconfig(apagado, fill = corFundo)
posicao[1] = -50 + 360
circulo (80)
posicao[0] = 0 + 640
posicao[1] = -50 + 360
giro = giro - 44
quadrado (120)
posicao[1] = --117 + 360
giro = giro - 75
corLapis = corRGB(255, 255, 0)
triangulo (80)
posicao[1] = -210 + 360
giro = giro + 120
corLapis = corRGB(255, 0, 0)
circulo (50)
posicao = [57 + 640, -187 + 360]
giro = giro - 45
circulo (50)
posicao = [80 + 640, -130 + 360]
giro = giro - 45
circulo (50)
posicao = [-30 + 640, -130 + 360]
giro = giro + 90
corLapis = corRGB(255, 255, 255)
circulo (20)
posicao[1] = -140 + 360
corLapis = corRGB(0, 0, 0)
circulo (10)
posicao = [-70 + 640, -170 + 360]
giro = giro + 140
corLapis = corRGB(255, 255, 0)
canvas.create_line(posicao[0], posicao[1], posicao[0] + 70 * math.cos(math.radians(giro)), 
			posicao[1] - 70 * math.sin(math.radians(giro)), fill = corLapis)
posicao = [posicao[0] + 70 * math.cos(math.radians(giro)), posicao[1] - 70 * math.sin(math.radians(giro))]
giro = giro + 150
canvas.create_line(posicao[0], posicao[1], posicao[0] + 92 * math.cos(math.radians(giro)), 
			posicao[1] - 92 * math.sin(math.radians(giro)), fill = corLapis)
posicao = [posicao[0] + 92 * math.cos(math.radians(giro)), posicao[1] - 92 * math.sin(math.radians(giro))]
posicao = [-70 + 640, -90 + 360]
giro = giro - 425
canvas.create_line(posicao[0], posicao[1], posicao[0] + 65 * math.cos(math.radians(giro)), 
			posicao[1] - 65 * math.sin(math.radians(giro)), fill = corLapis)
posicao = [posicao[0] + 65 * math.cos(math.radians(giro)), posicao[1] - 65 * math.sin(math.radians(giro))]
giro = giro - 146
canvas.create_line(posicao[0], posicao[1], posicao[0] + 87 * math.cos(math.radians(giro)), 
			posicao[1] - 87 * math.sin(math.radians(giro)), fill = corLapis)
posicao = [posicao[0] + 87 * math.cos(math.radians(giro)), posicao[1] - 87 * math.sin(math.radians(giro))]
posicao = [85 + 640, --35 + 360]
giro = giro + 331
corLapis = corRGB(0, 0, 0)
canvas.create_line(posicao[0], posicao[1], posicao[0] + 100 * math.cos(math.radians(giro)), 
			posicao[1] - 100 * math.sin(math.radians(giro)), fill = corLapis)
posicao = [posicao[0] + 100 * math.cos(math.radians(giro)), posicao[1] - 100 * math.sin(math.radians(giro))]
giro = giro + 90
semicirculo (50)
giro = giro + 45
canvas.create_line(posicao[0], posicao[1], posicao[0] + 100 * math.cos(math.radians(giro)), 
			posicao[1] - 100 * math.sin(math.radians(giro)), fill = corLapis)
posicao = [posicao[0] + 100 * math.cos(math.radians(giro)), posicao[1] - 100 * math.sin(math.radians(giro))]
giro = giro + 90
semicirculo (50)
giro = giro + 45
canvas.create_line(posicao[0], posicao[1], posicao[0] + 100 * math.cos(math.radians(giro)), 
			posicao[1] - 100 * math.sin(math.radians(giro)), fill = corLapis)
posicao = [posicao[0] + 100 * math.cos(math.radians(giro)), posicao[1] - 100 * math.sin(math.radians(giro))]
giro = giro + 90
semicirculo (50)
posicao = [-2 + 640, --210 + 360]
canvas.create_text(posicao[0], posicao[1], text = "galo")
tela.mainloop()