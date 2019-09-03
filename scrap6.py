from lxml import etree

elemento = etree.Element("Teste")
elemento.text = "Este é o texto da tag Teste"

print(elemento.tag)
print()

root = etree.Element("clientes")
sub = etree.SubElement(root,"cliente")

print(root.tag)
print(sub.tag)
print()

root = etree.Element("clientes")
sub = etree.Element("cliente")
root.append(sub)

print(root.tag)
print(sub.tag)
print()

clientes = etree.Element("clientes", atributo="valor")
clientes.set("codigo","1248")

cliente1 = etree.Element("cliente")
nome1 = etree.Element("nome")
nome1.text = "Gabriel"
idade1 = etree.Element("idade")
idade1.text = "32"
sexo1 = etree.Element("sexo")
sexo1.text = "Masculino"
cpf1 = etree.Element("cpf")
cpf1.text = "012.345.678-90"
cliente1.append(nome1)
cliente1.append(idade1)
cliente1.append(sexo1)
cliente1.append(cpf1)

clientes.append(cliente1)

cliente2 = etree.Element("cliente")
nome2 = etree.Element("nome")
nome2.text = "Juliana"
idade2 = etree.Element("idade")
idade2.text = "24"
sexo2 = etree.Element("sexo")
sexo2.text = "Feminino"
cpf2 = etree.Element("cpf")
cpf2.text = "123.456.789-10"
cliente2.append(nome2)
cliente2.append(idade2)
cliente2.append(sexo2)
cliente2.append(cpf2)

clientes.append(cliente2)

clientes.insert(0, etree.Element("cliente0"))
clientes.insert(0, etree.Element("cliente1"))
print(etree.tostring(clientes,pretty_print=True).decode('utf-8'))
print(len(clientes))
print(clientes.get("codigo"))
print(clientes.keys())
print(clientes.attrib)
print(clientes.attrib["atributo"])
print()
for atributo, valor in sorted(clientes.items()) :
    print(f"{atributo} = {valor}")
print()

clientes[0] = clientes[1]
for cliente_var in clientes[0:2] : 
    print(cliente_var.tag)

print(clientes is clientes[1].getparent())