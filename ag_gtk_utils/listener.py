class BaseListener:
    def __init__(self):
        self.buffer = ""
        self.max_buffer_size = 50
        self.running = False
        self.listener = None
        self._injecting = False
        self._expanding = False
        self._suppress_until = 0.0

    def reset_buffer(self):
        self.buffer = ""
