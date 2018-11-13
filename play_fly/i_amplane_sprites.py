import pygame

class GameSprite(pygame.sprite.Sprite):
    '''飞机大战精灵'''
    def __init__(self,image_name,speed=1):
#调用父类的初始化方法

        super().__init__()

#宝义对像的属性
        self.image = pygame.image.load()
        self.rect = self.image.get_rect()
        self.speed =speed



    def update(self, *args):
#