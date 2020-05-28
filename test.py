
import unittest
import main


class TestCalculator(unittest.TestCase):#unittest module provides a set of tools for constructing and running scripts, we will test features of online calculator in this case
	
	def setUp(self):#setUp , when unittest module is used and it enables application to test
		main.app.testing = True
		self.app = main.app.test_client()
    
    def test_div1(self):
		#case 1, A is n integer B is an integer
		solution = self.app.get('/div?A=30&B=2')
		self.assertEqual(b'15.0', solution.data)

	def test_div2(self):

		#case 2, A is rational number and B is rational number p/q form
		solution = self.app.get('/div?A=3/7&B=61/4')
		self.assertEqual(b'6.5357', solution.data)

	def test_div3(self):

		#case 3, A is a float and B is a float
		solution = self.app.get('/div?A=6.21&B=4.1')
		self.assertEqual(b'1.5146', solution.data)

	def test_div4(self):

		#case 4, when A is float and B is integer
		solution = self.app.get('/div?A=51.33&B=13')
		self.assertEqual(b'3.948461', solution.data)

	def test_div5(self):

		#case 5, when A is integer and B is float
		solution = self.app.get('/div?A=20&B=2.2')
		self.assertEqual(b'9.090909', solution.data)

	def test_div6(self):

		#case 6, when A is fraction p/q and B is an integer
		solution = self.app.get('/div?A=1/2&B=100')
		self.assertEqual(b'50', solution.data)

	def test_div7(self):

		#case 7, when A is an integer and B is a fraction p/q
		solution = self.app.get('/div?A=18&B=2/3')
		self.assertEqual(b'27.0', solution.data)

	def test_div8(self):

		#case 8, when A input is an alphabet(non integer) and B is integer
		solution = self.app.get('/div?A=sivani&B=12')
		self.assertEqual(b'0.0', solution.data)#non integer type considered as not valid , in this case which is zero

	def test_div9(self):

		#case 9, when A input is an integer and B input is an alphabet
		solution = self.app.get('/div?A=52&B=modali')
		self.assertEqual(b'None', solution.data)
		#when one input is alphabet and other input be any number, whether rational , integer, fraction ultimately the result will be the input which was an integer

	def test_div10(self):

		#case 10, when A input is of the form p/q where q=0 and B input be any number
		solution = self.app.get('div?A=6/0&B=2')
		self.assertEqual(b'None', solution.data)
		#according to the script if q=0 in p/q form then it should display an error

	def test_div11(self):

		#case 11, when A input is any number and B=p/q form where q=0
		solution = self.app.get('div?A=17&B=2/0')
		self.assertEqual(b'None', solution.data)


if __name__ == '__main__':
	unittest.main()