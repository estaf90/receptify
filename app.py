from pathlib import Path
from src.load_data import load_dict_from_file
import pandas as pd

if __name__ == '__main__':
    xml_path = str(Path(Path(__file__).parent, 'data', '20170101.xml'))
    data = load_dict_from_file(xml_path)
    data_lm = data['LivsmedelsLista']['Livsmedel']  # list of "livsmedel"
    df = pd.DataFrame(data_lm)
    print(df.head())