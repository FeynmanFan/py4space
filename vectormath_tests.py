import unittest
import course as c

class vectormath_tests(unittest.TestCase):
    def test_course_correction_10faster(self):
        course = c.Course(angle=0, magnitude=100)
        result = course.correct(110)
        
        self.assertEqual(result.x, 0)
        self.assertEqual(result.y, 10)
        
    def test_course_correction_10slower(self):
        course = c.Course(angle=0, magnitude=100)
        result = course.correct(90)
        
        self.assertEqual(result.x, 0)
        self.assertEqual(result.y, -10)
        
    def test_course_correction_heading(self):
        course = c.Course(angle=15, magnitude=100)
        result = course.correct(100)
        
        self.assertEqual(result.x, -25.8819)
        self.assertEqual(result.y, 3.40742)
        
        self.assertEqual(result.angle, -82.49999298734443);
        self.assertEqual(result.magnitude, 26.10523);

if __name__ == '__main__':
    unittest.main()