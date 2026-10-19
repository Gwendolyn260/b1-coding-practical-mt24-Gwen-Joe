class PDController:
    """Discrete proportional-derivative controller for depth tracking."""
    kp = 0.15
    kd = 0.6


    def __init__(self, kp: float = 0.15, kd: float = 0.6):
        self.kp = kp
        self.kd = kd
        self.previous_error = 0.0

    def reset(self) -> None:
        self.previous_error = 0.0

    def compute_control(self, reference: float, measurement: float) -> float:
        error = reference - measurement
        action = self.kp * error + self.kd * (error - self.previous_error)
        self.previous_error = error
        return cls(action)