from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.gridlayout import GridLayout
from kivy.graphics.vertex_instructions import Line
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Rectangle

from kivy.properties import StringProperty, BooleanProperty

from kivy.metrics import dp

class WidgetsExample(GridLayout):
    my_text = StringProperty("Hello!")
    slider_val = StringProperty("StringValue")
    count = 1
    countb = BooleanProperty(False)
    text_input_str = StringProperty("init")
    def on_button_click(self):
        print("Button clicked")
        if not self.countb:
            self.count += 1
            self.my_text = str(self.count)
    def on_toggle_state(self, toggle_button):
        print("toggle state", toggle_button.state)
        if toggle_button.state == "normal":
            self.countb = True
            toggle_button.text = "OFF"
            toggle_button.color = 1, 0, 0, 1
        else:
            self.countb = False
            toggle_button.text = "ON"
            toggle_button.color = 0, 1, 0, 1
    def on_switch_active(self, widget):
        print("switch:", widget.active)

    # def on_slider_value(self, widget):
    #     print("slider", widget.value)
    #     self.slider_val = str(int(widget.value))

    def on_text_validate(self, widget):
        self.text_input_str = str(widget.text)




class StackLayoutExample(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "lr-tb"
        for i in range(100):
            size = dp(100)
            b = Button(text=str(i), size_hint=(None, None), size=(size, size))
            self.add_widget(b)

class AnchorLayoutExample(AnchorLayout):
    pass

class BoxLayoutExampe(BoxLayout):
    pass
    # def __init__(self, **kwargs):
        # super().__init__(**kwargs)
        # self.orientation= "vertical"
        # b1 = Button(text="Ich bin ein Button")
        # b2 = Button(text="Weiterer Button")
        # self.add_widget(b1)
        # self.add_widget(b2)

class MainWidget(Widget):
    pass

class TravelApp(App):
    pass


class CanvasExample1(Widget):
    pass

class CanvasExample2(Widget):
    pass

class CanvasExample3(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Line(points=(100,100,200,300))
            Color(0,1,0)
            Line(circle=(400, 200, 80), width=2)
            Line(rectangle=(400, 200, 80, 20), width=2)
            self.rect = Rectangle(pos=(700, 200), size=(150,100))
    def on_click(self):
        # print("foo")
        x, y = self.rect.pos
        x -= dp(10)
        self.rect.pos = (x, y)
             


TravelApp().run()