import random
import pygame

# 屏幕大小的常量
SCREEN_RECT = pygame.Rect(0, 0, 400, 700)
# 设置刷新帧率
FRAME_PER_SEC = 60
# 创建敌机的定时器常量
CREATE_ENEMY_EVENT = pygame.USEREVENT


class GameSprite(pygame.sprite.Sprite):
    """飞机大战游戏精灵"""

    def __init__(self, image_name, speed=1):
        # 调用父类的初始化方法
        super().__init__()

        # 定义对象的属性
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        # 在屏幕的垂直方向移动
        self.rect.y += self.speed


class Background(GameSprite):  # 父类的方法不能满足子类的需求
    """游戏背景精灵"""

    def __init__(self, is_alt=False):

        # 1.调用父类的方法实现精灵的创建(image/rect/speed)
        super().__init__("./images/background.png")

        # 2.判断是否是交替图像,如果是,需要设置初始位置
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self):

        # 1.调用父类的方法实现
        super().update()

        # 2.判断是否移除屏幕，如果移出屏幕，将图像设置到屏幕的正上方
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height
        pass


class Enemy(GameSprite):
    """敌机精灵"""

    def __init__(self):
        # 1.调用父类方法调用敌机精灵
        super().__init__("./images/enemy1.png")

        # 2.指定敌机的初始速度　１～３
        self.speed = random.randint(1, 3)

        # 3.指定敌机的初始位置
        self.rect.bottom = 0

        max_x = SCREEN_RECT.width - self.rect.width  # 屏幕宽度减去图像宽度
        self.rect.x = random.randint(0, max_x)

    def update(self):
        # 1.调用父类方法，保持垂直方向的飞行
        super().update()
        # 2.判断敌机是否飞出屏幕，若飞出，则从精灵组中删除
        if self.rect.y >= SCREEN_RECT.height:
            # print("飞出屏幕，需要从精灵组删除.....")
            # kill将精灵从所有组中删除,精灵就会被自动销毁

            self.kill()

    def __del__(self):
        # print("敌机挂了　%s" % self.rect)
        pass


class Hero(GameSprite):
    """英雄精灵"""

    def __init__(self):

        # 1.调用父类方法，设置image&speed
        super().__init__("./images/me1.png", 0)

        # 2.设置英雄的初始位置
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120
