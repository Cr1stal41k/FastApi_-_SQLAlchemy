import pandas as pd
import streamlit as st

# Данные первой таблицы
df1 = {'name': ['UVG_E2', 'PBF_E2', 'NK_85', '85-120', '120-180', '150-250', '240-290', '290-350', 'HDT', 'HG_350-500',
                'Gudron'],
       'step': ['-6.02E-06', '3.83334E-05', '0.000491509', '0.008477915', '-0.052740835', '0.1', '-0.035069205',
                '-0.054749528', '0.006494053', '0.033615096', '-0.006551321'],
       'Weight': ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
       'Base': ['0.21', '1.35', '4.01', '5.43', '3.44', '8.01', '8.43', '15.17', '2.76', '25.45', '25.76'],
       'Target': ['0.03', '2', '0.03', '0.1', '0.1', '9', '8.45', '0.1', '0.1', '0.03', '0.1']}

# Данные второй таблицы
df2 = {'name': ['Benz,ECP', 'TS,ECP', 'DT,ECP'],
       'step': ['-0.33817', '0.396186', '-0.19664'],
       'ub': ['167.6', '218.9', '344.8'],
       'lb': ['147.3', '196.8', '336.1'],
       'Base': ['161.79', '202.06', '346.44']}

st.title('Добро пожаловать на тестовый проект!')

# Создание таблиц
table1 = pd.DataFrame(df1)
table2 = pd.DataFrame(df2)

# Создание колонок
col0, col1 = st.columns(2)
col2, col3 = st.columns(2)

# Названия таблиц
col0.markdown("<h4 style='text-align: center; color: green;'>Таблица 1</h1>", unsafe_allow_html=True)
col1.markdown("<h4 style='text-align: center; color: green;'>Таблица 2</h1>", unsafe_allow_html=True)

# Возможность редактирования таблиц
edited_col1 = col2.experimental_data_editor(table1)
edited_col2 = col3.experimental_data_editor(table2)

# Присваивание переменных для полей 1ой таблицы
step_UVG_E2, step_PBF_E2, step_NK_85, step_85_120, step_120_180, step_150_250, step_240_290, step_290_350, \
step_HDT, step_HG_350_500, step_Gudron = edited_col1['step']

Weight_UVG_E2, Weight_PBF_E2, Weight_NK_85, Weight_85_120, Weight_120_180, Weight_150_250, Weight_240_290, Weight_290_350, \
Weight_HDT, Weight_HG_350_500, Weight_Gudron = edited_col1['Weight']

Base_UVG_E2, Base_PBF_E2, Base_NK_85, Base_85_120, Base_120_180, Base_150_250, Base_240_290, Base_290_350, \
Base_HDT, Base_HG_350_500, Base_Gudron = edited_col1['Base']

Target_UVG_E2, Target_PBF_E2, Target_NK_85, Target_85_120, Target_120_180, Target_150_250, Target_240_290, Target_290_350, \
Target_HDT, Target_HG_350_500, Target_Gudron = edited_col1['Target']

# Присваивание переменных для полей 2ой таблицы
step_Benz_ECP, step_TS_ECP, step_DT_ECP = edited_col2['step']

ub_Benz_ECP, ub_TS_ECP, ub_DT_ECP = edited_col2['ub']

lb_Benz_ECP, lb_TS_ECP, lb_DT_ECP = edited_col2['lb']

Base_Benz_ECP, Base_TS_ECP, Base_DT_ECP = edited_col2['Base']
