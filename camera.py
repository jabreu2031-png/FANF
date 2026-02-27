class Camera:
    """
    A class to manage camera feeds, room navigation, and security monitoring.
    """

    def __init__(self, label):
        self.label = label  # The label for the camera
        self.feed = None  # Placeholder for the camera feed

    def start_feed(self):
        """
        Starts the camera feed.
        """
        self.feed = "Feed from camera: {}".format(self.label)
        print(self.feed)

    def stop_feed(self):
        """
        Stops the camera feed.
        """
        self.feed = None
        print("Camera feed stopped.")

    def navigate_room(self, room):
        """
        Navigate to a specified room.
        """
        print("Navigating to room: {}".format(room))

    def monitor_security(self):
        """
        Start monitoring for security purposes.
        """
        print("Monitoring security with camera: {}".format(self.label))

# Example usage:
if __name__ == '__main__':
    camera1 = Camera("Lobby")
    camera1.start_feed()
    camera1.navigate_room("Conference Room")
    camera1.monitor_security()
    camera1.stop_feed()