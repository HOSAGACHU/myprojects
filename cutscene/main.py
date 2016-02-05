import pygame, time

window = pygame.display.set_mode((1024, 682))
pygame.display.set_caption('Final Boss Fight')

screen = pygame.Surface((1024, 682 ))

class Sprite:
	def __init__(self, xpos, ypos, filename):
		self.x=xpos
		self.y=ypos
		self.bitmap=pygame.image.load(filename)
	def render(self):
		screen.blit(self.bitmap,(self.x, self.y))

bgr = pygame.image.load('background.png')

freq = 44100
bitsize = -16
channels = 2
buffer = 4096
pygame.mixer.init(freq, bitsize, channels, buffer)

lgh = pygame.mixer.Sound('lgh.ogg')
intro = pygame.mixer.Sound('intro.ogg')
lgh.set_volume(0.1)
intro.set_volume(0.1)
intro.play()

kef = Sprite(385, -214, 'sprite1.png')

kef.go_down = True

done = True
while done:
        for e in pygame.event.get():
                if e.type == pygame.QUIT:
                        done = False
        if kef.go_down == True:
                kef.y += 0.2
                if kef.y >= 214:
                        kef.go_down = False
                        intro.stop()
                        lgh.play()
                        time.sleep(2)
                        lgh.stop()
                        done = False
                
            
        kef.render()
        window.blit(screen,(0,0))
        screen.blit(bgr, (0, 0))
        pygame.time.delay(5)
        pygame.display.update() 
pygame.quit()
