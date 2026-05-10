from pathlib import Path

from src.app import App


BASE_DIR = Path(__file__).parent
PATHS_PATH = BASE_DIR / 'config' / 'paths' / 'paths.json'
ENCODING = 'utf-8'

app = ... # BASE_DIR, PATHS_PATH, ENCODING

if __name__ == '__main__':
	# app.run()
	pass
