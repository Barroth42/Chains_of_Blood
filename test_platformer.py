import unittest

from platformer import half_width, half_height, game_display, load_music

class Test_Half_Width(unittest.TestCase):	
	def test_half_width(self):
		"""Is number being halved"""
		self.assertEqual(half_width(800),400)
		
class Test_Half_Height(unittest.TestCase):	
	def test_half_height(self):
		"""Is number being halved"""
		self.assertEqual(half_height(800),400)
		
class Test_Game_Display(unittest.TestCase):	
	def test_game_display(self):
		"""Are numbers coming out correctly"""
		self.assertGreaterEqual(game_display(100,100),(100,100))
		
class Test_Music(unittest.TestCase):
	def test_load_music(self):
		"""Is the correct music name being input and being found in directory"""
		"""If not found in directory will produce error"""
		self.assertEqual(load_music("Intro.wav"),None)

if __name__ == '__main__':
    unittest.main()
