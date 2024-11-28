import py5
import imageio

class EnergyParticle:
    def __init__(self, angle):
        self.angle = angle
        self.radius = py5.random(100, 200)
        self.size = py5.random(10, 20)
        self.speed = py5.random(0.01, 0.05)
        self.color = py5.color(py5.random(100, 255), py5.random(100, 255), py5.random(100, 255))

    def move(self):
        self.angle += self.speed
        if self.angle > py5.TWO_PI:
            self.angle -= py5.TWO_PI

    def display(self):
        x = py5.width / 2 + self.radius * py5.cos(self.angle)
        y = py5.height / 2 + self.radius * py5.sin(self.angle)
        py5.fill(self.color)
        py5.no_stroke()
        py5.ellipse(x, y, self.size, self.size)

particles = []
frames = []  # List to store frames for GIF

def setup():
    py5.size(800, 600)
    py5.background(255)
    for i in range(50):
        angle = py5.random(0, py5.TWO_PI)
        particles.append(EnergyParticle(angle))

def draw():
    py5.background(255)
    
    # Update and display particles
    for particle in particles:
        particle.move()
        particle.display()

    # Capture the frame and append it to the frames list
    img = py5.get(0, 0, py5.width, py5.height)
    frames.append(img)

# Stop the sketch after 360 frames (or one full rotation cycle)
    if py5.frame_count >= 360:
        py5.no_loop()
        py5.exit_sketch()
        save_gif()

def save_gif():
    # Save the collected frames as a GIF
    gif_filename = "energy_particles.gif"
    with imageio.get_writer(gif_filename, mode='I', duration=0.05) as writer:
        for frame in frames:
            writer.append_data(py5.to_image(frame))  # Convert to image format
        print(f"GIF saved as {gif_filename}")

py5.run_sketch()
