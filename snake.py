class Snake:
    def __init__(self, block_size , initial_x, initial_y):
        self.block_size = block_size
        self.snake_body = [
            (initial_x, initial_y), #head
            (initial_x - block_size , initial_y) ,#body
            (initial_x - 2 * block_size , initial_y) #tail
            ]
        self.diretion = 'right'
        self.head = self.snake_body[0]

    def move(self):
        if self.diretion == 'up':
            new_head = (self.head[0], self.head [1] - self.block_size)
        if self.diretion == 'down':
            new_head = (self.head[0], self.head [1] + self.block_size)
        if self.diretion == 'right':
            new_head = (self.head[0] + self.block_size , self.head [1])
        if self.diretion == 'left':
            new_head = (self.head[0] - self.block_size , self.head [1])

        self.snake_body.insert(0 , new_head)
        self.head = self.snake_body[0] #update head

    def remove_tail(self):
        self.snake_body.pop()
