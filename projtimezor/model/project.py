class Project:

    def __init__(self, data):
        self.group_uuid = data['group_uuid']
        self.name = data['name']
        self.description = data['description']
        self.affinity = data['affinity']
        self.elapsed_time = data['elapsed_time']
        self.steps_finished = data['steps_finished']
        self.affinity = data['affinity']
        self.steps_list = initialize_steps(data['steps'])

    @property
    def properties(self):
        return self.__dict__

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
        for step in self.steps_list:
            if step.inner_steps:
                step_found, steps_count = self._search_inner_steps(step.inner_steps, steps_count)
            else:
                if steps_count == self.steps_finished:
                    return step_found

                else:
                    steps_count += 1

        return step_found


class Step:

    def __init__(self, data):
        self.description = data['description']
        self.order = data['order']
        self.elapsed_time = data['elapsed_time']
        self.finished = data['finished']
        if data.get('steps'):
            self.inner_steps = initialize_steps(data['steps'])
        else:
            self.inner_steps = False

def initialize_steps(data_steps):
    steps_list = list()
    for single_step in data_steps:
        steps_list.append(Step(single_step))
    return steps_list