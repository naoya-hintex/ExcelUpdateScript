from pathlib import Path
import json

def load_config():

    # このファイルを起点に「config.py」を取得するパスを作成
    base_dir = Path(__file__).resolve().parent.parent
    config_path = base_dir / "config" / "setting.json"

    # ファイルを読み込み、読み込んだデータを返却
    with open(config_path, "r", encoding="utf-8") as f:
        return json.load(f)