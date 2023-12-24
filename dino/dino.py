import pygame
pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption('Chào Mừng Đã Đến Với Trò Chơi')
screen = pygame.display.set_mode((600, 300))
bg = pygame.image.load(r'assets\background2.jpg')
ball = pygame.image.load(r'assets\ball.png')
dino = pygame.image.load(r'assets\dinosaur1.png')
anhnen = pygame.image.load(r'assets\anhnenchonman.png')
sound1 = pygame.mixer.Sound(r'sound\nhay.wav')
sound2 = pygame.mixer.Sound(r'sound\te.wav')
score, hscore = 0, 0
bg_x, bg_y = 0, 0
ball_x, ball_y = 550, 230
dino_x, dino_y = 0, 230
x_def, y_def = 5, 7
jump = False
gameplay = False  # Bắt đầu với gameplay = False
#Check loi
def checkvc():
    if dino_hcn.colliderect(ball_hcn):
        pygame.mixer.Sound.play(sound2)
        return False
    return True

# Tạo màn hình chọn cấp độ
def choose_difficulty():
    global x_def, y_def, gameplay
    selecting_difficulty = True
    while selecting_difficulty:
        screen.blit(anhnen, (0, 0))  # Màu nền trắng
        font = pygame.font.Font(None, 36)
        text_easy = font.render("1. easy", True, (0, 0, 0))
        text_medium = font.render("2.medium ", True, (0, 0, 0))
        text_hard = font.render("3. hard", True, (0, 0, 0))
        screen.blit(text_easy, (250, 100))
        screen.blit(text_medium, (250, 150))
        screen.blit(text_hard, (250, 200))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    x_def, y_def = 2 , 3  # Thiết lập cấp độ Dễ
                    gameplay = True
                    selecting_difficulty = False
                elif event.key == pygame.K_2:
                    x_def, y_def = 5, 7  # Thiết lập cấp độ Trung bình
                    gameplay = True
                    selecting_difficulty = False
                elif event.key == pygame.K_3:
                    x_def, y_def = 10 ,13  # Thiết lập cấp độ Khó
                    gameplay = True
                    selecting_difficulty = False

# Gọi hàm chọn cấp độ trước khi bắt đầu trò chơi
choose_difficulty()
game_font=pygame.font.Font('nen.TTF',20)
def score_view():
    if gameplay:
        score_txt=game_font.render(f'Score: {int(score)}',True,(255,255,0))
        screen.blit(score_txt,(250,50))
        hscore_txt=game_font.render(f'High Score: {int(hscore)}',True,(255,255,0))
        screen.blit(hscore_txt,(250,30))
    else:
        score_txt=game_font.render(f'Score: {int(score)}',True,(255,255,0))
        screen.blit(score_txt,(250,50))
        hscore_txt=game_font.render(f'High Score: {int(hscore)}',True,(255,255,0))
        screen.blit(hscore_txt,(250,30))
        over_txt=game_font.render(f'Game over',True,(255,0,0))
        screen.blit(over_txt,(250,200))
1
game_font=pygame.font.Font('nen.TTF',20)
def score_view():
    if gameplay:
        score_txt=game_font.render(f'Score: {int(score)}',True,(255,255,0))
        screen.blit(score_txt,(250,50))
        hscore_txt=game_font.render(f'High Score: {int(hscore)}',True,(255,255,0))
        screen.blit(hscore_txt,(250,30))
    else:
        score_txt=game_font.render(f'Score: {int(score)}',True,(255,255,0))
        screen.blit(score_txt,(250,50))
        hscore_txt=game_font.render(f'High Score: {int(hscore)}',True,(255,255,0))
        screen.blit(hscore_txt,(250,30))
        over_txt=game_font.render(f'Game over',True,(255,0,0))
        screen.blit(over_txt,(250,200))
running = True
while running:
    clock.tick(90)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and gameplay:
                if dino_y == 230:
                    jump = True
                    pygame.mixer.Sound.play(sound1)
            if event.key == pygame.K_SPACE and not gameplay:
                gameplay = True

    if gameplay:
        # Các phần code xử lý game khi gameplay = True
        #bg
        bg_hcn=screen.blit(bg,(bg_x,bg_y))
        bg2_hcn=screen.blit(bg,(bg_x+600,bg_y))
        bg_x-=x_def
        if bg_x==-600: bg_x=0
        #ball
        ball_hcn=screen.blit(ball,(ball_x,ball_y))
        ball_x-=x_def
        if ball_x==-20: ball_x=550
        #Robot
        dino_hcn=screen.blit(dino,(dino_x,dino_y))
        #Dieu khien dino
        if dino_y>=80 and jump:
            dino_y-=y_def
        else:
            jump=False
        if dino_y<230 and jump==False:
            dino_y+=y_def
        score+=0.1
        if hscore<score : hscore=score
        gameplay=checkvc()
        score_view()
    else:
        bg_x,bg_y=0,0
        ball_x,ball_y=550,230
        dino_x,dino_y=0,230
        bg_hcn=screen.blit(bg,(bg_x,bg_y))
        ball_hcn=screen.blit(ball,(ball_x,ball_y))
        dino_hcn=screen.blit(dino,(dino_x,dino_y))
        score=0
        score_view()    
    pygame.display.update()

pygame.quit()