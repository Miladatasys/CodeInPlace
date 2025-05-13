SPEED = 10.44 # Bolt's speed in meters / second

def main():
    time_str = input("Run time (s): ")
    time = float(time_str)
    distance = SPEED * time
    print(f"Bolt can run {distance} meters.")