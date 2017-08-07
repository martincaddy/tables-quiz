#!/usr/bin/env python
import unicornhat, signal

def zero():
    pixels = [[(0, 0, 0), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 0)], [(0, 0, 0), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 0)], [(0, 0, 0), (0, 0, 255), (0, 0, 255), (0, 0, 0), (0, 0, 0), (0, 0, 255), (0, 0, 255), (0, 0, 0)], [(0, 0, 0), (0, 0, 255), (0, 0, 255), (0, 0, 0), (0, 0, 0), (0, 0, 255), (0, 0, 255), (0, 0, 0)], [(0, 0, 0), (0, 0, 255), (0, 0, 255), (0, 0, 0), (0, 0, 0), (0, 0, 255), (0, 0, 255), (0, 0, 0)], [(0, 0, 0), (0, 0, 255), (0, 0, 255), (0, 0, 0), (0, 0, 0), (0, 0, 255), (0, 0, 255), (0, 0, 0)], [(0, 0, 0), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 0)], [(0, 0, 0), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 0)]]
    unicornhat.set_pixels(pixels)
    unicornhat.show()
    #signal.pause()

def one():
    pixels = [[(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 0)], [(0, 0, 0), (0, 0, 0), (0, 0, 255), (0, 0, 255), (0, 0, 0), (0, 0, 255), (0, 0, 255), (0, 0, 0)], [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 255), (0, 0, 255), (0, 0, 0)], [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 255), (0, 0, 255), (0, 0, 0)], [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 255), (0, 0, 255), (0, 0, 0)], [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 255), (0, 0, 255), (0, 0, 0)], [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 255), (0, 0, 255), (0, 0, 0)], [(0, 0, 0), (0, 0, 0), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255)]]
    unicornhat.set_pixels(pixels)
    unicornhat.show()
    #signal.pause()
    
def two():
    pixels = [[(0, 0, 0), (0, 0, 0), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 0)], [(0, 0, 0), (0, 0, 255), (0, 0, 255), (0, 0, 0), (0, 0, 0), (0, 0, 255), (0, 0, 255), (0, 0, 0)], [(0, 0, 0), (0, 0, 255), (0, 0, 255), (0, 0, 0), (0, 0, 0), (0, 0, 255), (0, 0, 255), (0, 0, 0)], [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 255), (0, 0, 255), (0, 0, 0)], [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 255), (0, 0, 255), (0, 0, 0), (0, 0, 0)], [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 255), (0, 0, 255), (0, 0, 0), (0, 0, 0), (0, 0, 0)], [(0, 0, 0), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)], [(0, 0, 0), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255)]]
    unicornhat.set_pixels(pixels)
    unicornhat.show()
    #signal.pause()
    
def three():
    pixels = [[(0, 0, 0), (0, 0, 0), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 0)], [(0, 0, 0), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255)], [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 255)], [(0, 0, 0), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255)], [(0, 0, 0), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255)], [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 255)], [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 255)], [(0, 0, 0), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255)]]
    unicornhat.set_pixels(pixels)
    unicornhat.show()
    
def four():
    pixels = [[(0, 0, 0), (255, 255, 0), (255, 255, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (255, 255, 0), (255, 255, 0)], [(0, 0, 0), (255, 255, 0), (255, 255, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (255, 255, 0), (255, 255, 0)], [(0, 0, 0), (255, 255, 0), (255, 255, 0), (255, 255, 0), (255, 255, 0), (255, 255, 0), (255, 255, 0), (255, 255, 0)], [(0, 0, 0), (255, 255, 0), (255, 255, 0), (255, 255, 0), (255, 255, 0), (255, 255, 0), (255, 255, 0), (255, 255, 0)], [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (255, 255, 0), (255, 255, 0)], [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (255, 255, 0), (255, 255, 0)], [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (255, 255, 0), (255, 255, 0)], [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (255, 255, 0), (255, 255, 0)]]
    unicornhat.set_pixels(pixels)
    unicornhat.show()
    
def five():
    pixels = [[(255, 255, 0), (255, 255, 0), (255, 255, 0), (255, 255, 0), (255, 255, 0), (255, 255, 0), (255, 255, 0), (255, 255, 0)], [(255, 255, 0), (255, 255, 0), (255, 255, 0), (255, 255, 0), (255, 255, 0), (255, 255, 0), (255, 255, 0), (255, 255, 0)], [(255, 255, 0), (255, 255, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)], [(255, 255, 0), (255, 255, 0), (255, 255, 0), (255, 255, 0), (255, 255, 0), (255, 255, 0), (255, 255, 0), (255, 255, 0)], [(255, 255, 0), (255, 255, 0), (255, 255, 0), (255, 255, 0), (255, 255, 0), (255, 255, 0), (255, 255, 0), (255, 255, 0)], [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (255, 255, 0)], [(255, 255, 0), (255, 255, 0), (255, 255, 0), (255, 255, 0), (255, 255, 0), (255, 255, 0), (255, 255, 0), (255, 255, 0)], [(255, 255, 0), (255, 255, 0), (255, 255, 0), (255, 255, 0), (255, 255, 0), (255, 255, 0), (255, 255, 0), (255, 255, 0)]]
    unicornhat.set_pixels(pixels)
    unicornhat.show()
    
def six():
    pixels = [[(255, 255, 0), (255, 255, 0), (255, 255, 0), (255, 255, 0), (255, 255, 0), (255, 255, 0), (255, 255, 0), (255, 255, 0)], [(255, 255, 0), (255, 255, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)], [(255, 255, 0), (255, 255, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)], [(255, 255, 0), (255, 255, 0), (255, 255, 0), (255, 255, 0), (255, 255, 0), (255, 255, 0), (255, 255, 0), (255, 255, 0)], [(255, 255, 0), (255, 255, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (255, 255, 0)], [(255, 255, 0), (255, 255, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (255, 255, 0)], [(255, 255, 0), (255, 255, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (255, 255, 0)], [(255, 255, 0), (255, 255, 0), (255, 255, 0), (255, 255, 0), (255, 255, 0), (255, 255, 0), (255, 255, 0), (255, 255, 0)]]
    unicornhat.set_pixels(pixels)
    unicornhat.show()
    
def seven():
    pixels = [[(255, 255, 0), (255, 255, 0), (255, 255, 0), (255, 255, 0), (255, 255, 0), (255, 255, 0), (255, 255, 0), (255, 255, 0)], [(255, 255, 0), (255, 255, 0), (255, 255, 0), (255, 255, 0), (255, 255, 0), (255, 255, 0), (255, 255, 0), (255, 255, 0)], [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (255, 255, 0), (255, 255, 0)], [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (255, 255, 0), (255, 255, 0), (0, 0, 0)], [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (255, 255, 0), (255, 255, 0), (0, 0, 0), (0, 0, 0)], [(0, 0, 0), (0, 0, 0), (0, 0, 0), (255, 255, 0), (255, 255, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)], [(0, 0, 0), (0, 0, 0), (255, 255, 0), (255, 255, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)], [(0, 0, 0), (255, 255, 0), (255, 255, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)]]
    unicornhat.set_pixels(pixels)
    unicornhat.show()
    
def eight():
    pixels = [[(0, 0, 0), (0, 255, 0), (0, 255, 0), (0, 255, 0), (0, 255, 0), (0, 255, 0), (0, 255, 0), (0, 0, 0)], [(0, 0, 0), (0, 255, 0), (0, 255, 0), (0, 255, 0), (0, 255, 0), (0, 255, 0), (0, 255, 0), (0, 0, 0)], [(0, 0, 0), (0, 255, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 255, 0), (0, 0, 0)], [(0, 0, 0), (0, 255, 0), (0, 255, 0), (0, 255, 0), (0, 255, 0), (0, 255, 0), (0, 255, 0), (0, 0, 0)], [(0, 0, 0), (0, 255, 0), (0, 255, 0), (0, 255, 0), (0, 255, 0), (0, 255, 0), (0, 255, 0), (0, 0, 0)], [(0, 0, 0), (0, 255, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 255, 0), (0, 0, 0)], [(0, 0, 0), (0, 255, 0), (0, 255, 0), (0, 255, 0), (0, 255, 0), (0, 255, 0), (0, 255, 0), (0, 0, 0)], [(0, 0, 0), (0, 255, 0), (0, 255, 0), (0, 255, 0), (0, 255, 0), (0, 255, 0), (0, 255, 0), (0, 0, 0)]]
    unicornhat.set_pixels(pixels)
    unicornhat.show()
    
def nine():
    pixels = [[(0, 0, 0), (0, 255, 0), (0, 255, 0), (0, 255, 0), (0, 255, 0), (0, 255, 0), (0, 255, 0), (0, 255, 0)], [(0, 0, 0), (0, 255, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 255, 0)], [(0, 0, 0), (0, 255, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 255, 0)], [(0, 0, 0), (0, 255, 0), (0, 255, 0), (0, 255, 0), (0, 255, 0), (0, 255, 0), (0, 255, 0), (0, 255, 0)], [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 255, 0)], [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 255, 0)], [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 255, 0)], [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 255, 0)]]
    unicornhat.set_pixels(pixels)
    unicornhat.show()
    
def ten():
    pixels = [[(0, 0, 0), (0, 0, 0), (0, 255, 0), (0, 255, 0), (0, 0, 0), (0, 255, 0), (0, 255, 0), (0, 255, 0)], [(0, 0, 0), (0, 255, 0), (0, 255, 0), (0, 255, 0), (0, 0, 0), (0, 255, 0), (0, 0, 0), (0, 255, 0)], [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 255, 0), (0, 0, 0), (0, 255, 0), (0, 0, 0), (0, 255, 0)], [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 255, 0), (0, 0, 0), (0, 255, 0), (0, 0, 0), (0, 255, 0)], [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 255, 0), (0, 0, 0), (0, 255, 0), (0, 0, 0), (0, 255, 0)], [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 255, 0), (0, 0, 0), (0, 255, 0), (0, 0, 0), (0, 255, 0)], [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 255, 0), (0, 0, 0), (0, 255, 0), (0, 0, 0), (0, 255, 0)], [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 255, 0), (0, 0, 0), (0, 255, 0), (0, 255, 0), (0, 255, 0)]]
    unicornhat.set_pixels(pixels)
    unicornhat.show()
    
def tick():
    pixels = [[(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 255, 0)], [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 255, 0), (0, 255, 0)], [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 255, 0), (0, 255, 0), (0, 0, 0)], [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 255, 0), (0, 255, 0), (0, 0, 0), (0, 0, 0)], [(0, 255, 0), (0, 0, 0), (0, 0, 0), (0, 255, 0), (0, 255, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)], [(0, 255, 0), (0, 0, 0), (0, 255, 0), (0, 255, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)], [(0, 255, 0), (0, 255, 0), (0, 255, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)], [(0, 255, 0), (0, 255, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)]]
    unicornhat.set_pixels(pixels)
    unicornhat.show()
    
def cross():
    pixels = [[(255, 0, 0), (255, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (255, 0, 0), (255, 0, 0)], [(0, 0, 0), (255, 0, 0), (255, 0, 0), (0, 0, 0), (0, 0, 0), (255, 0, 0), (255, 0, 0), (0, 0, 0)], [(0, 0, 0), (0, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0), (0, 0, 0), (0, 0, 0)], [(0, 0, 0), (0, 0, 0), (0, 0, 0), (255, 0, 0), (255, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)], [(0, 0, 0), (0, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0), (0, 0, 0), (0, 0, 0)], [(0, 0, 0), (255, 0, 0), (255, 0, 0), (0, 0, 0), (0, 0, 0), (255, 0, 0), (255, 0, 0), (0, 0, 0)], [(255, 0, 0), (255, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (255, 0, 0), (255, 0, 0)], [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)]]
    unicornhat.set_pixels(pixels)
    unicornhat.show()
    
def times():
    pixels = [[(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)], [(0, 0, 0), (0, 0, 0), (255, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (255, 0, 0), (0, 0, 0)], [(0, 0, 0), (0, 0, 0), (0, 0, 0), (255, 0, 0), (0, 0, 0), (255, 0, 0), (0, 0, 0), (0, 0, 0)], [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (255, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)], [(0, 0, 0), (0, 0, 0), (0, 0, 0), (255, 0, 0), (0, 0, 0), (255, 0, 0), (0, 0, 0), (0, 0, 0)], [(0, 0, 0), (0, 0, 0), (255, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (255, 0, 0), (0, 0, 0)], [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)], [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)]]
    unicornhat.set_pixels(pixels)
    unicornhat.show()
    
def equals():
    pixels = [[(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)], [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)], [(0, 0, 0), (0, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0), (0, 0, 0), (0, 0, 0)], [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)], [(0, 0, 0), (0, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0), (0, 0, 0), (0, 0, 0)], [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)], [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)], [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)]]
    unicornhat.set_pixels(pixels)
    unicornhat.show()
    
    
    
