import kivy
from kivy.app import App
from kivy.uix.scatter import ScatterPlane
from kivy.uix.image import Image
from os.path import join
from kivy.uix.floatlayout import FloatLayout
#from kivy.uix.gridlayout import GridLayout


class LabelMipmapTest(App):
    def build(self):
        self.window = FloatLayout()
        self.window.cols = 1
        background = Image(source="src/background.png",pos=(1,1),size=(2000,1000))
        self.window.add_widget(background )
        Film = ScatterPlane(scale=0.2,opacity=0.9)
        film_top = Image(source='src/film_top.png', pos=(0, 400), size=(756, 600))
        Film.add_widget(film_top )
        pictrue_list=["x (1).jpg","x (2).jpg"]
        y=0 #额外两张照片间隔
        for x in pictrue_list:
            film_down= Image(source='src/film.png', pos=(756+y, 400), size=(756, 600)) 
            Pictrue = Image(source=x, pos=(756+y, 460), size=(720,480 ))
            Film.add_widget(film_down)
            Film.add_widget(Pictrue)
            y = y+756    #额外两张照片间隔
        self.window.add_widget(Film)
        return self.window


if __name__ == '__main__':
    LabelMipmapTest().run()
