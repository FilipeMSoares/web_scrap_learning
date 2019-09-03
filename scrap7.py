from lxml import etree

funcionarios = etree.parse("funcionarios.xml")
print(funcionarios.find("funcionario"))
print()
print(funcionarios.getroot().find("funcionario"))
print()
print(funcionarios.findall("funcionario"))
print()
print(etree.tostring(funcionarios.getroot(),pretty_print=True).decode("utf-8"))
print()

todos_funcionarios = funcionarios.findall("funcionario")
for funcionario in todos_funcionarios:
    print("===============================")
    print("Tag: ", funcionario.tag.strip())
    print("Text: ", funcionario.text.strip())
    print("Tail: ", funcionario.tail.strip())
    print("Attrib: ", funcionario.attrib)

    for informacao in funcionario:
        print("**********************************")
        print("Tag: ", informacao.tag.strip())
        print("Text: ", informacao.text.strip())
        print("Tail: ", informacao.tail.strip())
        print("Attrib: ", informacao.attrib)