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

    is_event_handler = True

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

    def on_key_press(self, _key, modifiers):
        if _key == key.LEFT:
            SlidesManager.previous()
        elif _key == key.RIGHT:
            SlidesManager.next()


class TextSlide(Layer):

    is_event_handler = True

    def __init__(self, title, *lines):
        super(TextSlide, self).__init__()

        label = Label(title, font_name = 'super mario bros.', font_size=60, color=(0,0,0, 255) )
        label.position = 350, 640
        self.add(label)

        pos = 550

        for line in lines:
            label = Label(line, font_name = 'happy sans', font_size=24,color=(0,0,0, 255))
            label.position = 100, pos
            self.add(label)
            pos-=45

    def on_key_press(self, _key, modifiers):
        if _key == key.LEFT:
            SlidesManager.previous()
        elif _key == key.RIGHT:
            SlidesManager.next()

class ImageSlide(Layer):

    is_event_handler = True

    def __init__(self, title, line, image=None):
        super(ImageSlide, self).__init__()

        label = Label(title, font_name = 'super mario bros.', font_size=60, color=(0,0,0, 255) )
        label.position = 350, 640
        self.add(label)

        label = Label(line, font_name = 'mandingo', font_size=20, color=(0,0,0, 255) )
        label.position = 60, 580
        self.add(label)

        self.img = Sprite(image)
        self.img.position = 550, 350
        self.add(self.img)

    def on_key_press(self, _key, modifiers):
        if _key == key.LEFT:
            SlidesManager.previous()
        elif _key == key.RIGHT:
            SlidesManager.next()


class SlidesManager(object):

    def build_slides(self):
        self.__class__.slides_pool = [
            TextSlide(
                u'About me',
                u'- Flávio Ribeiro',
                u'- COBRATEAM Developer (http://cobrateam.info)',
                u'- Engenheiro de Software @ Avaty! Tecnologia (http://avaty.com.br)',
                u'- Engenharia Eletrica @ IFPB (http://ifpb.edu.br)',
                u'- GSoC2010 @ BlueZ (http://bluez.org)',
                u'- twitter.com/flavioribeiro'),

            TextSlide(
                u'Roteiro',
                u'- O que me levou a fazer essa palestra...',
                u'- Conceitos do desenvolvimento de games',
                u'- Python e seus frameworks de games',
                u'- Cocos2d',
                u'- Demos'),

            TextSlide(
                u'Por que?',
                u'- Python é adotada pro ensino da programação da UFCG',
                u'- O projeto final de alguns alunos é um game',
                u'- Fazer jogos é tão divertido quanto fazer robôs',
                u'- Apresentar um pouco do que aprendi na PyWeek',
                u'- Falar algo diferente de embarcados e marmota.mobi'
                ),

            TextSlide(
                u'Game Concepts',
                u'- ae',
                ),


            ImageSlide(
                u'Ex de Imagem',
                u'- Esse sou eu!',
                image="media/imgs/me.png"),

        ]

        self.__class__.current_position = 0
 
    @staticmethod
    def next():
        if SlidesManager.current_position+1 > len(SlidesManager.slides_pool):
            return

        scene = Scene(Presentation())
        scene.add(SlidesManager.slides_pool[SlidesManager.current_position], z=1)
        SlidesManager.current_position+=1
        director.push(scene)

    @staticmethod
    def previous():
        if SlidesManager.current_position == 0 or \
            SlidesManager.current_position-1 > len(SlidesManager.slides_pool):

            return

        SlidesManager.current_position-=1
        scene = Scene(Presentation())
        scene.add(SlidesManager.slides_pool[SlidesManager.current_position], z=1)
        director.push(scene)



if __name__ == "__main__":
    director.init(resizable=True, width=1024, height=728, fullscreen=False) 
    font_path = os.path.join( os.path.dirname(__file__), 'media/fonts')
    font.add_directory(font_path)

    slides_manager = SlidesManager()
    slides_manager.build_slides()

    scene = Scene(Presentation())
    scene.add(Intra(), z=1)
    director.run(scene)
