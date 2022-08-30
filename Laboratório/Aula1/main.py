"""
Module containing all the code for the Aula1 lesson.
"""

from typing import List


class Pessoa():
    """
    Class to represent a person.

    Attributes
    -----------
    nome : str
        The person name.
    """
    nome: str

    def __init__(self, nome: str) -> None:
        """
        Constructor to initialize a person.

        Parameters
        ----------
        nome : str
            The person name
        """
        self.nome = nome


class Aluno(Pessoa):
    """
    Class to represent a student.

    Attributes
    ----------
    matricula : int
        The student register.

    curso : str
        The student course.

    periodo : int
        The current student semester.

    Methods
    -------
    toString() -> str
        Method to convert the student to a string.
    """
    matricula: int
    curso: str
    periodo: int

    def __init__(self, nome: str, matricula: int, curso: str, periodo: int) -> None:
        """
        Constructor to initialize a student.

        Parameters
        -----------
        nome : str
            The student name.

        matricula : int
            The student register.

        curso : str
            The student course.

        periodo : int
            The current student semester.
        """
        super().__init__(nome)
        self.matricula = matricula
        self.curso = curso
        self.periodo = periodo


    def toString(self) -> str:
        """
        Method to convert a student to a str printable format.

        Returns
        -------
        str
            The student in str format.
        """
        return f'''
                nome: {self.nome}
                matricula: {self.matricula}
                curso: {self.curso}
                periodo: {self.periodo}
        '''


class Professor(Pessoa):
    """
    Class to represent a professor.

    Attributes
    ----------
    especialidade : str
        The professor main knowlodge.

    Methods
    -------
    toString() -> str
        Method to convert the professor to a string.
    """
    especialidade: str

    def __init__(self, nome: str, especialidade: str) -> None:
        """
        Constructor to initialize a professor.

        Parameters
        ----------
        nome : str
            The professor name.

        especialidade : str
            The professor main knowlodge.
        """
        super().__init__(nome)
        self.especialidade = especialidade

    def toString(self) -> str:
        """
        Method to convert a professor to a str printable format.

        Returns
        -------
        str
            The professor in str format.
        """
        return f'''
                Nome: {self.nome}
                Especialidade: {self.especialidade}
        ''' 


class Aula():
    """
    Class to represent a lesson.

    Attributes
    ----------
    assunto : str
        The lesson subject.

    professor : Professor
        A reference to the professor object.

    alunos : List[Aluno]
        A list containing all the students.

    Methods
    --------
    getListaPresenca() -> str
        Method to get the presence list of that lesson.
    """
    assunto: str
    professor: Professor
    alunos: List[Aluno]


    def __init__(self, assunto: str, professor: Professor, alunos: List[Aluno]) -> None:
        """
        Constructor to initialize a lesson.

        Parameters
        ----------
        assunto : str
            The lesson subject.

        professor : Professor
            A reference to the professor object.

        alunos : List[Aluno]
            A list containing all the students.
        """
        self.assunto = assunto
        self.professor = professor
        self.alunos = alunos

    def getListaPresenca(self) -> str:
        """
        Method to return the presence list.

        Returns
        ---------
        str
            The presence list.
        """
        base_string = f'''
        Aula de {self.assunto}

            - Professor: 
                {self.professor.toString()}

            - Alunos presentes:
        '''

        alunos_string = ''

        for aluno in self.alunos:
            alunos_string += aluno.toString()

        return base_string + alunos_string


# def main():
#     professor = Professor('RenZo', especialidade='Bancos de Dados')
#     alunos = [
#         Aluno('Bruno', 34, 'GES', 7),
#         Aluno('Leonardo', 44, 'GEC', 6),
#         Aluno('Davi', 54, 'GES', 2)
#     ]

#     aula = Aula('MongoDB', professor, alunos)

#     res = aula.getListaPresenca()
#     print(res)

# if __name__ == "__main__":
#     main()
