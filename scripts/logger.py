from pathlib import Path
import logging
import os

# loggerの初期設定
def setup_logger(log_config: dict):

    if not log_config.get("enable", False):
        logging.disable(logging.CRITICAL)
        return
    
    # このファイルを起点にlogファイルのパスを作成
    base_dir = Path(__file__).resolve().parent.parent
    log_file = base_dir / log_config["log_file"]
    
    log_level = log_config.get("level", "INFO")
    
    log_format = log_config.get("format")

    # ログフォルダがなければ作成
    os.makedirs(os.path.dirname(log_file), exist_ok=True)

    logging.basicConfig(
        filename=log_file,
        level=getattr(logging, log_level),
        format=log_format,
        encoding="utf-8"
    )
