import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
	"""表示打那个外星人的类"""

	def __init__(self, ai_game):
		"""初始化外星人并设置其初始位置"""
		super().__init__()
		self.screen = ai_game.screen

		# 加载外星人图形并设置其rect属性
		self.image = pygame.image.load('images/alien.bmp')
		self.rect = self.image.get_rect()

		# 最初每个外星人都在屏幕左上角
		self.rect.x = self.rect.width
		self.y = self.rect.height

		# 存储外星人的准确位置
		self.x = float(self.rect.x)