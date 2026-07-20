import logging
import time

logger = logging.getLogger(__name__)

class BaseListener:
    """
    Base listener handling generic buffer management and state tracking
    for keyboard listeners.
    """
    def __init__(self):
        self.buffer = ""
        self.max_buffer_size = 50
        
        self.running = False
        self.listener = None
        
        # Injection guards
        self._injecting = False
        self._expanding = False
        self._suppress_until = 0.0
        
    def start(self):
        """Must be implemented by subclass."""
        raise NotImplementedError
        
    def stop(self):
        if self.listener:
            try:
                self.listener.stop()
            except Exception:
                pass
        self.running = False

    def reset_buffer(self):
        """Clears the typing buffer."""
        self.buffer = ""
