#encoding: utf-8

from cocos.sprite import *
from cocos.director import director
from cocos.layer import Layer
from cocos.scene import Scene
from cocos.scenes.transitions import *
from cocos.actions import *
from cocos.sprite import *
from cocos.menu import *
from cocos.text import *
from pyglet import font

from pyglet.window import key

import os

class Presentation(Scene):

    def __init__(self):
        super(Presentation, self).__init__()

        self.img = pyglet.resource.image('media/imgs/background.png')

    def draw(self):
        glPushMatrix()
        self.transform()
        self.img.blit(0,0)
        glPopMatrix()

class Intra(Layer):

    def __init__(self):
        super(Intra, self).__init__()

        label = Label('''Desenvolvimento de Jogos''',
                font_name = 'happy sans',
                font_size=46,
                anchor_x='center',anchor_y='center',
                color=(0, 0, 0, 255)
                )
        label.position = 1024/2, (728+70)/2
        self.add(label)

        label = Label('''com Python e Cocos2d''',
                font_name = 'happy sans',
                font_size=46,
                anchor_x='center',anchor_y='center',
                color=(0, 0, 0, 255)
                )
        label.position = 1024/2, (728-30)/2
        self.add(label)

        label = Label('''Software Freedom Day 2010 @ Campina Grande''',
                font_name = 'mandingo',
                font_size=16,
                anchor_x='center',anchor_y='center',
                color=(0, 0, 0, 255)
                )
        label.position = 700, 30
        self.add(label)

class TextSlide(Layer):

    def __init__(self, title, *lines):
        super(TextSlide, self).__init__()

        self.title = title

        label = Label(self.title, font_name = 'super mario bros.', font_size=60,\
                        anchor_x='center', anchor_y='center', color=(0,0,0, 255) )
        label.position = 750, 650
        self.add(label)

        pos = 550

        for line in lines:
            label = Label(line, font_name = 'happy sans', font_size=24,color=(0,0,0, 255))
            label.position = 100, pos
            self.add(label)
            pos-=45


if __name__ == "__main__":
    font_path = os.path.join( os.path.dirname(__file__), 'media/fonts')
    font.add_directory(font_path)
    director.init(resizable=True, width=1024, height=728, fullscreen=False) #false por enquanto
    scene = Scene(Presentation())


    scene.add(TextSlide( \
        u'About me',
        u'- Flávio Ribeiro',
        u'- COBRATEAM Developer (http://cobrateam.info)',
        u'- Engenheiro de Software @ Avaty! Tecnologia (http://avaty.com.br)',
        u'- Engenharia Eletrica @ IFPB (http://ifpb.edu.br)',
        u'- GSoC2010 @ BlueZ (http://bluez.org)',
        u'- twitter.com/flavioribeiro',
        ), z=1)
    director.run(scene)
