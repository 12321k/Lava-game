from pygame import *

init()

size = 600, 800
window = display.set_mode(size)
clock = time.Clock()

font1 = font.Font(None, 60)


class Buttons:
    def __init__(self, x, y, width, height, text, color=(255, 0, 0), img=None):
        self.img = img
        if self.img:
            self.img = transform.scale(image.load(img), (width, height))
            self.rect = self.img.get_rect()
            self.rect.x = x
            self.rect.y = y
        else:
            self.rect = Rect(x, y, width, height)
        self.color = color
        self.text = font1.render(text, True, (0, 0, 0))
        self.rect_text = self.text.get_rect()
        self.rect_text.x = self.rect.x
        self.rect_text.y = self.rect.y

    def show_button(self):
        if self.img:
            window.blit(self.img, (self.rect.x, self.rect.y))
        else:
            draw.rect(window, self.color, self.rect, border_radius=15)
        window.blit(self.text, (self.rect_text.x, self.rect_text.y))


btn1 = Buttons(200, 400, 200, 120, 'Click', (0, 255, 0))
btn2 = Buttons(200, 600, 200, 120, 'Click2')

while True:
    for e in event.get():
        if e.type == QUIT:
            quit()

    btn1.show_button()
    btn2.show_button()

    display.update()
    clock.tick(60)