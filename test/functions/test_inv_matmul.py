from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import torch
import unittest
from torch.autograd import Variable
from gpytorch.lazy import NonLazyVariable
from gpytorch.utils import approx_equal


class TestInvMatmulNonBatch(unittest.TestCase):
    def setUp(self):
        mat = torch.Tensor([[3, -1, 0], [-1, 3, 0], [0, 0, 3]])
        vec = torch.randn(3)
        vecs = torch.randn(3, 4)

        self.mat_var = Variable(mat, requires_grad=True)
        self.mat_var_clone = Variable(mat, requires_grad=True)
        self.vec_var = Variable(vec, requires_grad=True)
        self.vec_var_clone = Variable(vec, requires_grad=True)
        self.vecs_var = Variable(vecs, requires_grad=True)
        self.vecs_var_clone = Variable(vecs, requires_grad=True)

    def test_inv_matmul_vec(self):
        # Forward
        res = NonLazyVariable(self.mat_var).inv_matmul(self.vec_var)
        actual = self.mat_var_clone.inverse().matmul(self.vec_var_clone)
        self.assertTrue(approx_equal(res, actual))

        # Backward
        grad_output = torch.randn(3)
        res.backward(gradient=grad_output)
        actual.backward(gradient=grad_output)
        self.assertTrue(approx_equal(self.mat_var_clone.grad.data, self.mat_var.grad.data))
        self.assertTrue(approx_equal(self.vec_var_clone.grad.data, self.vec_var.grad.data))

    def test_inv_matmul_multiple_vecs(self):
        # Forward
        res = NonLazyVariable(self.mat_var).inv_matmul(self.vecs_var)
        actual = self.mat_var_clone.inverse().matmul(self.vecs_var_clone)
        self.assertTrue(approx_equal(res, actual))

        # Backward
        grad_output = torch.randn(3, 4)
        res.backward(gradient=grad_output)
        actual.backward(gradient=grad_output)
        self.assertTrue(approx_equal(self.mat_var_clone.grad.data, self.mat_var.grad.data))
        self.assertTrue(approx_equal(self.vecs_var_clone.grad.data, self.vecs_var.grad.data))


class TestInvMatmulBatch(unittest.TestCase):
    def setUp(self):
        mats = torch.Tensor([[[3, -1, 0], [-1, 3, 0], [0, 0, 3]], [[10, -2, 1], [-2, 10, 0], [1, 0, 10]]])
        vecs = torch.randn(2, 3, 4)

        self.mats_var = Variable(mats, requires_grad=True)
        self.mats_var_clone = Variable(mats, requires_grad=True)
        self.vecs_var = Variable(vecs, requires_grad=True)
        self.vecs_var_clone = Variable(vecs, requires_grad=True)

    def test_inv_matmul_multiple_vecs(self):
        # Forward
        res = NonLazyVariable(self.mats_var).inv_matmul(self.vecs_var)
        actual = torch.cat(
            [self.mats_var_clone[0].inverse().unsqueeze(0), self.mats_var_clone[1].inverse().unsqueeze(0)]
        ).matmul(self.vecs_var_clone)
        self.assertTrue(approx_equal(res, actual))

        # Backward
        grad_output = torch.randn(2, 3, 4)
        res.backward(gradient=grad_output)
        actual.backward(gradient=grad_output)
        self.assertTrue(approx_equal(self.mats_var_clone.grad.data, self.mats_var.grad.data))
        self.assertTrue(approx_equal(self.vecs_var_clone.grad.data, self.vecs_var.grad.data))


if __name__ == "__main__":
    unittest.main()
