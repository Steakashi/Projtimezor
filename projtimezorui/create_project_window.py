from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import Screen
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.properties import ListProperty
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Rectangle

import uuid
import os


PROJECT_FIELDS = [
    "name",
    "description",
    "priority",
    "group",
]
STEP_FIELDS = [
    "description"
]
BUTTON_SIZE = 60


ADD = 'ADD'
EDIT = 'EDIT'
STEP_OBJECT = 'STEP_OBJECT'
STEP_LABEL = 'STEP_LABEL'


SIZE_PROJECT_GRID = (0, 240)
SIZE_ADD_STEP = (0, 180)
SIZE_HINT_ADD_STEP = (.8, None)
SIZE_STEPS_GRID = (0, Window.height - SIZE_PROJECT_GRID[1])


class ColoredBackgoundMixin:
    _color = None
    _rect = None
    background_color = ListProperty([0.0, 0.0, 0.0, 1.0])

    def __init__(self, *, background_color, **kwargs):
        super().__init__(**kwargs)
        with self.canvas.before:
            self.background_color = background_color
            self._color = Color(*background_color)
            self._rect = Rectangle(size=self.size, pos=self.pos)
            self.bind(size=self._update_rect, pos=self._update_rect, background_color=self._update_rect)

    def _update_rect(self, instance, value):
        self._color.rgba = instance.background_color
        self._rect.pos = instance.pos
        self._rect.size = instance.size


class CustomBoxLayout(ColoredBackgoundMixin, BoxLayout):
    pass


class CreateProjectWindow(Screen):

    created_steps = dict()
    current_popup = None
    current_edited_step = None

    def __init__(self, **kwargs):
        super(CreateProjectWindow, self).__init__(**kwargs)
        self.main_layout = GridLayout(cols=1, padding=20)

        self.project_grid = GridLayout(cols=2, size=SIZE_PROJECT_GRID, size_hint=(1, None))
        self.projects_inputs = list()
        for field in PROJECT_FIELDS:
            self.project_grid.add_widget(Label(text=field.capitalize()))
            text_input = TextInput(text='', multiline=False)
            self.projects_inputs.append(text_input)
            self.project_grid.add_widget(text_input)

        self.steps_creation_layout = GridLayout(cols=2, row_force_default=True, row_default_height=40)
        self.steps_inputs = list()
        for field in STEP_FIELDS:
            self.steps_creation_layout.add_widget(Label(text=field.capitalize()))
            text_input = TextInput(text='', multiline=False)
            self.steps_inputs.append(text_input)
            self.steps_creation_layout.add_widget(text_input)

        self.steps_layout = GridLayout(cols=1, spacing=5, padding=(0, 10, 0, 0), size_hint_y=None)
        self.steps_layout.bind(minimum_height=self.steps_layout.setter('height'))
        scroll_steps_layour = ScrollView(size_hint=(1, None), height=SIZE_STEPS_GRID[1])
        scroll_steps_layour.add_widget(self.steps_layout)

        button_close = Button(text='Validate')
        button_close.bind(on_press=self.validate_step_popup)

        self.step_popup = Popup(
            title='Add Step',
            content=self.steps_creation_layout,
            auto_dismiss=False,
            size=SIZE_ADD_STEP,
            size_hint=SIZE_HINT_ADD_STEP
        )

        self.steps_creation_layout.add_widget(button_close)

        self.main_layout.add_widget(self.project_grid)
        self.main_layout.add_widget(scroll_steps_layour)
        self.add_widget(self.main_layout)

    def get_text_projects_inputs(self):
        return {PROJECT_FIELDS[count]: input_.text for count, input_ in enumerate(self.projects_inputs)}

    def get_text_steps_inputs(self):
        return {STEP_FIELDS[count]: input_.text for count, input_ in enumerate(self.steps_inputs)}

    def validate_step_popup(self, instance):
        if self.current_popup == ADD:
            self.add_step(instance)
        elif self.current_popup == EDIT:
            self.edit_step(instance)

    def empty_steps_inputs(self):
        for step in self.steps_inputs:
            step.text = ""

    def regenerate_steps(self):
        for id, step in self.created_steps.items():
            self.add_step(step_object=step[STEP_OBJECT])

    def delete_step(self, instance, step_id, step_layout):
        self.created_steps.pop(step_id)
        self.steps_layout.remove_widget(step_layout)

    def add_step(self, instance=None, step_object=None):
        if not instance and not step_object:
            return

        if not step_object:
            step_object = self.get_text_steps_inputs()

        step_id = str(uuid.uuid4())

        step_layout = CustomBoxLayout(
            orientation='horizontal', size=(0, BUTTON_SIZE), size_hint=(1, None),
            background_color=[1, 1, 1, .1]
        )
        button_edit = Button(text='Edit', size=(BUTTON_SIZE, BUTTON_SIZE), size_hint=(None, None))
        button_add = Button(text='Add', size=(BUTTON_SIZE, BUTTON_SIZE), size_hint=(None, None))
        button_delete = Button(text='Delete', size=(BUTTON_SIZE, BUTTON_SIZE), size_hint=(None, None))

        button_edit.fbind('on_press', self.edit_step_window, step_id=step_id)#, step_layout=step_layout)
        button_delete.fbind('on_press', self.delete_step, step_id=step_id, step_layout=step_layout)

        step_label = Label(text=step_object['description'])
        step_layout.add_widget(step_label)
        step_layout.add_widget(button_edit)
        step_layout.add_widget(button_add)
        step_layout.add_widget(button_delete)

        self.created_steps[step_id] = {
            STEP_OBJECT: step_object,
            STEP_LABEL: step_label
        }

        self.steps_layout.add_widget(step_layout)
        self.step_popup.dismiss()

    def edit_step(self, instance=None):
        step_object = self.get_text_steps_inputs()
        self.created_steps[self.current_edited_step][STEP_OBJECT] = step_object
        self.created_steps[self.current_edited_step][STEP_LABEL].text = step_object[STEP_FIELDS[0]]

        self.current_edited_step = None
        self.step_popup.dismiss()

    def edit_step_window(self, instance, step_id):
        self.current_popup = EDIT
        self.current_edited_step = step_id
        for index, step_input in enumerate(self.steps_inputs):
            step_input.text = self.created_steps[step_id][STEP_OBJECT][STEP_FIELDS[index]]
        self.step_popup.open()

    def add_step_window(self, instance=None):
        self.current_popup = ADD
        self.empty_steps_inputs()
        self.step_popup.open()

    def set_parameters(self, parent):
        button_add_step = Button(text="Add Step")
        button_add_step.bind(on_press=self.add_step_window)

        button_create = Button(text='Create')
        button_create.bind(on_press=parent.create_project)

        self.project_grid.add_widget(Widget())
        self.project_grid.add_widget(button_add_step)
        self.project_grid.add_widget(Widget())
        self.project_grid.add_widget(button_create)
