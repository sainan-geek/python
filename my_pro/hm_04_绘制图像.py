import pygame

pygame.init()

# 创建游戏的窗口 480 * 700
screen = pygame.display.set_mode((480, 700))

# 绘制背景图像
# > 加载图像数据
bg = pygame.image.load("./images/background.png") # .当前文件夹下 返回值用bg记录
# > blit绘制图像
screen.blit(bg, (0, 0))
# > update 更新屏幕显示
pygame.display.update() # 要想在屏幕上显示一定要调用

while True:
    pass
pygame.quit()