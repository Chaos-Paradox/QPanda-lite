# import warnings

# try:
#     # QPandaLitePy extension is implemented by C++
#     from QPandaLitePy import *
# except ImportError as e:
#     # Note: Without compiling the QPandaLiteCpp, you can also use qpandalite.
#     # Only the C++ simulator is disabled.
#     warnings.warn('qpandalite is not install with QPandaLiteCpp.')

from .originir_simulator import OriginIR_Simulator