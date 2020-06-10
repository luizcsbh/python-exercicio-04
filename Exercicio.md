1 - Como organizar modelos em módulos?
```
Para realizar a organização dos modelos em módulos é necessario criar dentro da pasta models criar um arquivo __init__.py para indicar que se trata de módulo.
```

2 - Como criar modelos com herança? De quais tipos?
```
Os modelos criados já são herdados de models do pacote django.db
```

3 - Como criar Enumeration types e usar como choices?
```
Enum é uma classe em python para criar enumerações, que são um conjunto de nomes simbólicos (membros) vinculados a valores constantes únicos.
import enum
```
``` python
#Using enum class create enumerations
class Days(enum.Enum):
   Sun = 1
   Mon = 2
   Tue = 3
print the enum member as a string
print ("The enum member as a string is : ",end="")
print (Days.Mon)

# print the enum member as a repr
print ("he enum member as a repr is : ",end="")
print (repr(Days.Sun))

# Check type of enum member
print ("The type of enum member is : ",end ="")
print (type(Days.Mon))

# print name of enum member
print ("The name of enum member is : ",end ="")
print (Days.Tue.name)

```

4 - No projeto da aula, crie pelo menos quatro queries customizadas. Use as informações em https://docs.djangoproject.com/en/3.0/topics/db/queries/ (Links para um site externo.)
link github

5 - O que é, para quê serve e como usar um Proxy no modelo?
```
Ao usar a herança de várias tabelas , uma nova tabela de banco de dados é criada para cada subclasse de um modelo. Esse é geralmente o comportamento desejado, pois a subclasse precisa de um local para armazenar quaisquer campos de dados adicionais que não estão presentes na classe base. Às vezes, no entanto, você deseja alterar apenas o comportamento Python de um modelo - talvez alterar o gerenciador padrão ou adicionar um novo método.

É para isso que serve a herança do modelo de proxy: criar um proxy para o modelo original. Você pode criar, excluir e atualizar instâncias do modelo de proxy e todos os dados serão salvos como se você estivesse usando o modelo original (sem proxy). A diferença é que você pode alterar coisas como a ordem do modelo padrão ou o gerente padrão no proxy, sem precisar alterar o original.
```
6 - O que faz o método __str__() em uma classe?
```
Serve para exibir o objeto para usuário final
```

7 - Quais são e para que servem as propriedades adicionais dos tipos de relacionamento/mapeamento?
```
Model relationship API usage

Many-to-many relationships

Many-to-one relationships

One-to-one relationships

```