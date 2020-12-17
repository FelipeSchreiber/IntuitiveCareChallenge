import tabula
import pandas as pd
import os
import zipfile

tables = tabula.read_pdf("Padrao_TISS_Componente_Organizacional_202010.pdf", pages = "all", multiple_tables = True)
tables[38].to_csv("Quadro30.csv",encoding="iso-8859-1")
tables[45].to_csv("Quadro32.csv",encoding="iso-8859-1")
quadro31 = tables[38].values.tolist()
for i in range(39,44):
    quadro31.append(list(tables[i].columns))
    quadro31.extend(tables[i].values)    
df = pd.DataFrame(quadro31,columns=tables[38].columns)
df.to_csv("Quadro31.csv",encoding="iso-8859-1",index=False)

zipf = zipfile.ZipFile("Teste_Intuitive_Care_{Felipe_Schreiber}.zip", 'w', zipfile.ZIP_DEFLATED)
for filename in os.listdir():
	if filename.endswith("csv"):
		zipf.write(filename)

