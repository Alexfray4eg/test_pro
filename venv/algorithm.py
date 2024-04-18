class Algorithm:
    def __init__(self, name):
        self.name = name

    def execute(self):
        print(f"Executing algorithm: {self.name}")


class AlgorithmManager:
    def __init__(self):
        self.algorithms = {}
        self.analytics = []

    def create_algorithm(self, name, tags):
        algorithm = Algorithm(name)
        for tag in tags:
            if tag not in self.algorithms:
                self.algorithms[tag] = []
            self.algorithms[tag].append(algorithm)
        return algorithm

    def apply_to_tasks(self, tag, task_database):
        algorithms = self.algorithms.get(tag, [])
        for algorithm in algorithms:
            print(f"Applying algorithm '{algorithm.name}' to tasks in {task_database}")

    def random_impulse(self):
        return random.randint(1, 3)

    def analyze_impulses(self):
        impulse_data = []
        for tag, algorithms in self.algorithms.items():
            for algorithm in algorithms:
                impulse_data.append((algorithm.name, self.random_impulse()))
        return impulse_data

    def analyze_kpd(self):
        kpd_data = []
        for tag, algorithms in self.algorithms.items():
            for algorithm in algorithms:
                kpd_data.append((algorithm.name, random.uniform(0, 1)))
        return kpd_data

    def regulate_parameters(self):
        parameter_data = []
        for tag, algorithms in self.algorithms.items():
            for algorithm in algorithms:
                parameter_data.append((algorithm.name, random.randint(1, 100)))
        return parameter_data

    def analyze_all(self):
        impulses = self.analyze_impulses()
        kpd = self.analyze_kpd()
        parameters = self.regulate_parameters()
        self.analytics.extend(impulses)
        self.analytics.extend(kpd)
        self.analytics.extend(parameters)

# main.py

from algorithm import AlgorithmManager

if __name__ == "__main__":
    manager = AlgorithmManager()

    algorithm1 = manager.create_algorithm("Algorithm1", ["Tag1", "Tag3"])
    algorithm2 = manager.create_algorithm("Algorithm2", ["Tag2", "Tag4"])

    manager.apply_to_tasks("Tag1", "TaskDB1")
    manager.apply_to_tasks("Tag2", "TaskDB2")
    manager.apply_to_tasks("Tag3", "TaskDB3")
    manager.apply_to_tasks("Tag4", "TaskDB4")

    manager.analyze_all()

    print("Analytics Data:")
    for data in manager.analytics:
        print(data)
