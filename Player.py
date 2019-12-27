class Player:
    x = []
    y = []
    step = 32
    direction = 0 # TODO: Can this become an enum?
    length = 3

    updateCountMax = 2
    updateCount = 0

    def __init__(self, length):
        self.length = length
        
        for i in range(0, 2000):
            self.x.append(100)
            self.y.append(100)

        # initial positions, no collision (TODO: improve this!)
        self.x[1] = 1 * self.step
        self.x[2] = 2 * self.step

    def update(self):

        self.updateCount = self.updateCount + 1
        if self.updateCount & self.updateCountMax:

            # update previous position
            for i in range(self.length-1, 0, -1):
                self.x[i] = self.x[i-1]
                self.y[i] = self.y[i-1]

            # update position of the head of the snake
            if self.direction == 0:
                if(self.x[0] + self.step >= 800):
                    self.x[0] = 0
                else:
                    self.x[0] = self.x[0] + self.step

            if self.direction == 1:
                if(self.x[0] - self.step <= 0):
                    self.x[0] = 800
                else:
                    self.x[0] = self.x[0] - self.step

            if self.direction == 2:
                if(self.y[0] - self.step <= 0):
                    self.y[0] = 600
                else:
                    self.y[0] = self.y[0] - self.step

            if self.direction == 3:
                if(self.y[0] + self.step >= 600):
                    self.y[0] = 0
                else:
                    self.y[0] = self.y[0] + self.step

            self.updateCount = 0

    def moveRight(self):
        if(self.direction != 1):
            self.direction = 0

    def moveLeft(self):
        if(self.direction != 0):
            self.direction = 1

    def moveUp(self):
        if(self.direction != 3):
            self.direction = 2

    def moveDown(self):
        if(self.direction != 4):
            self.direction = 3

    def draw(self, surface, image):
        for i in range(0, self.length):
            surface.blit(image, (self.x[i], self.y[i]))
