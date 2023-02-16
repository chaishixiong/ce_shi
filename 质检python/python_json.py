from flask import Flask
from flask import jsonify
from 质检python import switch_insulation
from 质检python import switch_normal
from 质检python import switch_heat
from 质检python import shoe_aromatic_amine
from 质检python import shoe_abrasion
from 质检python import shoe_sign
from 质检python import cloth_soap
from 质检python import cloth_ph
from 质检python import cloth_water
import warnings
warnings.filterwarnings('ignore')
import json


app = Flask(__name__)

# 开关绝缘材料
def switch_insulation_material():


    df = switch_insulation.load_data()
    # x_train, y_train, x_test, y_test, x_pred, y_pred, last_month, last_value\
    #     , now_month, now_value, pred_month, pred_value= switch_insulation.XGBoost(df)
    # print(x_train)
    y_train, y_test, y_pred, last_month, last_value\
        , now_month, now_value, pred_month, pred_value, x= switch_insulation.XGBoost(df)

    json_data = {
        'echartsone': {

            'y_train': y_train,
    },
        'echartstwo': {

            'y_test': y_test,
        },
        'echartsthree': {
            'x_pred': x,
            'y_pred': y_pred,
        },
        'last_month': last_month,
        'last_value': last_value,
        'now_month': now_month,
        'now_value': now_value,
        'pred_month': pred_month,
        'pred_value': pred_value
    }
    return json_data

# 开关正常操作
def switch_normal_generation():


    df = switch_normal.load_data()
    # x_train, y_train, x_test, y_test, x_pred, y_pred, last_month, last_value\
    #     , now_month, now_value, pred_month, pred_value= switch_normal.XGBoost(df)
    # print(x_train)

    y_train, y_test, y_pred, last_month, last_value\
        , now_month, now_value, pred_month, pred_value, x= switch_normal.XGBoost(df)

    json_data = {
        'echartsone': {

            'y_train': y_train,
    },
        'echartstwo': {

            'y_test': y_test,
        },
        'echartsthree': {
            'x_pred': x,
            'y_pred': y_pred,
        },
        'last_month': last_month,
        'last_value': last_value,
        'now_month': now_month,
        'now_value': now_value,
        'pred_month': pred_month,
        'pred_value': pred_value
    }
    return json_data

# 开关耐热
def switch_heat_resist():


    df = switch_heat.load_data()
    # x_train, y_train, x_test, y_test, x_pred, y_pred\
    #     , now_month, now_value, pred_month, pred_value, standard_date, standard_value_list, standard_value= switch_heat.XGBoost(df)
    y_train, y_test, y_pred\
        , now_month, now_value, pred_month, pred_value, standard_date, standard_value_list, standard_value= switch_heat.XGBoost(df)

    json_data = {

        'x': standard_date,

        'echartsone': {

            'y_train': y_train,
    },
        'echartstwo': {

            'y_test': y_test,
        },
        'echartsthree': {

            'y_pred': y_pred,
        },
        'echartsfour': {

            'y_standard': standard_value_list,
        },
        'now_month': now_month,
        'now_value': now_value,
        'pred_month': pred_month,
        'pred_value': pred_value,
        'standard_value': standard_value,
        'sign': '<='
    }
    return json_data


# 皮鞋有害芳香胺
def shoe_harmful_aromatic_amine():


    df = shoe_aromatic_amine.load_data()
    # x_train, y_train, x_test, y_test, x_pred, y_pred, last_month, last_value\
    #     , now_month, now_value, pred_month, pred_value= shoe_aromatic_amine.XGBoost(df)
    # print(x_train)

    y_train, y_test, y_pred, last_month, last_value\
        , now_month, now_value, pred_month, pred_value, x= shoe_aromatic_amine.XGBoost(df)

    json_data = {
        'echartsone': {

            'y_train': y_train,
    },
        'echartstwo': {

            'y_test': y_test,
        },
        'echartsthree': {
            'x_pred': x,
            'y_pred': y_pred,
        },
        'last_month': last_month,
        'last_value': last_value,
        'now_month': now_month,
        'now_value': now_value,
        'pred_month': pred_month,
        'pred_value': pred_value
    }
    return json_data


# 皮鞋外底耐磨性能
def shoe_abrasion_resist():


    df = shoe_abrasion.load_data()
    # x_train, y_train, x_test, y_test, x_pred, y_pred \
    #     , now_month, now_value, pred_month, pred_value, standard_date, standard_value_list, standard_value = switch_heat.XGBoost(df)
    # print(x_train)

    y_train, y_test, y_pred\
        , now_month, now_value, pred_month, pred_value, standard_date, standard_value_list, standard_value= shoe_abrasion.XGBoost(df)


    json_data = {
        'echartsone': {
            'y_train': y_train,
    },
        'echartstwo': {
            'y_test': y_test,
        },
        'echartsthree': {
            'y_pred': y_pred,
        },
        'echartsfour': {
            'x_standard': standard_date,
            'y_standard': standard_value_list,
        },
        'now_month': now_month,
        'now_value': now_value,
        'pred_month': pred_month,
        'pred_value': pred_value,
        'standard_value': standard_value,
        'sign': '<='
    }
    return json_data


# 皮鞋标识
def shoe_sign_recognize():


    df = shoe_sign.load_data()
    # x_train, y_train, x_test, y_test, x_pred, y_pred, last_month, last_value\
    #     , now_month, now_value, pred_month, pred_value= shoe_sign.XGBoost(df)
    # print(x_train)

    y_train, y_test, y_pred, last_month, last_value\
        , now_month, now_value, pred_month, pred_value, x = shoe_sign.XGBoost(df)

    json_data = {
        'echartsone': {

            'y_train': y_train,
    },
        'echartstwo': {

            'y_test': y_test,
        },
        'echartsthree': {
            'x_pred': x,
            'y_pred': y_pred,
        },
        'last_month': last_month,
        'last_value': last_value,
        'now_month': now_month,
        'now_value': now_value,
        'pred_month': pred_month,
        'pred_value': pred_value
    }
    return json_data


# 校服耐皂洗色牢度（级）
def cloth_soap_wash():


    df = cloth_soap.load_data()
    # x_train, y_train, x_test, y_test, x_pred, y_pred, last_month, last_value\
    #     , now_month, now_value, pred_month, pred_value= cloth_soap.XGBoost(df)
    # print(x_train)
    y_train, y_test, y_pred, last_month, last_value\
        , now_month, now_value, pred_month, pred_value, x = cloth_soap.XGBoost(df)

    json_data = {
        'echartsone': {

            'y_train': y_train,
    },
        'echartstwo': {

            'y_test': y_test,
        },
        'echartsthree': {
            'x_pred': x,
            'y_pred': y_pred,
        },
        'last_month': last_month,
        'last_value': last_value,
        'now_month': now_month,
        'now_value': now_value,
        'pred_month': pred_month,
        'pred_value': pred_value
    }
    return json_data


# 校服ph
def cloth_ph_value():


    df = cloth_ph.load_data()
    # x_train, y_train, x_test, y_test, x_pred, y_pred\
    #     , now_month, now_value, pred_month, pred_value, standard_value1_list, standard_value1\
    #     , standard_date, standard_value2_list, standard_value2 = cloth_ph.XGBoost(df)
    # print(x_train)

    y_train, y_test, y_pred\
        , now_month, now_value, pred_month, pred_value, standard_date, standard_value1_list, standard_value1\
        , standard_value2_list, standard_value2 = cloth_ph.XGBoost(df)


    json_data = {
        'echartsone': {

            'y_train': y_train,
    },
        'echartstwo': {

            'y_test': y_test,
        },
        'echartsthree': {

            'y_pred': y_pred,
        },
        'echartsfour': {
            'x_standard': standard_date,
            'y_standard1': standard_value1_list,
        },
        'echartsfive': {

            'y_standard2': standard_value2_list,
        },
        'now_month': now_month,
        'now_value': now_value,
        'pred_month': pred_month,
        'pred_value': pred_value,
        'standard_value1': standard_value1,
        'standard_value2': standard_value2
    }
    return json_data


# 校服耐水色牢度（级）
def cloth_water_wash():


    df = cloth_water.load_data()
    # x_train, y_train, x_test, y_test, x_pred, y_pred, last_month, last_value\
    #     , now_month, now_value, pred_month, pred_value= cloth_water.XGBoost(df)
    # print(x_train)
    y_train, y_test, y_pred, last_month, last_value\
        , now_month, now_value, pred_month, pred_value, x = cloth_water.XGBoost(df)

    json_data = {
        'echartsone': {

            'y_train': y_train,
    },
        'echartstwo': {

            'y_test': y_test,
        },
        'echartsthree': {
            'x_pred': x,
            'y_pred': y_pred,
        },
        'last_month': last_month,
        'last_value': last_value,
        'now_month': now_month,
        'now_value': now_value,
        'pred_month': pred_month,
        'pred_value': pred_value
    }
    return json_data



# 开关绝缘材料
@app.route('/switchInsulationMaterial', methods=['GET'])
def get_switch_insulation_material():
    # usr = [user for user in users if (user['id'] == userId)]
    return jsonify(switch_insulation_material())


# 开关正常操作
@app.route('/switchNormalGeneration', methods=['GET'])
def get_switch_normal_generation():
    # usr = [user for user in users if (user['id'] == userId)]
    return jsonify(switch_normal_generation())


# 开关耐热
@app.route('/switchHeatResist', methods=['GET'])
def get_switch_heat_resist():
    # usr = [user for user in users if (user['id'] == userId)]
    return jsonify(switch_heat_resist())


# 皮鞋有害芳香胺
@app.route('/shoeAromaticAmine', methods=['GET'])
def get_shoe_harmful_aromatic_amine():
    # usr = [user for user in users if (user['id'] == userId)]
    return jsonify(shoe_harmful_aromatic_amine())



# 皮鞋外底耐磨性能
@app.route('/shoeAbrasionResist', methods=['GET'])
def get_shoe_abrasion_resist():
    # usr = [user for user in users if (user['id'] == userId)]
    return jsonify(shoe_abrasion_resist())


# 皮鞋重金属含量
@app.route('/shoeSignRecognize', methods=['GET'])
def get_shoe_sign_recognize():
    # usr = [user for user in users if (user['id'] == userId)]
    return jsonify(shoe_sign_recognize())


# 耐皂洗色牢度（级
@app.route('/clothSoapWash', methods=['GET'])
def get_cloth_soap_wash():
    # usr = [user for user in users if (user['id'] == userId)]
    return jsonify(cloth_soap_wash())


# 校服ph值
@app.route('/clothPhValue', methods=['GET'])
def get_cloth_ph_value():
    # usr = [user for user in users if (user['id'] == userId)]
    return jsonify(cloth_ph_value())


# 耐水色牢度（级）
@app.route('/clothWaterWash', methods=['GET'])
def get_cloth_water_wash():
    # usr = [user for user in users if (user['id'] == userId)]
    return jsonify(cloth_water_wash())


# 也可以自定义其他的方法

# 设定监听端口为3307
if __name__ == '__main__':
    app.run(host='localhost', port=3307)
