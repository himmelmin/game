from map_make import *
pygame.init()
menu_state = "main"

running = True
while running:
    if menu_state == "main":
        opening_sound.play(-1)
        opening_make()
        if start_button.draw(screen):
            menu_state = "map"
        elif rule_button.draw(screen):
            menu_state = "rule"
        elif exit_button.draw(screen):
            running = False
    if menu_state == "rule":
        rule_make()
        if back_button.draw(screen):
            menu_state = "main"
    if menu_state == "map":
        opening_sound.stop()
        map_sound.play(-1)
        map_make()
    # 2. 이벤트 처리 (키보드. 마우스 등)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()