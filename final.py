import sys

import pygame
from pygame import key, font

class App():
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Be the Webb!")
        font.init()

        self.size = self.width, self.height = 550, 600
        self.screen = pygame.display.set_mode(self.size)

        self.focus_list = [
                           6, 6, 6,
                           5, 5, 5,
                           4, 4, 4,
                           3, 3, 3,
                           2, 2, 2,
                           1, 1, 1, 1, 1,
                           2, 2, 2,
                           3, 3, 3,
                           4, 4, 4,
                           5, 5, 5,
                           6, 6, 6] # 1: máxima/6: mínima
        self.current_focus = 0

    def loop(self):
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.pick_filename()

            self.check_focus()
            self.screen.fill((0, 0, 0))  # black/negro
            self.screen.blit(self.img, self.img_rect)
            self.draw_text("You're the James Webb telescope (JWST) now! Let's take a photo of the universe!", 450, ((170, 238, 187)))
            self.draw_text("Use W and S keys to adjust the focus of your len, until it's totally focused.", 470, ((170, 238, 187)))
            self.text_focus()
            self.send_reaction()
            pygame.display.flip()

    def check_focus(self):
        pos = self.focus_list[self.current_focus]
        fname = f"images/image_{pos}.png"
        self.img = pygame.image.load(fname)
        self.img_rect = self.img.get_rect()

    def pick_filename(self):
        if key.get_pressed()[pygame.K_w] and self.current_focus < 34:
            self.current_focus += 1
        if key.get_pressed()[pygame.K_s] and self.current_focus > 0:
            self.current_focus -= 1

    def draw_text(self, msg, text_y, color):
        fnt = font.Font(None, 20)
        text = fnt.render(msg, True, color)
        textpos = text.get_rect(centerx=self.screen.get_width() / 2, y=text_y)
        self.screen.blit(text, textpos)

    def text_focus(self):
        txt2 = False

        if self.focus_list[self.current_focus] in (6, 5):
            txt = "Blurry"
            col = ((200, 0, 0))
        elif self.focus_list[self.current_focus] in (3, 4):
            txt = "Good"
            col = ((242, 236, 6))
        elif self.focus_list[self.current_focus] == 2:
            txt = "Almost focused"
            col = ((145, 148, 21))
        elif self.focus_list[self.current_focus] == 1:
            txt = "Focused!"
            txt2 = True
            col = ((5, 219, 0))
        self.draw_text(f"JWST len status: {txt}", 490, col)
        if txt2:
            self.draw_text("Press SPACE to send this image back to Earth!", 510, ((2, 209, 253)))
            self.draw_text("This will also quit the game. Thanks for playing, and keep learning!", 525, ((2, 209, 253)))


    def send_reaction(self):
        if self.focus_list[self.current_focus] == 1 and key.get_pressed()[pygame.K_SPACE]:
            print("Image received at Earth! Thank you!")
            sys.exit()

if __name__ == '__main__':
    app = App()
    app.loop()
