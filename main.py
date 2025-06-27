import numpy as np
import UsefulTools as ut


def main():
    """
    These two function run with different implementations
    and times how long each one takes to run. Testing speed of numpy vs normal python.
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


if __name__ == "__main__":
    main()
