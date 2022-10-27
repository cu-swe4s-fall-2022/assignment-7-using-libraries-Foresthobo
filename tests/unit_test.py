import numpy as np
import sys
import os
import unittest
import shutil
import random
src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
sys.path.append(src_path)
import data_processor #nopep8

class MyTestCase(unittest.TestCase):
    
    
    def test_random_matrix(self):
        N = 10
        M = 10
        Mat = data_processor.get_random_matrix(N,M)
        self.assertEqual(np.shape(Mat), (N,M))
        R = np.random.randint(0,N)
        self.assertIsNotNone(Mat[R][0])
        
        self.assertNotEqual(Mat[0][0], Mat[0][1], Mat[0][2])
        
        self.assertIsNone(data_processor.get_random_matrix(0,0))
    
    
    def setUp(self):
        
        self.test_file_name = 'setup_test_file.txt'
        
        f = open(self.test_file_name, 'w')
        for i in range(4):
            f.write('1, 2, 3, 4, 5 \n')
        f.close()
        
        self.test_file_name_0 = 'setup_test_file_0.txt'
        
        f = open(self.test_file_name_0, 'w')
        f.close()

    def tearDown(self):
        os.remove(self.test_file_name)
        os.remove(self.test_file_name_0)
    
    def test_file_read(self):
        
        dim = data_processor.get_file_dimensions(self.test_file_name)
        self.assertEqual(dim, (4,5))
        
        dim2 = data_processor.get_file_dimensions(self.test_file_name_0)
        self.assertEqual(dim2, (0,))
        
        dimIris = data_processor.get_file_dimensions('../iris.data')
        self.assertEqual(dimIris, (150, 5))
    
    def test_matrix_to_file(self):
        data = data_processor.write_matrix_to_file(5, 5, 'test.csv')
        
        dim = data_processor.get_file_dimensions('test.csv')
        self.assertEqual(dim, (5, 5))
        os.remove('test.csv')