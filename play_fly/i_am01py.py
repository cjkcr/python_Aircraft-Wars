import pygame

# 初始化
pygame.init()
import time
# print('good game')
#
# hero_rect=pygame.Rect(100,500,100,124)
# print(hero_rect.x,hero_rect.y)
# print(hero_rect.width,hero_rect.height)
# print(hero_rect.size)
# 创建窗口大小  480,852
screen = pygame.display.set_mode((483,723))
# 绘制背景图像
# 1，加载图像
bg=pygame.image.load('./feiji/meground.jpg')
# 2，blit绘制图像
screen.blit(bg,(0,0))
# 3，更新显示(可以在所有绘制完成后统一更新显示
# pygame.display.update()

# 上飞机
hero=pygame.image.load('./feiji/hero1.png')
#
screen.blit(hero,(150,500))



# 最后只调用一次更新显示
pygame.display.update()
# 创建时钟
clock = pygame.time.Clock()
# 1，定义飞机的初始位置



while True:
#指定代码执行频率
    clock.tick(60)  #每秒60帧
# 修改飞机位置

#

pygame.quit()