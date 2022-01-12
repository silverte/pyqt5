# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import cv2

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    test_camera01 = cv2.VideoCapture(0)
    test_camera01.set(cv2.CAP_PROP_FRAME_WIDTH, 1000)
    test_camera01.set(cv2.CAP_PROP_FRAME_HEIGHT, 500)

    while cv2.waitKey(50) < 0:
        a, b = test_camera01.read()
        cv2.imshow("Test_Camera out", b)

    test_camera01.release()
    cv2.destroyAllWindows()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
