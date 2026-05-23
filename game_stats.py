class GameStats:
    """Tracking statistics for the game"""

    def __init__(self,ai_game):
        """Initializing statistics"""
        self.settings = ai_game.settings
        self.reset_stats()

    def reset_stats(self):
            