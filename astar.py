A_STAR_SPACE = 0xFFFFFFFF
A_STAR_WALL = 0xFFFFFFFE

class astar:
    def __init__(self):
        self.map = None  # 2D list for map
        self.xs = 0
        self.ys = 0
        self.px = None  # list of x-coordinates of the path
        self.py = None  # list of y-coordinates of the path
        self.ps = 0     # path length

    def _freemap(self):
        """Release the memory of the map."""
        self.map = None
        self.xs = 0
        self.ys = 0

    def _freepnt(self):
        """Release the memory of the path points."""
        self.px = None
        self.py = None
        self.ps = 0

    def resize(self, _xs, _ys):
        """Resize the map to new dimensions."""
        if self.xs == _xs and self.ys == _ys:
            return
        self._freemap()
        self.xs = _xs
        self.ys = _ys
        self.map = [[A_STAR_SPACE for _ in range(self.xs)] for _ in range(self.ys)]

    def set(self, bitmap, col_wall):
        """Set the map using a bitmap (2D list) with a specific wall color."""
        self.resize(len(bitmap[0]), len(bitmap))
        for y in range(self.ys):
            for x in range(self.xs):
                self.map[y][x] = A_STAR_WALL if bitmap[y][x] == col_wall else A_STAR_SPACE

    def get(self):
        """Return the map for debugging purposes."""
        return [[self.map[y][x] for x in range(self.xs)] for y in range(self.ys)]

    def compute(self, x0, y0, x1, y1):
        """Compute the path from (x0, y0) to (x1, y1) using the A* algorithm."""
        # Clear previous paths
        for y in range(self.ys):
            for x in range(self.xs):
                if self.map[y][x] != A_STAR_WALL:
                    self.map[y][x] = A_STAR_SPACE

        self._freepnt()

        # Init points lists for BFS-like exploration
        i0 = 0
        i1 = self.xs * self.ys
        n0 = 0
        n1 = 0
        px = [0] * (i1 * 2)
        py = [0] * (i1 * 2)

        if self.map[y0][x0] == A_STAR_SPACE:
            px[i0 + n0] = x0
            py[i0 + n0] = y0
            n0 += 1
            self.map[y0][x0] = 0

            for j in range(1, self.xs * self.ys):
                if self.map[y1][x1] != A_STAR_SPACE:
                    break

                e = False
                for ii in range(i0, i0 + n0):
                    x, y = px[ii], py[ii]

                    # Test neighbors
                    for yy, xx in [(y-1, x), (y+1, x), (y, x-1), (y, x+1)]:
                        if 0 <= yy < self.ys and 0 <= xx < self.xs and self.map[yy][xx] == A_STAR_SPACE:
                            self.map[yy][xx] = j
                            px[i1 + n1] = xx
                            py[i1 + n1] = yy
                            n1 += 1
                            e = True

                if not e:
                    break

                # Swap the lists
                i0, i1 = i1, i0
                n0, n1 = n1, 0

        # Reconstruct path if found
        if self.map[y1][x1] == A_STAR_SPACE or self.map[y1][x1] == A_STAR_WALL:
            return  # No path found

        self.ps = self.map[y1][x1] + 1
        self.px = [0] * self.ps
        self.py = [0] * self.ps

        x, y = x1, y1
        for i in range(self.ps - 1, -1, -1):
            self.px[i] = x
            self.py[i] = y

            if y > 0 and self.map[y-1][x] == i - 1:
                y -= 1
            elif y < self.ys - 1 and self.map[y+1][x] == i - 1:
                y += 1
            elif x > 0 and self.map[y][x-1] == i - 1:
                x -= 1
            elif x < self.xs - 1 and self.map[y][x+1] == i - 1:
                x += 1
