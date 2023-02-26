__author__ = 'bunkus'
from kivy.app import App
#from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture
from kivy.uix.button import Button
#from kivy.lang import Builder
import cv2
import time


class CamApp(App):
    def build(self):
        layout = BoxLayout()
        # Add a button to capture images
        capture_btn = Button(size=(100, 200))
        layout.add_widget(capture_btn)
        capture_btn.bind(on_press=self.capture_image)
        # Add an image widget that will show the image we take
        self.img1 = Image()
        layout.add_widget(self.img1)
        # Create a VideoCapture object
        self.capture = cv2.VideoCapture(0)
        # Make the video show in the image widget
        Clock.schedule_interval(self.update, 1.0/33.0)
        return layout

    def update(self, dt):
        # display image from cam in opencv window
        ret, frame = self.capture.read()
        buf1 = cv2.flip(frame, 0)
        buf = buf1.tostring()
        texture1 = Texture.create(
            size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
        texture1.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
        # display image from the texture
        self.img1.texture = texture1

    def capture_image(self, obj):
        # save image to a file
        ret, frame = self.capture.read()
        timestr = time.strftime("%Y%m%d_%H%M%S")
        cv2.imwrite("gallery/Film_{}.jpg".format(timestr), frame)


if __name__ == '__main__':
    CamApp().run()
    cv2.destroyAllWindows()
