import numpy as np


def u(theta_, phi_, lambda_):
    theta_ = theta_ % (2*np.pi)
    lambda_ = lambda_ % (2*np.pi)

    return np.array([
        [
            np.cos(theta_/2),
            -np.e**(1j*lambda_) * np.sin(theta_/2)
        ],
        [
            np.e**(1j * phi_) * np.sin(theta_/2),
            np.e**(1j * (phi_+lambda_)) * np.cos(theta_/2)
        ]
    ])


def hadamard(qubit):
    arr = u(np.pi/2, 0, np.pi)
    print(arr)
    return np.dot(qubit, arr)


identity = np.array([[1, 0], [0, 1]])
pauli_x = np.array([[0, 1], [1, 0]])
pauli_y = np.array([[0, -1j], [1j, 0]])
pauli_z = np.array([[1, 0], [0, -1]])


def ctrl(qubit, ctrl):
    pass


state = np.array([1, 0], dtype='complex128')
# print(state, state.dtype)
print(hadamard(state), state.dtype)
# print(state3 := hadamard(state2), state3.dtype)
