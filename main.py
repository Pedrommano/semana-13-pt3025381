import aluno as a;
import turma as t;

alunos = []
alunos.append(a.Aluno('Cesar', 'Arlindo', 12));
alunos.append(a.Aluno('Fabiano', 'Junior', 8));
alunos.append(a.Aluno('Lucia', 'Abreu', 7));
alunos.append(a.Aluno('Ana', 'Correa', 2));
alunos.append(a.Aluno('Pedro', 'Rocha', 5));
alunos.append(a.Aluno('Arlindo', 'Menezes', -3));

turmaObject = t.Turma();
turmaObject.cadastrarAlunos(alunos);

turmaObject.mostrarAlunos();
print('*'*30)
print('Aluno com menor nota:', turmaObject.menorNota.mostrarAluno())
print('Aluno com maior nota:', turmaObject.maiorNota.mostrarAluno())
turmaObject.maiorNota.mostrarAluno();
