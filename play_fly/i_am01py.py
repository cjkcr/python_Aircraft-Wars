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
screen.blit(hero,(150,300))





# 创建时钟
clock = pygame.time.Clock()
# 1，定义飞机的初始位置
hero_rect = pygame.Rect(150,300,100,124)


while True:
#指定代码执行频率
    clock.tick(60)  #每秒60帧
#捕获事件
    for event in pygame.event.get():
#事件监听用户是否点击了关闭
        if event.type ==pygame.QUIT:
            
            print('不玩了宝宝')
            time.sleep(2)

            pygame.quit()
#直接退出

            exit()



# 修改飞机位置
    hero_rect.y -=1
#判断飞的位置，是否出了地图
    if hero_rect.y<=-124:
        hero_rect.y=723



#刷新背景
    screen.blit(bg,(0,0))
# 刷新飞机
    screen.blit(hero,hero_rect)
# 最后只调用一次更新显示
    pygame.display.update()

pygame.quit()