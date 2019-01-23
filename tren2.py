"""
==========================================
Control de un tren de cercanias
==========================================

* Antecedentes (Entradas)
   - `Sensor curva`
      * Conjunto difuso: No (muy lejos), lejos,cerca, muy cerca, en la curva
   - `Sensor estacion`
      * Conjunto difuso: No (muy lejos), lejos,cerca, muy cerca, en la estacion
   - `Velocidad`
      * Conjunto difuso: Detenido,lento,moderado,rapido, muy rapido
* Consecuentes (Salidas)
   - `Frenado`
      * Conjunto difuso: No, muy leve, leve, moderado, intenso, muy intenso
   - `Acelerar`
      * Conjunto difuso: No, muy leve, leve, moderado, intenso, muy intenso
"""
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl


# New Antecedent/Consequent objects hold universe variables and membership
# functions
curva = ctrl.Antecedent(np.arange(0, 1.1, 0.001), 'curva')
estacion = ctrl.Antecedent(np.arange(0, 1.1, 0.001), 'estacion')
velocidad = ctrl.Antecedent(np.arange(0,33.77, 0.001), 'velocidad') #m/S

frenado = ctrl.Consequent(np.arange(0, 2, 0.001), 'frenado')    #m/s^2
acelerar = ctrl.Consequent(np.arange(0, 1, 0.001), 'acelerar')  #m/s^2

curva['no'] = fuzz.trapmf(curva.universe, (0, 0, 0.1,0.5))
curva['muy lejos'] = fuzz.trapmf(curva.universe, (0.2,0.4,0.5,0.6))
curva['lejos'] = fuzz.trapmf(curva.universe,(0.5,0.6,0.65,0.75))  # 3 par->centro, 2 par ->pendiente, 1 par->ancho
curva['cerca'] = fuzz.trapmf(curva.universe,(0.68,0.75,0.84,0.89))
curva['muy cerca'] = fuzz.trapmf(curva.universe,(0.85,0.90,0.94,0.975))
curva['en la curva'] = fuzz.trapmf(curva.universe,(0.94,0.98,1.1,1.1))
#curva.view()

estacion['no'] = fuzz.trapmf(curva.universe, (0, 0, 0.1,0.5))
estacion['muy lejos']=fuzz.trapmf(curva.universe, (0.2,0.4,0.5,0.6))
estacion['lejos'] = fuzz.trapmf(curva.universe,(0.5,0.6,0.65,0.75))  # 3 par->centro, 2 par ->pendiente, 1 par->ancho
estacion['cerca'] = fuzz.trapmf(curva.universe,(0.68,0.75,0.84,0.89))
estacion['muy cerca'] = fuzz.trapmf(curva.universe,(0.85,0.90,0.96,1))
estacion['en la estacion'] = fuzz.trapmf(curva.universe,(0.96,0.99,1.1,1.1))
#estacion.view()
velocidad['detenido']=fuzz.trapmf(velocidad.universe, (0, 0, 0.5,2))  #0 0 0.1 0.2
velocidad['muy lento']=fuzz.trapmf(velocidad.universe, (1,5,8.66,11.33)) # 0.3 .....
velocidad['lento']= fuzz.trapmf(velocidad.universe, (7.66, 11.66,14.66, 17.5))
velocidad['moderado']=fuzz.trapmf(velocidad.universe, (15.11, 17.5, 20.5, 22.5))
velocidad['rapido']= fuzz.trapmf(velocidad.universe, (20.5, 22.5, 24.7,27.27))
velocidad['muy rapido']= fuzz.trapmf(velocidad.universe, (24.7, 27.27, 33.77,33.77))
#velocidad.view()
frenado['no']= fuzz.trapmf(frenado.universe, (0,0,0.01,0.01))
frenado['leve']=fuzz.trapmf(frenado.universe, (-0.08,0.2,0.4,0.6))
frenado['moderado']= fuzz.trapmf(frenado.universe,(0.4,0.6,0.9,1.2))
frenado['intenso']= fuzz.trapmf(frenado.universe,(0.9,1.2,1.5,1.8))
frenado['muy intenso']= fuzz.trapmf(frenado.universe, (1.5,1.8,2,2))
#frenado.view()
acelerar['no']= fuzz.trapmf(acelerar.universe, (0,0,0.01,0.01))
acelerar['leve']=fuzz.trapmf(acelerar.universe, (-0.115,0.07,0.115,0.142))
acelerar['moderado']= fuzz.trapmf(acelerar.universe,(0.1,0.21,0.36,0.5))
acelerar['intenso']= fuzz.trapmf(acelerar.universe,(0.36,0.5,0.71,0.86))
acelerar['muy intenso']=fuzz.trapmf(acelerar.universe,(0.71,0.86,1,1))
#acelerar.view()
#"""
rule1 = ctrl.Rule(curva['no'] & estacion['no'] & velocidad['detenido'], (acelerar['moderado'], frenado['no']))
rule2 = ctrl.Rule(curva['no'] & estacion['no'] & velocidad['muy lento'], (acelerar['intenso'], frenado['no']))
rule3 = ctrl.Rule(curva['no'] & estacion['no'] & velocidad['lento'], (acelerar['intenso'], frenado['no']))
rule4 = ctrl.Rule(curva['no'] & estacion['no'] & velocidad['moderado'], (acelerar['muy intenso'], frenado['no']))
rule5 = ctrl.Rule(curva['no'] & estacion['no'] & velocidad['rapido'], (acelerar['muy intenso'], frenado['no']))
rule6 = ctrl.Rule(curva['no'] & estacion['no'] & velocidad['muy rapido'], (acelerar['no'], frenado['no']))

rule7 = ctrl.Rule((curva['muy lejos'] & estacion['no']) & velocidad['muy rapido'], (acelerar['no'], frenado['leve']))
rule8 = ctrl.Rule((curva['muy lejos'] & estacion['no']) & velocidad['rapido'], (acelerar['no'], frenado['no']))
rule9 = ctrl.Rule((curva['muy lejos'] & estacion['no']) & velocidad['moderado'], (acelerar['muy intenso'], frenado['no']))   #acelrar->intenso
rule10 = ctrl.Rule((curva['muy lejos'] & estacion['no']) & velocidad['lento'], (acelerar['intenso'], frenado['no']))   #acelerar ->moderado

rule11 = ctrl.Rule((curva['lejos'] & estacion['no']) & velocidad['muy rapido'], (acelerar['no'], frenado['leve']))
rule12= ctrl.Rule((curva['lejos'] & estacion['no']) & velocidad['rapido'], (acelerar['no'], frenado['leve']))
rule13 = ctrl.Rule((curva['lejos'] & estacion['no']) & velocidad['moderado'], (acelerar['intenso'], frenado['no']))   #6 intenso
rule14= ctrl.Rule((curva['lejos'] & estacion['no']) & velocidad['lento'], (acelerar['intenso'], frenado['no']))    #6  moderado

rule15=ctrl.Rule((curva['cerca'] & estacion['no']) & velocidad['rapido'], (acelerar['no'], frenado['leve']))
rule16=ctrl.Rule((curva['cerca'] & estacion['no']) & velocidad['muy rapido'], (acelerar['no'], frenado['moderado']))
rule17 = ctrl.Rule((curva['cerca'] & estacion['no']) & velocidad['moderado'], (acelerar['no'], frenado['no']))
rule18 = ctrl.Rule((curva['cerca'] & estacion['no']) & velocidad['lento'], (acelerar['leve'], frenado['no']))

rule19 = ctrl.Rule(curva['muy cerca'] & estacion['no'] & velocidad['moderado'], (acelerar['no'], frenado['moderado']))
rule20 = ctrl.Rule(curva['muy cerca'] & estacion['no'] & velocidad['lento'], (acelerar['no'], frenado['leve']))
rule21 = ctrl.Rule(curva['muy cerca'] & estacion['no'] & velocidad['rapido'], (acelerar['no'], frenado['intenso']))

rule22=ctrl.Rule(curva['en la curva'] & estacion['no'] & velocidad['lento'], (acelerar['no'], frenado['no']))

rule23 = ctrl.Rule(curva['no'] & estacion['muy lejos'] & velocidad['moderado'], (acelerar['moderado'], frenado['no']))
rule24 = ctrl.Rule(curva['no'] & estacion['muy lejos'] & velocidad['lento'], (acelerar['leve'], frenado['no']))
rule25 = ctrl.Rule(curva['no'] & estacion['muy lejos'] & velocidad['rapido'], (acelerar['no'], frenado['leve']))
rule26 = ctrl.Rule(curva['no'] & estacion['muy lejos'] & velocidad['muy rapido'], (acelerar['no'], frenado['moderado']))

rule27 = ctrl.Rule(curva['no'] & estacion['lejos'] & velocidad['moderado'], (acelerar['intenso'], frenado['no']))   #moderado
rule28 = ctrl.Rule(curva['no'] & estacion['lejos'] & velocidad['lento'], (acelerar['moderado'], frenado['no']))             #leve
rule29 = ctrl.Rule(curva['no'] & estacion['lejos'] & velocidad['rapido'], (acelerar['no'], frenado['moderado']))    #leve
rule30 = ctrl.Rule(curva['no'] & estacion['lejos'] & velocidad['muy rapido'], (acelerar['no'], frenado['moderado']))  #leve


rule31 = ctrl.Rule(curva['no'] & estacion['cerca'] & velocidad['moderado'], (acelerar['no'], frenado['moderado']))   #no no
rule32 = ctrl.Rule(curva['no'] & estacion['cerca'] & velocidad['lento'], (acelerar['leve'], frenado['no']))
rule33 = ctrl.Rule(curva['no'] & estacion['cerca'] & velocidad['rapido'], (acelerar['no'], frenado['moderado']))
rule34 = ctrl.Rule(curva['no'] & estacion['cerca'] & velocidad['muy rapido'], (acelerar['no'], frenado['intenso']))

rule35 = ctrl.Rule(curva['no'] & estacion['muy cerca'] & velocidad['moderado'], (acelerar['no'], frenado['moderado']))  #intenso
rule36 = ctrl.Rule(curva['no'] & estacion['muy cerca'] & velocidad['lento'], (acelerar['no'], frenado['moderado']))   #leve
rule37 = ctrl.Rule(curva['no'] & estacion['muy cerca'] & velocidad['rapido'], (acelerar['no'], frenado['intenso']))  #muy intenso

#rule38=ctrl.Rule(curva['no'] & estacion['en la estacion'] & velocidad['lento'], (acelerar['no'], frenado['intenso']))  #frenado muy intenso
rule39=ctrl.Rule(curva['muy lejos'] & estacion['muy cerca'] & velocidad['detenido'], (acelerar['no'], frenado['leve']))   #frenado insenso

rule40=ctrl.Rule(curva['muy lejos'] & estacion['en la estacion'] & velocidad['detenido'], (acelerar['no'], frenado['leve']))
rule41=ctrl.Rule(curva['muy lejos'] & estacion['no'] & velocidad['detenido'], (acelerar['moderado'], frenado['no']))
rule42=ctrl.Rule(curva['muy lejos'] & estacion['no'] & velocidad['muy lento'], (acelerar['intenso'], frenado['no']))

#rule43=ctrl.Rule(curva['muy lejos'] & estacion['en la estacion'] & velocidad['detenido'], (acelerar['no'], frenado['no']))
rule44=ctrl.Rule(curva['muy lejos'] & estacion['en la estacion'] & velocidad['muy lento'], (acelerar['no'], frenado['moderado']))
rule38=ctrl.Rule(curva['muy lejos'] & estacion['muy cerca'] & velocidad['muy lento'], (acelerar['no'], frenado['leve']))


tipping_ctrl = ctrl.ControlSystem([rule1,rule2,rule3,rule4,rule5,rule6,rule7,rule8,rule9,rule10,
                                   rule11,rule12,rule13,rule14,rule15,rule16,rule17,rule18,rule18,rule18,rule19,rule20,
                                   rule21,rule22,rule23,rule24,rule25,rule26,rule27,rule28,rule29,rule30,rule31,rule32,rule33,
                                   rule34,rule35,rule36,rule37,rule38,rule44,rule41,rule42,rule39,rule40
                                   ])
tipping = ctrl.ControlSystemSimulation(tipping_ctrl)

def calculate(c,e,v):
    
    tipping.input['curva'] = c
    tipping.input['estacion'] = e
    tipping.input['velocidad'] = v
    tipping.compute()
    #frenado.view(sim=tipping)
    #acelerar.view(sim=tipping)
    return tipping.output['acelerar'],tipping.output['frenado']
"""
distance=2730
vel=0
r=0

while(r<distance):
    c=r/distance
    #e=r/distance*2
    #if e>1:
    #    e=0
    a,b=calculate(c,0,vel)
    vel=vel+a-b
    print("velocidad: "+str(vel))
    #print("recorrido: "+str(r))
    #print("estacion: "+str(ecls))
    print("curva: "+str(c))
    print("aceleracion: "+str(a))
    print("frenado: "+str(b))
    r+=vel
    #print(r)

r=0
distance1=distance/2
while (r<distance):
    c=r/distance
    e=r/(distance1+7)
    if r>distance1+7:
        print("yes")
        e=0
        break
    #if e>1:
    #    e=0
    a,b=calculate(c,e,vel)
    vel=vel+a-b
    if vel<0:
        print("no")
        vel=0
    print("velocidad: "+str(vel))
    #print("recorrido: "+str(r))
    print("estacion: "+str(e))
    print("curva: "+str(c))
    print("aceleracion: "+str(a))
    print("frenado: "+str(b))
    r+=vel
    """
   