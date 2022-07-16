class Medico:
    def __init__(self, nome, crm, especialidades):
        self.__nome = nome
        self.__crm = crm
        self.__especialidades = especialidades

    def get_nome(self):
        return self.__nome

    def get_crm(self):
        return self.__crm

    def get_especialidades(self):
        return self.__especialidades

    def fazer_residencia(self, residencia, especialidade):
        if residencia:
            self.__especialidades.append(especialidade)


medico = Medico('Antenor', '123456789', ['A', 'B', 'C'])
medico.fazer_residencia(True, 'D')

print(f'Nome do medico - {medico.get_nome()} - CRM: {medico.get_crm()} - especialidades: {medico.get_especialidades()}')

