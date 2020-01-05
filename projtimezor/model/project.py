import datetime


class Project:

    def __init__(self, data):
        self.group_uuid = data['group_uuid']
        self.name = data['name']
        self.description = data['description']
        self.affinity = data['affinity']
        self.elapsed_time = datetime.timedelta(seconds=(data['elapsed_time']))
        self.steps_finished = data['steps_finished']
        self.affinity = data['affinity']
        self.steps = initialize_steps(data['steps'])
        self.filename = data['filename']

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
            elif key != 'filename':
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

    def get_current_step(self):
        steps_count = 0
        for step in self.steps:
            if step.inner_steps:
                step_found, steps_count = self._search_inner_steps(step.inner_steps, steps_count)
            else:
                if steps_count == self.steps_finished:
                    return step_found

                else:
                    steps_count += 1

        return step_found

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


def initialize_steps(data_steps):
    steps_list = list()
    for single_step in data_steps:
        steps_list.append(Step(single_step))
    return steps_list