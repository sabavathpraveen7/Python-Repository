class PID:
    def __init__(self, Kp, Ki, Kd):
        self.Kp, self.Ki, self.Kd = Kp, Ki, Kd
        self.prev_error = 0
        self.integral = 0

    def update(self, setpoint, current_value):
        error = setpoint - current_value
        self.integral += error
        derivative = error - self.prev_error
        
        output = (self.Kp * error) + (self.Ki * self.integral) + (self.Kd * derivative)
        self.prev_error = error
        return output

# Simulate a drone trying to reach 10 meters altitude
drone_pid = PID(Kp=0.5, Ki=0.01, Kd=0.1)
current_alt = 0
target_alt = 10

for i in range(20):
    adjustment = drone_pid.update(target_alt, current_alt)
    current_alt += adjustment
    print(f"Time {i}: Altitude = {current_alt:.2f}m")