from algorithm_manager_class import AlgorithmManager
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