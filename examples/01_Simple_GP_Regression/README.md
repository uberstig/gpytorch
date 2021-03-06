# Simple GP Regression

Here are examples for simple GP regression models.
These examples will work for small to medium sized datasets (~2,000 data points).
All examples here use exact GP inference (and therefore assume a Gaussian noise observation model).

For a tutorial on GPyTorch, check out the [simple GP regression notebook](./Simple_GP_Regression.ipynb).


## Contents
- **[Simple_GP_Regression.ipynb](./Simple_GP_Regression.ipynb)**
  - This is the simplist of the notebooks - a GP regression model with an RBF kernel. Start here if you are new to GPyTorch, or new to GPs in general.
- **[Spectral_Mixture_GP_Regression.ipynb](./Spectral_Mixture_GP_Regression.ipynb)**
  - This notebook expands on previous eample with a more complex kernel.
    The [spectral mixture kernel](https://arxiv.org/pdf/1302.4245.pdf) is a great choice if you have a complex extrapolation problem.
- **[Simple_GP_Regression_With_LOVE_Fast_Variances_CUDA.ipynb](./Simple_GP_Regression_With_LOVE_Fast_Variances_CUDA.ipynb)**
  - This notebook demonstrates [LOVE](https://arxiv.org/pdf/1803.06058.pdf), a technique to rapidly speed up predictive variance computaitons.
    Check out this notebook to see how to use LOVE in GPyTorch, and how it compares to standard variance computations.
