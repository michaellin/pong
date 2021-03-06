import unittest

import config
import moving


class Detector:
    def __init__(self):
        minX = 0
        minY = 0
        maxX = minX + config.BOARD_WIDTH
        maxY = minY + config.BOARD_HEIGHT
        self.bounds = (minX, minY, maxX, maxY)

    def checkCollision(self, coordsA, coordsB):
        if coordsA[0] >= coordsB[2]:
            return False
        if coordsA[2] <= coordsB[0]:
            return False
        if coordsA[1] >= coordsB[3]:
            return False
        if coordsA[3] <= coordsB[1]:
            return False
        return True

    def checkBounds(self, coords):
        if coords[0] < self.bounds[0]:
            return 'left'
        elif coords[1] < self.bounds[1]:
            return 'top'
        elif coords[2] > self.bounds[2]:
            return 'right'
        elif coords[3] > self.bounds[3]:
            return 'bottom'
        else:
            return False

class DetectorTests(unittest.TestCase):
    def setUp(self):
        self.minX = 0
        self.minY = 0
        self.maxX = self.minX + config.BOARD_WIDTH
        self.maxY = self.minY + config.BOARD_HEIGHT
        
        self.detector = Detector()

    def testBallDoesntCollideWithWall(self):
        inCoords = (
            (0, 0, 10, 10),
            (self.maxX - 10, self.maxY - 10,
             self.maxX, self.maxY),
            (self.maxX - 10, 0, self.maxX, 10),
            (0, self.maxY - 10, 10, self.maxY))
        for coords in inCoords:
            self.assertFalse(self.detector.checkBounds(coords))
    
    def testBallCollidesWithWall(self):
        outCoords = (
            (-1, 20, 9, 30),
            (40, -1, 50, 9),
            (-1000, -1000, -990, -990),
            (1000, 1000, 1010, 1010),
            (self.maxX - 9, self.maxY - 9,
             self.maxX + 1, self.maxY + 1)
            )
        for coords in outCoords:
            self.assertTrue(self.detector.checkBounds(coords))

    def testObjectsCollide(self):
        objects = (
            ((10, 10, 20, 20), (19, 19, 29, 29)),
            ((100, 100, 110, 110), (90, 90, 101, 110)),
            ((10, 10, 1000, 1000), (50, 50, 60, 60))
            )
        for object in objects:
            self.assertTrue(self.detector.checkCollision(object[0], object[1]))

    def testObjectsDontCollide(self):
        objects = (
            ((10, 10, 20, 20), (21, 10, 31, 20)),
            ((50, 100, 60, 200), (100, 100, 110, 200))
            )
        for object in objects:
            self.assertFalse(self.detector.checkCollision(object[0], object[1]))


if __name__ == '__main__':
    unittest.main()
