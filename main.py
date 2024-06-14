import os
import shutil
from datetime import datetime


def get_latest_folder_name(directory: str) -> str:
    """directoryフォルダ内のYYYY_MMDD形式になっているファイル一覧から最新のものを選択する

    Args:
        directory (str, optional): 検索対象. Defaults to "./raw".

    Returns:
        str: YYYY_MMDDが最新のフォルダのパス
    """

    # ディレクトリ内のファイル名のみを取得
    folder_names = os.listdir(directory)

    # ファイル名取得するやつ
    dates_dict = {}
    for folder_name in folder_names:
        try:
            yyyy_mmdd_datetime = datetime.strptime(folder_name, "%Y_%m%d")

            yyyy_mmdd_str = folder_name

            dates_dict[yyyy_mmdd_datetime] = yyyy_mmdd_str

        except ValueError:
            # YYYY_MMDD形式以外はエラー出るので無視する
            pass

    # 最新を取得
    yyyy_mmdd_datetime_latest = max(list(dates_dict.keys()))

    yyyy_mmdd_str_latest = dates_dict[yyyy_mmdd_datetime_latest]

    latest_folder_path = os.path.join(directory, yyyy_mmdd_str_latest)

    print(f"latest_folder: {latest_folder_path}")

    return latest_folder_path


def folder_actions(
    source_directory: str, process_directory: str = "./processing"
) -> None:
    """source_directoryフォルダ内のファイル名でprocess_directoryフォルダ配下にフォルダを作成して、コピーする

    Args:
        source_directory (str): コピー元
        process_directory (str, optional): コピー先. Defaults to "./processing".
    """

    if not os.path.exists(process_directory):
        os.makedirs(process_directory)

    filelist = os.listdir(source_directory)

    # 各ファイルについて処理
    for filename in filelist:
        # ファイル名から拡張子を除外
        base_name = os.path.splitext(filename)[0]
        file_path = os.path.join(source_directory, filename)

        # フォルダを作成 (拡張子を除いたファイル名のフォルダ)
        folder_path = os.path.join(process_directory, base_name)

        print(f"copy: {file_path} -> {folder_path}")

        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        # ファイルの場合、単純にコピー
        if os.path.isfile(file_path):
            shutil.copy(file_path, folder_path)


if __name__ == "__main__":
    latest_folder_name = get_latest_folder_name(directory="./raw")

    folder_actions(source_directory=latest_folder_name)
