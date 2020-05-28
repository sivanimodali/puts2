import unittest
import main


class TestCalculator(unittest.TestCase):#unittest module provides a set of tools for constructing and running scripts, we will test features of online calculator in this case
	
	def setUp(self):#setUp , when unittest module is used and it enables application to test
		main.app.testing = True
		self.app = main.app.test_client()

	def test_mul1(self):
		#case 1, A is n integer B is an integer
		solution = self.app.get('/mul?A=25&B=2')
		self.assertEqual(b'50.0', solution.data)

	def test_mul2(self):

		#case 2, A is rational number and B is rational number p/q form
		solution = self.app.get('/mul?A=5/4&B=12/5')
		self.assertEqual(b'3.00', solution.data)

	def test_mul3(self):

		#case 3, A is a float and B is a float
		solution = self.app.get('/mul?A=6.4&B=100.2')
		self.assertEqual(b'641.28', solution.data)

	def test_mul4(self):

		#case 4, when A is float and B is integer
		solution = self.app.get('/mul?A=7.6&B=43')
		self.assertEqual(b'326.8', solution.data)

	def test_mul5(self):

		#case 5, when A is integer and B is float
		solution = self.app.get('/mul?A=30&B=2.2')
		self.assertEqual(b'66', solution.data)

	def test_mul6(self):

		#case 6, when A is fraction p/q and B is an integer
		solution = self.app.get('/mul?A=2/3&B=55')
		self.assertEqual(b'36.66', solution.data)

	def test_mul7(self):

		#case 7, when A is an integer and B is a fraction p/q
		solution = self.app.get('/mul?A=19&B=5/14')
		self.assertEqual(b'6.7857', solution.data)

	def test_mul8(self):

		#case 8, when A input is an alphabet(non integer) and B is integer
		solution = self.app.get('/mul?A=sivani&B=12')
		self.assertEqual(b'0.0', solution.data)#non integer type considered as not valid , in this case which is zero

	def test_mul9(self):

		#case 9, when A input is an integer and B input is an alphabet
		solution = self.app.get('/mul?A=12&B=modali')
		self.assertEqual(b'0.0', solution.data)
		#when one input is alphabet and other input be any number, whether rational , integer, fraction ultimately the result will be the input which was an integer

	def test_mul10(self):

		#case 10, when A input is of the form p/q where q=0 and B input be any number
		solution = self.app.get('mul?A=8/0&B=2')
		self.assertEqual(b"None", solution.data)
		#according to the script if q=0 in p/q form then it should display an error but it is resolved using zerodivision module

	def test_mul11(self):

		#case 11, when A input is any number and B=p/q form where q=0
		solution = self.app.get('mul?A=14&B=6/0')
		self.assertEqual(b"None", solution.data)

if __name__ == '__main__':
	unittest.main()
