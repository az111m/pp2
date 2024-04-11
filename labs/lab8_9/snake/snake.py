import pygame              
import random              

pygame.init() 

SW, SH = 600, 600
WW, WH = 600, 700

BLOCK_SIZE = 40
FONT = pygame.font.SysFont("Futura", BLOCK_SIZE)    

screen = pygame.display.set_mode((WW, WH))
pygame.display.set_caption("snake")
clock = pygame.time.Clock()

class Snake:
    def __init__(self):
        self.x, self.y = BLOCK_SIZE, BLOCK_SIZE
        self.xdir = 1
        self.ydir = 0
        self.head = pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE) 
        self.body = [pygame.Rect(self.x-BLOCK_SIZE, self.y, BLOCK_SIZE, BLOCK_SIZE)]
        self.dead = False 
        self.restart = False 

    def update(self):
        global apple, wall, golden_apple

        for square in self.body:
            if self.head.x == square.x and self.head.y == square.y: 
                self.dead = True
            if self.head.x not in range(0, SW) or self.head.y not in range(0, SH): 
                self.dead = True
        if self.dead and self.restart:
                self.x, self.y = BLOCK_SIZE, BLOCK_SIZE
                self.head = pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)
                self.body = [pygame.Rect(self.x-BLOCK_SIZE, self.y, BLOCK_SIZE, BLOCK_SIZE)]
                self.xdir = 1
                self.ydir = 0
                self.dead = False
                self.restart = False
                apple = Apple() 
                wall = Wall() 
                golden_apple = GoldenApple(self.body, (apple.x, apple.y), [barrier for barrier in wall.barriers]) 
        self.body.append(self.head)
        for i in range(len(self.body) - 1):
            self.body[i].x, self.body[i].y = self.body[i+1].x, self.body[i+1].y
        self.head.x += self.xdir * BLOCK_SIZE
        self.head.y += self.ydir * BLOCK_SIZE
        self.body.remove(self.head)

class Apple:
    def __init__(self):
        self.spawn_apple()
        self.spawn_time = pygame.time.get_ticks() 
    def spawn_apple(self):
        self.x = int(random.randint(0, SW) / BLOCK_SIZE) * BLOCK_SIZE
        self.y = int(random.randint(0, SH) / BLOCK_SIZE) * BLOCK_SIZE
    def update(self, snake_body): 
        if pygame.time.get_ticks() - self.spawn_time >= 5000: 
            self.spawn_apple() 
            self.spawn_time = pygame.time.get_ticks()
        while (self.x, self.y) in [(square.x, square.y) for square in snake_body]:
            self.spawn_apple()
        self.new_apple = pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)
        pygame.draw.rect(screen, "red", self.new_apple)

class GoldenApple:
    def __init__(self, snake_body, apple_pos, wall_barriers):
        self.spawn_time = pygame.time.get_ticks()
        self.golden_apple_rect = None
        if random.random() <= 0.1: 
            self.spawn_golden_apple(snake_body, apple_pos, wall_barriers) 
    def spawn_golden_apple(self, snake_body, apple_pos, wall_barriers):
        while True:
            self.x = int(random.randint(0, SW) / BLOCK_SIZE) * BLOCK_SIZE
            self.y = int(random.randint(0, SH) / BLOCK_SIZE) * BLOCK_SIZE
            if (self.x, self.y) not in apple_pos and \
               (self.x, self.y) not in [(square.x, square.y) for square in snake_body] and \
               (self.x, self.y) not in [(barrier.x, barrier.y) for barrier in wall_barriers]:
                self.golden_apple_rect = pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)
                break
    def update(self, snake_body, apple_pos, wall_barriers):
        current_time = pygame.time.get_ticks()

        if self.golden_apple_rect is not None: 
            if current_time - self.spawn_time >= 3000: 
                self.golden_apple_rect = None  
        else: 
            if random.random() <= 0.1:  
                self.spawn_golden_apple(snake_body, apple_pos, wall_barriers)
                self.spawn_time = current_time

        if self.golden_apple_rect is not None: 
            pygame.draw.rect(screen, "gold", self.golden_apple_rect)

class Wall:
    def __init__(self):
        self.barriers = []
    def spawn_barrier(self, snake_body, apple_pos, snake_head_pos):
        while True:
            self.x = int(random.randint(0, SW) / BLOCK_SIZE) * BLOCK_SIZE
            self.y = int(random.randint(0, SH) / BLOCK_SIZE) * BLOCK_SIZE
            new_barrier = pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE) 
            if new_barrier.collidelist(snake_body) == -1 and new_barrier.collidepoint(apple_pos) == False: 
                if abs(snake_head_pos[0] - new_barrier.x) > 3 * BLOCK_SIZE or abs(snake_head_pos[1] - new_barrier.y) > 3 * BLOCK_SIZE:
                    self.barriers.append(new_barrier)
                    break    
    def update(self, snake_body, apple_pos, snake_head_pos, eaten_fruits):
        for barrier in self.barriers:
            pygame.draw.rect(screen, "blue", barrier)
            if barrier.colliderect(snake_head_pos): 
                snake.dead = True

        eaten_fruits = eaten_fruits // 2
        if eaten_fruits > len(self.barriers):
            for _ in range(eaten_fruits - len(self.barriers)):
                self.spawn_barrier(snake_body, apple_pos, snake_head_pos)
def drawGrid():
    for x in range(0, SW, BLOCK_SIZE):
        for y in range(0, SH, BLOCK_SIZE):
            rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(screen, (60, 60, 60), rect, 1)

score = speed = eaten_fruits = 0
scoretxt = speedtxt = leveltxt = FONT.render("0", True, "white")
score_rect = scoretxt.get_rect(center=(20, 620))
speed_rect = speedtxt.get_rect(center=(20, 660))
level_rect = leveltxt.get_rect(center=(480, 620))

drawGrid()
snake = Snake()
apple = Apple()
wall = Wall()
golden_apple = GoldenApple(snake.body, (apple.x, apple.y), [barrier for barrier in wall.barriers])

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: 
                done = True
            elif event.key == pygame.K_SPACE:
                snake.restart = True
                score = speed = eaten_fruits = 0
            if event.key == pygame.K_DOWN: 
                snake.ydir = 1
                snake.xdir = 0
            elif event.key == pygame.K_UP:
                snake.ydir = -1
                snake.xdir = 0
            elif event.key == pygame.K_RIGHT:
                snake.ydir = 0
                snake.xdir = 1
            elif event.key == pygame.K_LEFT:
                snake.ydir = 0
                snake.xdir = -1

    snake.update()

    screen.fill("black")

    drawGrid()

    wall.update(snake.body, (apple.x, apple.y), snake.head, eaten_fruits)

    apple.update(snake.body)

    golden_apple.update(snake.body, (apple.x, apple.y), [barrier for barrier in wall.barriers])

    pygame.draw.rect(screen, (0, 255, 0), snake.head)
    pygame.draw.rect(screen, (42, 42, 42), [0, SH, WW, WH]) 
    scoretxt = FONT.render(f"score: {score}", True, (138, 154, 91)) 
    speedtxt = FONT.render(f"speed: {speed + 5}", True, (96, 130, 182))
    leveltxt = FONT.render(f"level: {eaten_fruits//2}", True, (207, 159, 255))
    screen.blit(scoretxt, score_rect)
    screen.blit(speedtxt, speed_rect)
    screen.blit(leveltxt, level_rect)

    for square in snake.body:
        pygame.draw.rect(screen, (0, 65, 0), square)

    if golden_apple.golden_apple_rect is not None and snake.head.colliderect(golden_apple.golden_apple_rect):
        snake.body.append(pygame.Rect(square.x, square.y, BLOCK_SIZE, BLOCK_SIZE))
        golden_apple = GoldenApple(snake.body, (apple.x, apple.y), [barrier for barrier in wall.barriers])
        eaten_fruits += 1
        score += 3
        if (len(snake.body)-1) % 5 == 0: 
            speed += 0.5

    if snake.head.x == apple.x and snake.head.y == apple.y:
        snake.body.append(pygame.Rect(square.x, square.y, BLOCK_SIZE, BLOCK_SIZE)) 
        apple = Apple()
        eaten_fruits += 1
        score += 1
        if (len(snake.body)-1) % 5 == 0: 
            speed += 0.5

    for barrier in wall.barriers:
        if apple.x == barrier[0] and apple.y == barrier[1]:
            apple.spawn_apple()

    if snake.dead and not snake.restart:
        screen.fill("black")
        endtxt = FONT.render(f"your score: {score}", True, "red") 
        end_rect = endtxt.get_rect(center=(SW/2, SH/2))
        screen.blit(endtxt, end_rect)

    pygame.display.update() 
    clock.tick(5 + speed) 