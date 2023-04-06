import numpy as np

class Course:
    magnitude: float = 0.0
    angle: float = 0.0
    x: float = 0.0
    y: float = 0.0
                
    @classmethod
    def convert_xy_to_angle(cls, x: int, y: int):
        vector = np.array([x, y])
        return  np.degrees(np.arctan2(vector[0], vector[1]))
        
    def convert_angle_and_mag_to_xy(cls, angle: float, magnitude: float):
        angle = 90 - angle;
        angle = np.deg2rad(angle)
        
        x = np.cos(angle) 
        #print(f"COS: {x}")
        
        y = np.sin(angle)
        #print(f"SIN: {y}")
        
        return [x* magnitude, y* magnitude]
    
    @classmethod    
    def convert_xy_to_magnitude(cls, x: int, y: int):
        return np.math.sqrt(x*x + y*y)
        
    @classmethod
    def course_from_coords(cls, x: int, y: int):
        magnitude = np.round(Course.convert_xy_to_magnitude(x, y), 5)
        angle = Course.convert_xy_to_angle(x, y)
        
        return Course(angle = angle, magnitude=magnitude)
            
    def __init__(self, angle: float, magnitude:float):
            self.angle = angle;
            self.magnitude = magnitude;
            coords = Course.convert_angle_and_mag_to_xy(None, angle=angle, magnitude=magnitude);
            
            #print(f"Coords :{coords}")
            
            self.x = np.round(coords[0], 5);
            self.y = np.round(coords[1], 5);
            
    def correct(self, magnitude: float):
        # corrected Course has a zero angle by definition
        # therefore, all we need is the magnitude
        # this method will produce the Course addend that will produce the corrected Course
        correct = Course(angle=0, magnitude=magnitude);
        
        # simple vector subtract
        adjust = np.subtract([correct.x, correct.y], [self.x, self.y]);
        
        return Course.course_from_coords(adjust[0], adjust[1])
        
    def __str__(self):
        return f"magnitude: {self.magnitude}\nangle: {format(self.angle, '.2f')}\nx: {self.x}\ny: {self.y}"