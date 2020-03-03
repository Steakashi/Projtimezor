import datetime
import uuid


from ..constants import STATE_FINISHED


class Project:

    def __init__(self, data):
        self.group_id = data.get('group_id')
        self.id = data.get("id", str(uuid.uuid4()))
        self.name = data['name']
        self.description = data['description']
        self.finished = data.get('finished', False)
        self.elapsed_time = datetime.timedelta(seconds=(data.get('elapsed_time', 0)))
        self.steps_finished = data.get('steps_finished', 0)
        self.steps = initialize_steps(data.get('steps', []))
        self.steps_number = self.count_steps()
        self.priority = data['priority']
        self.current_step = None
        self.filename = data.get('filename', 'project_{}_{}'.format(self.name, self.id))

    @property
    def properties(self):
        return self.__dict__

    @property
    def json(self):
        json = dict()
        for key, value in self.__dict__.items():
            if key == 'steps':
                json[key] = [step_data.json for step_data in value]
            elif key == 'elapsed_time':
                json[key] = value.seconds
            elif key not in ['filename', 'current_step']:
                json[key] = value
        return json

    def _search_inner_steps(self, browsed_steps, steps_count):
        step_found = None
        for step in browsed_steps:
            if step.inner_steps:
                step_found, steps_count = self.get_current_step(step.inner_steps, steps_count)
            else:
                if steps_count == self.steps_finished:
                    return step, steps_count

                else:
                    steps_count += 1

        return step_found, steps_count

    def _count_inner_steps(self, steps_list, steps_number=0):
        for step in steps_list:
            steps_number += 1
            if step.inner_steps:
                steps_number = self._count_steps(step.inner_steps, steps_number)

        return steps_list, steps_number

    def count_steps(self):
        steps_number = 0
        for step in self.steps:
            if step.inner_steps:
                step_list, steps_number = self._count_inner_steps(step.inner_steps, steps_number)
            else:
                steps_number += 1
        return steps_number

    def get_current_step(self):
        if self.finished:
            return STATE_FINISHED

        steps_count = 0
        step_found = self.steps[0]

        for step in self.steps:
            print(step)
            if step.inner_steps:
                step_found, steps_count = self._search_inner_steps(step.inner_steps, steps_count)
            else:
                if steps_count == self.steps_finished:
                    self.current_step = step_found
                    return step_found

                else:
                    steps_count += 1

        if step_found:
            self.current_step = step_found

        return self.current_step

    def validate_step(self):
        if self.finished:
            return

        self.current_step.validate_step()
        self.steps_finished += 1
  
        if self.steps_finished == self.steps_number:
            self.finished = True

    def register_elapsed_time(self, elapsed_time):
        self.elapsed_time += elapsed_time


class Step:

    def __init__(self, data):
        self.description = data['description']
        self.order = data['order']
        self.elapsed_time = datetime.timedelta(seconds=(data['elapsed_time']))
        self.finished = data['finished']
        if data.get('steps'):
            self.inner_steps = initialize_steps(data['steps'])
        else:
            self.inner_steps = False

    @property
    def json(self):
        json = dict()
        for key, value in self.__dict__.items():
            if key == 'inner_steps':
                if not self.inner_steps:
                    continue
                json['steps'] = [inner_step_data.json for inner_step_data in value]
            elif key == 'elapsed_time':
                json[key] = value.seconds
            else:
                json[key] = value
        return json

    def validate_step(self):
        self.finished = True


def initialize_steps(data_steps):
    steps_list = list()
    for single_step in data_steps:
        steps_list.append(Step(single_step))
    return steps_list