
#GFOLD��ز���


import numpy as np

# ʱ�䲽��
class SuperParams:
    def __init__(self):
        self.N = 40

# �������ز���
class SolverOptions:
    def __init__(self):
        pass


# ֱ�Ӵ���������Ĳ�������Ӧcvxpy.Parameter��
class Params:
    def __init__(self, N):
        self.x0 = np.zeros((6, 1))
        self.xf = np.zeros((6, 1))
        self.z0_term_inv = np.zeros((1, N))
        self.z0_term_log = np.zeros((1, N))
        self.g = np.zeros((3, 1))
        self.alpha_dt = None
        self.G_max = None
        self.V_max = None
        self.y_gs_cot = None
        self.p_cs_cos = None
        self.m_wet_log = None
        self.r1 = None
        self.r2 = None
        self.tf = None
        


