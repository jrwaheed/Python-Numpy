import numpy as np
import UsefulTools as ut


def main():
    """
    These two function run with different implementations
    and times how long each one takes to run. Testing speed of numpy vs normal python.


    The great thing about numpy is that it's memory efficient when using
    vectorization. Allows you to loop over a large array at once.
    """

    @ut.timer
    def numpy_func():
        np.arange(1000000)

    @ut.timer
    def normal_func():
        list(range(1000000))

    # Run the functions
    numpy_func()
    normal_func()

    data = np.array([[1.5, -0.1, 3], [0, -3, 6.5]], dtype=np.float64)
    print(1/data)

    data = np.arange(10)
    data[:] = 11  # Bare assignment

    print(data)

    print(np.zeros((3, 6)))

    data = np.array([[1.5, -0.1, 3], [0, -3, 6.5]])

    dummy_data = np.arange(10)

    dummy_data.astype(float)

    print(dummy_data * dummy_data)


if __name__ == "__main__":
    main()
