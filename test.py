from unittest import TestCase, main
from zerosend import zeros_end

class ZerosFirstTestCase(TestCase):
    def test_1_given(self):
        self.assertEqual(zeros_end([0, 1, 0, 3, 12]), [1, 3, 12, 0, 0] )

    def test_2_given(self):
        self.assertEqual(zeros_end([1, 7, 0, 0, 8, 0, 10, 12, 0, 4]), [1, 7, 8, 10, 12, 4, 0, 0, 0, 0])
    def test_3_emtpy(self):
        self.assertFalse(zeros_end([]))

    def test_4_mirror(self):
        self.assertEqual(zeros_end([1, 2, 3, 0, 0, 0, 3, 2, 1]), [1, 2, 3, 3, 2, 1, 0, 0, 0])
    
    def test_5_all_zeros(self):
        self.assertEqual(zeros_end([0, 0, 0, 0, 0, 0, 0, 0, 0]), [0, 0, 0, 0, 0, 0, 0, 0, 0])
    
    def test_6_no_zeros(self):
        self.assertEqual(zeros_end([1, 1, 3, 9, 11, 1, 5, 8, 7]), [1, 1, 3, 9, 11, 1, 5, 8, 7])

    def test_7_one_zero(self):
        self.assertEqual(zeros_end([0]), [0])
    
    def test_8_one_elem(self):
        self.assertEqual(zeros_end([8]), [8])

if __name__=="__main__":
    main()


