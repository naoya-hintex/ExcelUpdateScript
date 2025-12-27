from config import load_config
from logger import setup_logger
from pathlib import Path
import logging
import pandas as pd

def load_csv(input_Config):

    # CSVファイルのパスを作成
    base_dir = Path(__file__).resolve().parent.parent
    csv_path = base_dir / input_Config["csv_folder"] / input_Config["file_name"]
    
    # データフレームで取得
    df = pd.read_csv(csv_path, encoding='utf-8')
    return df

def aggregate_daily(csvData):

    # 集約したデータを格納する辞書
    test = csvData.pivot_table(index='date', columns='category', values=['count', 'avg_process_time'], aggfunc='sum', fill_value=0)

    return csvData.pivot_table(index='日付', columns='商品', values='売上', aggfunc='sum', fill_value=0)


def update_excel():
    pass

def main():

    # configの読み込み
    configData = load_config()

    # loggerの初期設定
    setup_logger(configData["log"])

    logging.info("CSV転記処理を開始します。")

    try:

        # CSVファイルを取得 
        csvData = load_csv(configData["input"])

        # アウトプットデータの作成
        outputData = aggregate_daily(csvData)

        # エクセルファイルを更新
        update_excel()

    except:
        logging.exception("エラーが発生しました。")
        raise

if __name__ == "__main__":
    main()