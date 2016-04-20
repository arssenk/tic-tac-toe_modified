class BTNode(object):
    def __init__(self, data =  None):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

    def get_board(self):
        return self.data
