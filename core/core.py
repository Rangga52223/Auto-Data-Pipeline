from core.data_input_handler import main_data_input
from core.EDA_Handler.EDA_1 import main_eda

def full_main(file):
    df = main_data_input(file)
    main_eda(df)
