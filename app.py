'''
Created on May 25, 2021

@author: 869259
'''
'''
intent of code is for recommending frequently sold options for a selected product
input params:
productcode, market, frequency
if running in local - set medium param in pythonconfig.ini - medium=local
if running in webapp - set medium param in pythonconfig.ini - medium=db
set configurable params in pythonconfig.ini
output:
for success scenario - return apriori result set
for failure scenario - return status,msg

'''

from flask import Flask,request,jsonify
from apriori import get_recommendation,get_recommendation_test
import pandas as pd

app=Flask(__name__)
app.config['JSON_SORT_KEYS']=False

@app.route('/testme')
def home():
    return 'success'

@app.route('/simulate',methods=['POST'])
def recommend():
    df_result=get_recommendation(request)
    return df_result
#     return(jsonify(df_result.to_json(orient='records')))
#     return recommendation(request)

@app.route('/simulatestub',methods=['POST'])
def recommend_stub():
    status=get_recommendation_test(request)
    test_dict={"ID":"2bdacb9e-1eaf-4f85-b20f-d6e6bfef8816","Product_Code":"712034","Options":"NRDN215","Option_Name":"SkyPlate Infrastructure Kit","Total_WRP":"5000.0","Support":"0.9821428571428571","Length":"1"}
#     test_dict={"ID":"f37f507a-fbf1-4d9b-beb0-daae3ab722ae","Product_Code":"712034","Options":"NRDN215","Option_Name":"SkyPlateInfrastructureKit","Total_WRP":"5000.0","Support":"0.9133858267716536","Length":"1"},{"ID":"f37f507a-fbf1-4d9b-beb0-daae3ab722ae","Product_Code":"712034","Options":"NRDN544","Option_Name":"DiDiC90HighPerform.Room","Total_WRP":"52000.0","Support":"0.8372703412073491","Length":"1"},{"ID":"f37f507a-fbf1-4d9b-beb0-daae3ab722ae","Product_Code":"712034","Options":"NRDN421","Option_Name":"StretchgripforVS/VMstand","Total_WRP":"749.0","Support":"0.8136482939632546","Length":"1"},{"ID":"f37f507a-fbf1-4d9b-beb0-daae3ab722ae","Product_Code":"712034","Options":"NRDN544,NRDN215","Option_Name":"DiDiC90HighPerform.Room,SkyPlateInfrastructureKit","Total_WRP":"57000.0","Support":"0.800524934383202","Length":"2"},{"ID":"f37f507a-fbf1-4d9b-beb0-daae3ab722ae","Product_Code":"712034","Options":"NRDN421,NRDN215","Option_Name":"StretchgripforVS/VMstand,SkyPlateInfrastructureKit","Total_WRP":"5749.0","Support":"0.7926509186351706","Length":"2"},{"ID":"f37f507a-fbf1-4d9b-beb0-daae3ab722ae","Product_Code":"712034","Options":"NRDN544,NRDN421","Option_Name":"DiDiC90HighPerform.Room,StretchgripforVS/VMstand","Total_WRP":"52749.0","Support":"0.7795275590551181","Length":"2"},{"ID":"f37f507a-fbf1-4d9b-beb0-daae3ab722ae","Product_Code":"712034","Options":"NRDN544,NRDN421,NRDN215","Option_Name":"DiDiC90HighPerform.Room,StretchgripforVS/VMstand,SkyPlateInfrastructureKit","Total_WRP":"57749.0","Support":"0.7585301837270341","Length":"3"},{"ID":"f37f507a-fbf1-4d9b-beb0-daae3ab722ae","Product_Code":"712034","Options":"NRDN191","Option_Name":"VarioFocus","Total_WRP":"739.0","Support":"0.7139107611548556","Length":"1"},{"ID":"f37f507a-fbf1-4d9b-beb0-daae3ab722ae","Product_Code":"712034","Options":"NRDN209","Option_Name":"LargeSkyPlateSet","Total_WRP":"45000.0","Support":"0.7086614173228346","Length":"1"},{"ID":"f37f507a-fbf1-4d9b-beb0-daae3ab722ae","Product_Code":"712034","Options":"NRDN209,NRDN215","Option_Name":"LargeSkyPlateSet,SkyPlateInfrastructureKit","Total_WRP":"50000.0","Support":"0.7086614173228346","Length":"2"},{"ID":"f37f507a-fbf1-4d9b-beb0-daae3ab722ae","Product_Code":"712034","Options":"NRDN544,NRDN518","Option_Name":"DiDiC90HighPerform.Room,LiveCameraPackage","Total_WRP":"61585.0","Support":"0.6902887139107612","Length":"2"},{"ID":"f37f507a-fbf1-4d9b-beb0-daae3ab722ae","Product_Code":"712034","Options":"NRDN518","Option_Name":"LiveCameraPackage","Total_WRP":"9585.0","Support":"0.6902887139107612","Length":"1"},{"ID":"f37f507a-fbf1-4d9b-beb0-daae3ab722ae","Product_Code":"712034","Options":"NRDN250","Option_Name":"AutomaticImageStitching","Total_WRP":"4382.0","Support":"0.6850393700787402","Length":"1"},{"ID":"f37f507a-fbf1-4d9b-beb0-daae3ab722ae","Product_Code":"712034","Options":"NRDN209,NRDN421,NRDN215","Option_Name":"LargeSkyPlateSet,StretchgripforVS/VMstand,SkyPlateInfrastructureKit","Total_WRP":"50749.0","Support":"0.6719160104986877","Length":"3"},{"ID":"f37f507a-fbf1-4d9b-beb0-daae3ab722ae","Product_Code":"712034","Options":"NRDN209,NRDN421","Option_Name":"LargeSkyPlateSet,StretchgripforVS/VMstand","Total_WRP":"45749.0","Support":"0.6719160104986877","Length":"2"},{"ID":"f37f507a-fbf1-4d9b-beb0-daae3ab722ae","Product_Code":"712034","Options":"NRDN544,NRDN209","Option_Name":"DiDiC90HighPerform.Room,LargeSkyPlateSet","Total_WRP":"97000.0","Support":"0.6692913385826772","Length":"2"},{"ID":"f37f507a-fbf1-4d9b-beb0-daae3ab722ae","Product_Code":"712034","Options":"NRDN544,NRDN209,NRDN215","Option_Name":"DiDiC90HighPerform.Room,LargeSkyPlateSet,SkyPlateInfrastructureKit","Total_WRP":"102000.0","Support":"0.6692913385826772","Length":"3"},{"ID":"f37f507a-fbf1-4d9b-beb0-daae3ab722ae","Product_Code":"712034","Options":"NRDN544,NRDN518,NRDN215","Option_Name":"DiDiC90HighPerform.Room,LiveCameraPackage,SkyPlateInfrastructureKit","Total_WRP":"66585.0","Support":"0.6640419947506562","Length":"3"},{"ID":"f37f507a-fbf1-4d9b-beb0-daae3ab722ae","Product_Code":"712034","Options":"NRDN518,NRDN215","Option_Name":"LiveCameraPackage,SkyPlateInfrastructureKit","Total_WRP":"14585.0","Support":"0.6640419947506562","Length":"2"},{"ID":"f37f507a-fbf1-4d9b-beb0-daae3ab722ae","Product_Code":"712034","Options":"NRDN544,NRDN518,NRDN421","Option_Name":"DiDiC90HighPerform.Room,LiveCameraPackage,StretchgripforVS/VMstand","Total_WRP":"62334.0","Support":"0.6509186351706037","Length":"3"},{"ID":"f37f507a-fbf1-4d9b-beb0-daae3ab722ae","Product_Code":"712034","Options":"NRDN191,NRDN215","Option_Name":"VarioFocus,SkyPlateInfrastructureKit","Total_WRP":"5739.0","Support":"0.6509186351706037","Length":"2"},{"ID":"f37f507a-fbf1-4d9b-beb0-daae3ab722ae","Product_Code":"712034","Options":"NRDN518,NRDN421","Option_Name":"LiveCameraPackage,StretchgripforVS/VMstand","Total_WRP":"10334.0","Support":"0.6509186351706037","Length":"2"},{"ID":"f37f507a-fbf1-4d9b-beb0-daae3ab722ae","Product_Code":"712034","Options":"NRDN544,NRDN191","Option_Name":"DiDiC90HighPerform.Room,VarioFocus","Total_WRP":"52739.0","Support":"0.6456692913385826","Length":"2"},{"ID":"f37f507a-fbf1-4d9b-beb0-daae3ab722ae","Product_Code":"712034","Options":"NRDN513","Option_Name":"DigitalVSExt.FixDetector","Total_WRP":"96414.0","Support":"0.6430446194225722","Length":"1"},{"ID":"f37f507a-fbf1-4d9b-beb0-daae3ab722ae","Product_Code":"712034","Options":"NRDN544,NRDN513","Option_Name":"DiDiC90HighPerform.Room,DigitalVSExt.FixDetector","Total_WRP":"148414.0","Support":"0.6430446194225722","Length":"2"},{"ID":"f37f507a-fbf1-4d9b-beb0-daae3ab722ae","Product_Code":"712034","Options":"NRDN544,NRDN209,NRDN421,NRDN215","Option_Name":"DiDiC90HighPerform.Room,LargeSkyPlateSet,StretchgripforVS/VMstand,SkyPlateInfrastructureKit","Total_WRP":"102749.0","Support":"0.6377952755905512","Length":"4"},{"ID":"f37f507a-fbf1-4d9b-beb0-daae3ab722ae","Product_Code":"712034","Options":"NRDN544,NRDN209,NRDN421","Option_Name":"DiDiC90HighPerform.Room,LargeSkyPlateSet,StretchgripforVS/VMstand","Total_WRP":"97749.0","Support":"0.6377952755905512","Length":"3"},{"ID":"f37f507a-fbf1-4d9b-beb0-daae3ab722ae","Product_Code":"712034","Options":"NRDN191,NRDN421","Option_Name":"VarioFocus,StretchgripforVS/VMstand","Total_WRP":"1488.0","Support":"0.6351706036745407","Length":"2"},{"ID":"f37f507a-fbf1-4d9b-beb0-daae3ab722ae","Product_Code":"712034","Options":"NRDN518,NRDN421,NRDN215","Option_Name":"LiveCameraPackage,StretchgripforVS/VMstand,SkyPlateInfrastructureKit","Total_WRP":"15334.0","Support":"0.6325459317585301","Length":"3"},{"ID":"f37f507a-fbf1-4d9b-beb0-daae3ab722ae","Product_Code":"712034","Options":"NRDN544,NRDN518,NRDN421,NRDN215","Option_Name":"DiDiC90HighPerform.Room,LiveCameraPackage,StretchgripforVS/VMstand,SkyPlateInfrastructureKit","Total_WRP":"67334.0","Support":"0.6325459317585301","Length":"4"},{"ID":"f37f507a-fbf1-4d9b-beb0-daae3ab722ae","Product_Code":"712034","Options":"NRDN422","Option_Name":"PatientSupportForStitching","Total_WRP":"5323.0","Support":"0.6299212598425197","Length":"1"},{"ID":"f37f507a-fbf1-4d9b-beb0-daae3ab722ae","Product_Code":"712034","Options":"NRDN422,NRDN250","Option_Name":"PatientSupportForStitching,AutomaticImageStitching","Total_WRP":"9705.0","Support":"0.6272965879265092","Length":"2"},{"ID":"f37f507a-fbf1-4d9b-beb0-daae3ab722ae","Product_Code":"712034","Options":"NRDN250,NRDN215","Option_Name":"AutomaticImageStitching,SkyPlateInfrastructureKit","Total_WRP":"9382.0","Support":"0.6246719160104987","Length":"2"},{"ID":"f37f507a-fbf1-4d9b-beb0-daae3ab722ae","Product_Code":"712034","Options":"NRDN544,NRDN191,NRDN215","Option_Name":"DiDiC90HighPerform.Room,VarioFocus,SkyPlateInfrastructureKit","Total_WRP":"57739.0","Support":"0.6194225721784777","Length":"3"},{"ID":"f37f507a-fbf1-4d9b-beb0-daae3ab722ae","Product_Code":"712034","Options":"NRDN191,NRDN421,NRDN215","Option_Name":"VarioFocus,StretchgripforVS/VMstand,SkyPlateInfrastructureKit","Total_WRP":"6488.0","Support":"0.6194225721784777","Length":"3"},{"ID":"f37f507a-fbf1-4d9b-beb0-daae3ab722ae","Product_Code":"712034","Options":"NRDN544,NRDN513,NRDN215","Option_Name":"DiDiC90HighPerform.Room,DigitalVSExt.FixDetector,SkyPlateInfrastructureKit","Total_WRP":"153414.0","Support":"0.6089238845144357","Length":"3"},{"ID":"f37f507a-fbf1-4d9b-beb0-daae3ab722ae","Product_Code":"712034","Options":"NRDN513,NRDN215","Option_Name":"DigitalVSExt.FixDetector,SkyPlateInfrastructureKit","Total_WRP":"101414.0","Support":"0.6089238845144357","Length":"2"},{"ID":"f37f507a-fbf1-4d9b-beb0-daae3ab722ae","Product_Code":"712034","Options":"NRDN513,NRDN421","Option_Name":"DigitalVSExt.FixDetector,StretchgripforVS/VMstand","Total_WRP":"97163.0","Support":"0.6062992125984252","Length":"2"},{"ID":"f37f507a-fbf1-4d9b-beb0-daae3ab722ae","Product_Code":"712034","Options":"NRDN544,NRDN513,NRDN421","Option_Name":"DiDiC90HighPerform.Room,DigitalVSExt.FixDetector,StretchgripforVS/VMstand","Total_WRP":"149163.0","Support":"0.6062992125984252","Length":"3"},{"ID":"f37f507a-fbf1-4d9b-beb0-daae3ab722ae","Product_Code":"712034","Options":"NRDN544,NRDN191,NRDN421","Option_Name":"DiDiC90HighPerform.Room,VarioFocus,StretchgripforVS/VMstand","Total_WRP":"53488.0","Support":"0.6036745406824147","Length":"3"},{"ID":"f37f507a-fbf1-4d9b-beb0-daae3ab722ae","Product_Code":"712034","Options":"NDCC221","Option_Name":"ClinicalQC","Total_WRP":"1833.0","Support":"0.6010498687664042","Length":"1"}
    df_result=pd.DataFrame([test_dict], columns=test_dict.keys())
    return(jsonify(df_result.to_json(orient='records')))
    
@app.route('/marketstub',methods=['POST'])
def market_stub():
#     status=get_recommendation_test(request)
    test_dict={"market1":"APAC","market2":"Benelux","market3":"Central Europe", "market4":"DACH", "market5":"France", "market6":"Greater China"}
    df_result=pd.DataFrame([test_dict], columns=test_dict.keys())
    return(jsonify(df_result.to_json(orient='records')))

@app.route('/productstub',methods=['POST'])
def product_stub():
#     status=get_recommendation_test(request)
    test_dict={"product1":"712033","product2":"712034","product3":"712214", "product4":"712035", "product5":"712202", "product6":"712203"}
    df_result=pd.DataFrame([test_dict], columns=test_dict.keys())
    return(jsonify(df_result.to_json(orient='records')))

if __name__=='__main__':
    app.run(debug=True)
