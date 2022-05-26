# 4.* Create an interface for the Laptop with the next methods: Screen, Keyboard, Touchpad, WebCam, Ports, Dynamics
# and create an HPLaptop class by using your interface.

from abc import ABC, abstractmethod

class Laptop(ABC):

    @abstractmethod
    def Screen(self):
        raise NotImplementedError('This method is not implemented')

    @abstractmethod
    def Keyboard(self):
        raise NotImplementedError('This method is not implemented')

    @abstractmethod
    def Touchpad(self):
        raise NotImplementedError('This method is not implemented')

    @abstractmethod
    def WebCam(self):
        raise NotImplementedError('This method is not implemented')

    @abstractmethod
    def Ports(self):
        raise NotImplementedError('This method is not implemented')

    @abstractmethod
    def Dynamics(self):
        raise NotImplementedError('This method is not implemented')

class HPLaptop(Laptop):

    def __init__(self, screen, keyboard, touchpad, webcam, ports, dynamics):
        self.screen = screen
        self.keyboard = keyboard
        self.touchpad = touchpad
        self.webcam = webcam
        self.ports = ports
        self.dynamics = dynamics

    def Screen(self):
        return self.screen

    def Keyboard(self):
        return self.keyboard

    def Touchpad(self):
        return self.touchpad

    def WebCam(self):
        return self.webcam

    def Ports(self):
        return self.ports

    def Dynamics(self):
        return self.dynamics

laptop = HPLaptop(24, 'Razer', 'Razer', 'Logitech', 8, 'F&D')