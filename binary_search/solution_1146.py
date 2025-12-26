class SnapshotArray:

    def __init__(self, length: int):
        self.count = 0

    def set(self, index: int, val: int) -> None:

    def snap(self) -> int:
        self.count += 1

    def get(self, index: int, snap_id: int) -> int:

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)