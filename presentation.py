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
from random import choice

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

            ImageSlide(
                u'Conceitos',
                u'- Surface',
                image="media/imgs/surface.png"
                ),

            ImageSlide(
                u'Conceitos',
                u'- Sprite',
                image="media/imgs/sprite1.png"
                ),


            ImageSlide(
                u'Conceitos',
                u'- Sprite',
                image="media/imgs/sprite2.png"
                ),

            ImageSlide(
                u'Conceitos',
                u'- Rect (Retângulo)',
                image="media/imgs/rect1.png"
                ),

            ImageSlide(
                u'Conceitos',
                u'- Rect (Retângulo)',
                image="media/imgs/rect2.png"
                ),

            ImageSlide(
                u'Conceitos',
                u'- Rect (Retângulo)',
                image="media/imgs/rect3.png"
                ),
 
            ImageSlide(
                u'Conceitos',
                u'- Colisão',
                image="media/imgs/colisao1.png"
                ),

            ImageSlide(
                u'Conceitos',
                u'- Colisão',
                image="media/imgs/colisao2.png"
                ),


           TextSlide(
                u'Conceitos',
                u'- GameLoop',
                u'-- Batimento cardíaco do jogo'
            ),
 
            TextSlide(
                u'Conceitos',
                u'- GameLoop',
                u'-- while jogo_rodando:',
                u'--    atualizar_jogo()',
                u'--    desenhar_jogo()',
                u'',
                u'- Não controla o tempo.',
                u'- Hardware diferente == velocidade diferente',
                ),
 
            TextSlide(
                u'Conceitos',
                u'- GameLoop',
                u'-- Baseado em FPS (Frames por segundo)',
                u'-- Fixa a atualização do jogo em x vezes por segundo',
                u'-- Fixa também o jogo em uma unidade de medida "universal" (segundos)',
                ),


           TextSlide(
                u'Python',
                u'- Fácil de aprender',
                u'- Baterias inclusas',
                u'- Gerencia de tipos e coleções excelente',
                u'- Multiplataforma (Linux, Windows, Mac, Celulares)',
                u'- Divertida :-)',
                u'- Tem várias API\'s pra jogos'
                ),

           TextSlide(
                u'Python',
                u'- Pygame',
                u'- Pyglet',
                u'- Cocos2d',
                u'- Panda3D',
                u'- PyOgre, Soya3d, etc...'
                ),

 
           TextSlide(
                u'Python',
                u'- Quem utiliza Python pra Games?',
                ),
        
         ImageSlide(
                u'Python',
                u'Frets on Fire',
                image='media/imgs/fretsonfire.png'
                ),


         ImageSlide(
                u'Python',
                u'Civilization',
                image='media/imgs/civilization.png'
                ),



         ImageSlide(
                u'Python',
                u'InterZone',
                image='media/imgs/interzone.png'
                ),

          TextSlide(
                u'Pygame',
                u'- Mais popular',
                u'- SDL (Simple DirectMedia Layer)',
                u'- Implementa colisões, dirty rect, etc',
                u'- GameLoop Based',
                u'- Modular',
                u'- Otimizado',
                ),

   TextSlide(
                u'Cocos2d',
                u'- Curva de aprendizado baixa',
                u'- Não baseada em GameLoop',
                u'- Actions',
                u'- Scenes',
                u'- Director',
                u'- Transitions',
                u'- **Cocos2d for iPhone**'
                ),

   TextSlide(
                u'Obrigado!',
                u'- Palestra disponivel em:',
                u'http://github.com/flavioribeiro/softwarefreedomdaycg'
                ),



   TextSlide(
                u'Referências',
                u'- http://cocos2d.org'
                u'- http://www.slideshare.net/andrewsmedina/',
                u'- http://www.slideshare.net/r1chardj0n3s/',
                ),
        ]

        self.__class__.current_position = 0
 
    @staticmethod
    def next():
        if SlidesManager.current_position+1 > len(SlidesManager.slides_pool):
            return

        scene = Scene(Presentation())
        scene.add(SlidesManager.slides_pool[SlidesManager.current_position], z=1)
        SlidesManager.current_position+=1
       
        trans = [ FadeTRTransition, FlipX3DTransition, CornerMoveTransition, ShuffleTransition, FlipY3DTransition, EnvelopeTransition, ZoomTransition ]
        t = choice(trans)
        director.replace( t(scene, duration=1))

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
