# relação de dias da semana que cada médico atende
cardiologista = {'terca', 'quarta'}
ortopedista = {'terca', 'quinta'}
dermatologista = {'segunda', 'quarta', 'sexta'}
neurologista = {'terca', 'quinta', 'sexta'}
psiquiatra = {'segunda', 'quarta', 'sexta'}
# Calcula quais os dias possíveis para dois médicos
def disp_dois_especialistas(medico01, medico02):
    return medico01.intersection(medico02)
# Calcula quais os dias possíveis para três médicos
def disp_tres_especialistas(medico01, medico02, medico03):
    teste = disp_dois_especialistas(medico01, medico02)
    return medico03.intersection(teste)
print(disp_dois_especialistas(neurologista, ortopedista))
print(disp_tres_especialistas(cardiologista, ortopedista, neurologista))