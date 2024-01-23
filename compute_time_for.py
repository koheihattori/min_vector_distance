#!/usr/bin/env python
# coding: utf-8

import numpy
import time



def doit_time_for_loop(N_US_per_star=100, K=10000, N_repeat = 100):
    # 100 x 10000
    print('='*20)
    print('N_US_per_star', N_US_per_star)
    print('K', K)
    print('N_repeat', N_repeat)
    print('='*20)
    numpy.random.seed(123)
    
    # A
    x = numpy.random.rand(N_US_per_star) # Jr_i
    y = numpy.random.rand(N_US_per_star) # Jz_i
    z = numpy.random.rand(N_US_per_star) # Jphi_i

    # B
    u = numpy.random.rand(K) # _Jr_c
    v = numpy.random.rand(K) # _Jz_c
    w = numpy.random.rand(K) # _Jphi_c

    N_A = len(x) # N_US_per_star
    N_B = len(u) # K
    
    
    print('[1a] For loop over N_US_per_star')
    start = time.time()
    for i in range(N_repeat):
        d2_min = 1e10
        best_j = 0
        best_k = 0
        for j in range(N_A):
            d2 = (x[j]-u)**2 + (y[j]-v)**2 + (z[j]-w)**2
            tmp_argmin_d2 = numpy.argmin(d2)
            tmp_d2_min    = d2[tmp_argmin_d2]
            if (tmp_d2_min<d2_min):
                d2_min = tmp_d2_min
                best_j = j
                best_k = tmp_argmin_d2
        
    print(d2_min, best_j, best_k)
    end = time.time()
    print('# required time = %lf' % (end-start), 'sec (Repeated for %d times.)'% (N_repeat))
    print('-'*20)
    
    
        
    print('[1b] For loop over K')
    start = time.time()
    for i in range(N_repeat):
        d2_min = 1e10
        best_j = 0
        best_k = 0
        for k in range(N_B):
            d2 = (x-u[k])**2 + (y-v[k])**2 + (z-w[k])**2
            tmp_argmin_d2 = numpy.argmin(d2)
            tmp_d2_min    = d2[tmp_argmin_d2]
            if (tmp_d2_min<d2_min):
                d2_min = tmp_d2_min
                best_j = tmp_argmin_d2
                best_k = k
        
    print(d2_min, best_j, best_k)
    end = time.time()
    print('# required time = %lf' % (end-start), 'sec (Repeated for %d times.)'% (N_repeat))
    print('-'*20)
    return None

def doit_time(N_US_per_star=100, K=10000, N_repeat = 100):
    # 100 x 10000
    print('='*20)
    print('N_US_per_star', N_US_per_star)
    print('K', K)
    print('N_repeat', N_repeat)
    print('='*20)
    numpy.random.seed(123)

    
    # A
    x = numpy.random.rand(N_US_per_star) # Jr_i
    y = numpy.random.rand(N_US_per_star) # Jz_i
    z = numpy.random.rand(N_US_per_star) # Jphi_i

    # B
    u = numpy.random.rand(K) # _Jr_c
    v = numpy.random.rand(K) # _Jz_c
    w = numpy.random.rand(K) # _Jphi_c

    N_A = len(x) # N_US_per_star
    N_B = len(u) # K
    
    
    print('[1] Construction of matrix_A and matrix_B')
    start = time.time()
    for i in range(N_repeat):
        matrix_A = numpy.vstack([x, y, z])
        matrix_B = numpy.vstack([u, v, w])
    end = time.time()
    print('# required time = %lf' % (end-start), 'sec (Repeated for %d times.)'% (N_repeat))
    print('-'*20)
    
        
    print('[2] Construction of matrix_A_T__xNB and matrix_B__xNA_T')
    start = time.time()
    for i in range(N_repeat):
        matrix_A_T__xNB = numpy.tile(matrix_A.T, N_B).reshape(N_A*N_B,3)
        matrix_B__xNA_T = numpy.tile(matrix_B, N_A).T
    end = time.time()
    print('# required time = %lf' % (end-start), 'sec (Repeated for %d times.)' % (N_repeat))
    print('-'*20)

    
    print('[3] Construction of diff_AB_2')
    start = time.time()
    for i in range(N_repeat):
        diff_AB_2 = (matrix_A_T__xNB - matrix_B__xNA_T)**2
    end = time.time()
    print('# required time = %lf' % (end-start), 'sec (Repeated for %d times.)' % (N_repeat))
    print('-'*20)
    
        
    print('[4] Getting dmin2_AB')
    start = time.time()
    for i in range(N_repeat):
        #dmin_AB = numpy.sqrt(numpy.min(numpy.sum(diff_AB_2, axis=1)))
        d2_AB =              numpy.sum(diff_AB_2, axis=1)
        dmin2_AB = numpy.min(d2_AB)
    end = time.time()
    print('# required time = %lf' % (end-start), 'sec (Repeated for %d times.)' % (N_repeat))
    print('-'*20)
        
        
    print('[5] Getting best (j,k) using pre-computed d2_AB')
    start = time.time()
    for i in range(N_repeat):
            #argmin_diff_AB_2 = dmin2_AB #numpy.argmin(numpy.sum(diff_AB_2, axis=1))
            argmin_diff_AB_2 = numpy.argmin(d2_AB)
            best_j_for_a_given_star = int(argmin_diff_AB_2 / N_B)
            best_k_for_a_given_star =    (argmin_diff_AB_2 % N_B)
    end = time.time()
    print('# required time = %lf' % (end-start), 'sec (Repeated for %d times.)' % (N_repeat))
    print('-'*20)
    
    print(dmin2_AB, best_j_for_a_given_star, best_k_for_a_given_star)

    
doit_time_for_loop()

    
doit_time()

