from pathlib import Path
from common import create_filePath
import json

# ＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊
# 関数名           load_config                                                             
# 処理概要         設定ファイルを読み込み、設定情報を返却します。                                                          
# 作成者           naoya-hintex                                                           
# 戻り値           configData: 設定データ                                                       
# ＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊
def load_config():

    # 設定ファイルを取得するパスを作成
    config_path = create_filePath("config", "setting.json")

    # 設定ファイルを読み込み、読み込んだデータを返却
    with open(config_path, "r", encoding="utf-8") as f:
        return json.load(f)