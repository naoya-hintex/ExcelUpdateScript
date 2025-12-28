from pathlib import Path

# ＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊
# 関数名           create_FilePath                                                             
# 処理概要         フォルダパスとファイル名からファイルパスを作成します。                                                          
# 作成者           naoya-hintex                                                           
# 引数             input_Config: 設定情報                                                           
# 戻り値           df: CSVデータ                                                       
# ＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊
def create_filePath(targetFolderPath: str, targetFileName: str):

    # プロジェクトのルートディレクトリを取得
    base_dir = Path(__file__).resolve().parent.parent

    # フォルダパスとファイル名を結合して返却
    return base_dir / targetFolderPath / targetFileName