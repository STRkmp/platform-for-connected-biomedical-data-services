
def recognize(input_file):
    import pandas as pd
    import joblib
    import os
    current_directory = os.getcwd()

    df = pd.read_csv(current_directory + '/resource/Columns.csv')

    p = pd.read_csv(input_file)

    df_a = df.mask(p.notnull(), p)

    disease_list = ['Retinopathy', 'Kidney Disease', 'Dementia', 'Heart Disease', 'Stroke']
    d_chance = {key: None for key in disease_list}

    if df_a.Retinopathy[0] == 0:
        retino = ['Sex',
                  'Age',
                  'Diabetes duration (y)',
                  'KidneyDisease',
                  'Smoking',
                  'Drinking',
                  'Height(cm)',
                  'Weight(kg)',
                  'BMI (kg/m2)',
                  'SBP (mmHg)',
                  'DBP (mmHg)',
                  'HbA1c (%)',
                  'FBG (mmol/L)',
                  'TG(mmoll)',
                  'C-peptide (ng/ml)',
                  'TC(mmoll)',
                  'HDLC(mmoll)',
                  'LDLC(mmoll)',
                  'Insulin',
                  'Metformin',
                  'Lipid lowering drugs']
        df_retino = df_a[retino]
        model_retino = joblib.load(current_directory + "/model/rf_o_ret.joblib")
        pred_proba_Retino = model_retino.predict_proba(df_retino)[:, 1]
        chance_percent = f"{pred_proba_Retino[0] * 100:.2f}%"
        d_chance['Retinopathy'] = f"Chance of development Retinopathy: {chance_percent}"
        df_check = p[retino]
        if df_check.isnull().any().any():
            d_chance['Retinopathy'] += " !!! Accuracy reduced due to insufficient data"
        print(pred_proba_Retino)

    if df_a.KidneyDisease[0] == 0:
        neph = ['Sex',
                'Age',
                'Diabetes duration (y)',
                'Retinopathy',
                'Smoking',
                'Drinking',
                'Height(cm)',
                'Weight(kg)',
                'BMI (kg/m2)',
                'SBP (mmHg)',
                'DBP (mmHg)',
                'HbA1c (%)',
                'FBG (mmol/L)',
                'TG(mmoll)',
                'C-peptide (ng/ml)',
                'TC(mmoll)',
                'HDLC(mmoll)',
                'LDLC(mmoll)',
                'Insulin',
                'Metformin',
                'Lipid lowering drugs']
        df_neph = df_a[neph]
        model_Neph = joblib.load(current_directory + "/model/rf_o_nep1.joblib")
        pred_proba_Neph = model_Neph.predict_proba(df_neph)[:, 1]
        chance_percent = f"{pred_proba_Neph[0] * 100:.2f}%"
        d_chance['Kidney Disease'] = f"Chance of development Kidney Disease: {chance_percent}"
        df_check = p[neph]
        if df_check.isnull().any().any():
            d_chance['Kidney Disease'] += " !!! Accuracy reduced due to insufficient data"
        print(pred_proba_Neph)

    if df_a.Dementia[0] == 0:
        dem = ['AlcoholLevel',
               'HeartRate',
               'BloodOxygenLevel',
               'BodyTemperature',
               'Weight(kg)',
               'MRI_Delay',
               'Age',
               'Education_Level',
               'Dominant_Hand',
               'Sex',
               'Family_Dementia_History',
               'Smoking',
               'APOE_ε4',
               'Physical_Activity',
               'Depression_Status',
               'Cognitive_Test_Scores',
               'Sleep_Quality',
               'Balanced Diet',
               'Low-Carb Diet',
               'Mediterranean Diet',
               'Donepezil',
               'Galantamine',
               'Memantine',
               'Rivastigmine']
        df_dem = df_a[dem]
        model_dem = joblib.load(current_directory + '/model/nn_dem.joblib')
        pred_proba_dem = model_dem.predict(df_dem).flatten()
        chance_percent = f"{pred_proba_dem[0] * 100:.2f}%"
        d_chance['Dementia'] = f"Chance of development Dementia: {chance_percent}"
        df_check = p[dem]
        if df_check.isnull().any().any():
            d_chance['Dementia'] += " !!! Accuracy reduced due to insufficient data"
        print(pred_proba_dem)

    if df_a.HeartDisease[0] == 0:
        heart = [
            'Smoking',
            'Drinking',
            'Stroke',
            'PhysicalHealth',
            'MentalHealth',
            'DiffWalking',
            'Sex',
            'Age',
            'Physical_Activity',
            'Sleep_Quality',
            'Asthma',
            'KidneyDisease',
            'SkinCancer',
            'American Indian/Alaskan Native',
            'Asian',
            'Black',
            'Hispanic',
            'Other',
            'White']
        df_heart = df_a[heart]
        model_heart = joblib.load(current_directory + "/model/rf_o_heart.joblib")
        pred_proba_heart = model_heart.predict_proba(df_heart)[:, 1]
        chance_percent = f"{pred_proba_heart[0] * 100:.2f}%"
        d_chance['Heart Disease'] = f"Chance of development Heart Disease: {chance_percent}"
        df_check = p[heart]
        if df_check.isnull().any().any():
            d_chance['Heart Disease'] += " !!! Accuracy reduced due to insufficient data"
        print(pred_proba_heart)

    if df_a.Stroke[0] == 0:
        stroke = [
            'HeartDisease',
            'Smoking',
            'Drinking',
            'PhysicalHealth',
            'MentalHealth',
            'DiffWalking',
            'Sex',
            'Age',
            'Physical_Activity',
            'Sleep_Quality',
            'Asthma',
            'KidneyDisease',
            'SkinCancer',
            'American Indian/Alaskan Native',
            'Asian',
            'Black',
            'Hispanic',
            'Other',
            'White']
        df_stroke = df_a[stroke]
        model_stroke = joblib.load(current_directory + "/model/rf_o_stroke.joblib")
        pred_proba_stroke = model_stroke.predict_proba(df_stroke)[:, 1]
        chance_percent = f"{pred_proba_stroke[0] * 100:.2f}%"
        d_chance['Stroke'] = f"Chance of development Stroke: {chance_percent}"
        df_check = p[stroke]
        if df_check.isnull().any().any():
            d_chance['Stroke'] += " !!! Accuracy reduced due to insufficient data"
        print(pred_proba_stroke)

    from reportlab.lib.pagesizes import letter
    from reportlab.pdfgen import canvas
    from io import BytesIO

    # Функция для создания PDF-файла с информацией о шансах развития заболеваний
    def create_pdf(data_dict):
        # Создание PDF-документа
        packet = BytesIO()
        c = canvas.Canvas(packet, pagesize=letter)

        # Настройка шрифта
        c.setFont("Helvetica", 12)

        # Начальная позиция для текста
        y_position = 750

        # Заголовок
        c.drawString(100, y_position, "Your risks of developing T2DM complications:")
        y_position -= 20

        # Перебор данных из словаря и добавление информации в PDF
        for disease, chance in data_dict.items():
            if chance is not None:
                c.drawString(100, y_position, chance)
                y_position -= 20

        # Сохранение PDF-файла
        c.save()
        packet.seek(0)
        output_file = BytesIO(packet.getvalue())
        output_file.name = 'Result.pdf'
        return output_file

    return create_pdf(d_chance)
