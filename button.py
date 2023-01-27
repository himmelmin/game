import pygame
pygame.font.init()
# 게임 화면 크기 설정
screen_width = 1280  # 가로 크기
screen_height = 700  # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))
main_font = pygame.font.SysFont("cambria", 30)

class Button():
	def __init__(self, image, x_pos, y_pos, text_input):
		self.image = image
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.clicked = False
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		self.text_input = text_input
		self.text = main_font.render(self.text_input, True, "white")
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))
	def update(self):
		screen.blit(self.image, self.rect)
		screen.blit(self.text, self.text_rect)

	# # Button
	# def checkForInput(self, position):
	# 	if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
	# 		print("Button Press!")

	#Button
	def changeColor(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = main_font.render(self.text_input, True, "green")
		else:
			self.text = main_font.render(self.text_input, True, "white")
	#Exit
	def changeColor2(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = main_font.render(self.text_input, True, "Red")
		else:
			self.text = main_font.render(self.text_input, True, "white")
	def draw(self, surface):
		action = False
		#get mouse position
		pos = pygame.mouse.get_pos()

		#check mouseover and clicked conditions
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				action = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False

		#draw button on screen
		surface.blit(self.image, (self.rect.x, self.rect.y))

		return action