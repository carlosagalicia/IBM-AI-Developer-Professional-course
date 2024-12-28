class RoomModel(Model):
    def __init__(self, width, height, dirty_cells=0.90, vacuums=5):
        super().__init__()
        """
        Initializes the RoomModel with given dimensions,
        percentage of dirty cells, and number of vacuums.

        Args:
            width (int): Width of the room grid.
            height (int): Height of the room grid.
            dirty_cells (float): Percentage of cells initially dirty (default: 0.90).
            vacuums (int): Number of vacuum cleaner agents (default: 5).
        """
        self.grid = SingleGrid(width, height, torus=False)
        self.schedule = RandomActivation(self)
        self.steps = 0
        self.vacuums = vacuums
        self.running = True  # The simulation runs until the room is clean.
        self.dirty_agents = 0
        self.datacollector = DataCollector(
            model_reporters={"Grid": get_grid, "Steps": lambda m: m.steps})

        # The model dirty the cells randomly
        num_dirty_cells = int(width * height * dirty_cells)
        dirty_cells_placed = 0
        self.dirty_agents = num_dirty_cells
        while dirty_cells_placed < num_dirty_cells:
            dirt_agent = Dirt(dirty_cells_placed + 1, self)
            self.grid.move_to_empty(dirt_agent)
            self.schedule.add(dirt_agent)
            dirty_cells_placed += 1

        # Place vacuum cleaners
        for i in range(self.vacuums):
            agent = VacuumCleaner(i, self)
            self.grid.move_to_empty(agent)
            self.schedule.add(agent)


    # Vacuum Cleaner Efficiency
    def vacuum_efficiency(self):
        avg_efficiency = 0
        for i in self.schedule.agents:
            if isinstance(i, VacuumCleaner):
                if i.visited > 0:
                    efficiency = i.cleaned / i.visited
                else:
                    efficiency = 0
                print(f"Vacuum Efficiency {i.unique_id}: {efficiency * 100:.2f}%")
                avg_efficiency += efficiency
        print()
        return avg_efficiency / self.vacuums


    def decrease_dirty_cells(self):
        self.dirty_agents -= 1

    def step(self):
        if self.dirty_agents == 0:
          print("Clean habitat. Finishing simulation.")
          return

        self.datacollector.collect(self)
        self.schedule.step()
        self.steps += 1
