import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestMyFunction(unittest.TestCase):

    def test_my_function(self):

        result = emotion_detector("I am glad this happened")['dominant_emotion']
        self.assertEqual(result, "joy")

        result = emotion_detector("I am really mad about this")['dominant_emotion']
        self.assertEqual(result, "anger")

        result = emotion_detector("I feel disgusted just hearing about this")['dominant_emotion']
        self.assertEqual(result, "disgust")

        result = emotion_detector("I am so sad about this")['dominant_emotion']
        self.assertEqual(result, "sadness")

        result = emotion_detector("I am really afraid that this will happen")['dominant_emotion']
        self.assertEqual(result, "fear")
unittest.main()