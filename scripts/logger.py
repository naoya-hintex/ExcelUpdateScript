from pathlib import Path
from common import create_filePath
import logging
import os

# ＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊
# 関数名           setup_logger                                                             
# 処理概要         ログ出力設定を初期化します。                                                          
# 作成者           naoya-hintex                                                           
# 引数             log_config: ログ設定情報                                                           
# ＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊
def setup_logger(log_config: dict):

    # ログ出力がFalseの場合、ログ出力を無効化して終了
    if not log_config.get("enable", False):
        logging.disable(logging.CRITICAL)
        return
    
    # logファイルのパスを作成
    log_file = create_filePath(log_config["log_folder"], log_config["log_file"])
    
    # ログレベルとフォーマットを取得
    log_level = log_config.get("level", "INFO")
    log_format = log_config.get("format")

    # ログフォルダがなければ作成
    os.makedirs(os.path.dirname(log_file), exist_ok=True)

    # ログ出力設定を初期化
    logging.basicConfig(
        filename=log_file,
        level=getattr(logging, log_level),
        format=log_format,
        encoding="utf-8"
    )
