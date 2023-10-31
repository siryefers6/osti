from pathlib import Path

path = Path('dir1/dir2/dir3/dir4')
path.mkdir(parents=True)
print(path.is_relative_to('.'))